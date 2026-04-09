"""
High-level wrapper around the JOpt TourOptimizer REST API.

Provides a simplified interface for:
- Running synchronous optimizations (start_run -> get_run_result) with SSE stream monitoring.
- Submitting asynchronous job-based optimizations (create_job) with database persistence.
- Listing and retrieving persisted job results (list_jobs, get_job_result).
- Checking server health.
- Exporting optimization results to JSON.

API clients are lazily initialized on first use and reused for subsequent calls.
"""

from touroptimizer_py_client.models.rest_optimization import RestOptimization

from touroptimizer_py_client.api.optimization_api import OptimizationApi
from touroptimizer_py_client.api.job_api import JobApi
from touroptimizer_py_client.api.health_api import HealthApi

import touroptimizer_py_client
from touroptimizer_py_client.models.status import Status

from util.test_element_creator import TestElementsCreator
from util.test_position_input import TestPositionsInput
from util.test_rest_optimization_creator import TestRestOptimizationCreator

from util.tour_optimizer_endpoints import Endpoints

import asyncio
from pprint import pprint
import json
from datetime import datetime
import threading

try:
    import aiohttp  # type: ignore[import-untyped]
except ImportError:
    aiohttp = None  # type: ignore[assignment]

from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult

from typing import List, Optional

class TourOptimizerRestCaller:
    """
    A class to handle interactions with the Tour Optimizer REST API. It provides methods for running optimizations,
    handling response streams, and managing output data.
    """

    def __init__(self, tour_optimizer_url: str = Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_URL, azure_api_key: Optional[str] = None):
        """
        Initializes the TourOptimizerRestCaller with the given URL and Azure API key.

        :param tour_optimizer_url: URL of the Tour Optimizer API.
        :param azure_api_key: Optional Azure API key for authentication.
        """
        self.tour_optimizer_url = tour_optimizer_url
        self.api_instance: Optional[OptimizationApi] = None
        self.api_job_instance: Optional[JobApi] = None
        self.api_health_instance: Optional[HealthApi] = None

    def _initialize_api_client(self):
        """
        Initializes the API client for general optimization processes.
        """
        api_client = touroptimizer_py_client.ApiClient()
        self.api_instance = OptimizationApi(api_client)
        self.api_instance.api_client.configuration.host = self.tour_optimizer_url
        pprint(self.api_instance.api_client.configuration.host)

    def _initialize_api_job_client(self):
        """
        Initializes the API client for job-based (fire-and-forget) optimization processes.
        """
        api_client = touroptimizer_py_client.ApiClient()
        self.api_job_instance = JobApi(api_client)
        self.api_job_instance.api_client.configuration.host = self.tour_optimizer_url
        pprint(self.api_job_instance.api_client.configuration.host)

    def _initialize_health_api_client(self):
        """
        Initializes the API client for health checks.
        """
        api_client = touroptimizer_py_client.ApiClient()
        self.api_health_instance = HealthApi(api_client)
        self.api_health_instance.api_client.configuration.host = self.tour_optimizer_url
        pprint(self.api_health_instance.api_client.configuration.host)

    #
    #
    #

    async def process_stream(self, path: str):
        """
        Asynchronously processes the stream from the given path.

        :param path: Path of the stream to be processed.
        """
        if aiohttp is None:
            print("aiohttp is not installed, skipping stream processing")
            return

        async with aiohttp.ClientSession() as session:
            url = self.tour_optimizer_url + path
            print(f"Accessing URL: {url}")
            async with session.get(url) as response:
                stream = response.content

                # Writing the stream
                async for line in stream:
                    print(line.decode().strip())

    def attach_to_streams(self, run_id: str):
        """
        Sets up and manages the processing of streams. If optimization has started, it runs stream processing tasks concurrently.

        :param run_id: The run identifier returned by start_run.
        """
        if self.api_instance is None:
            self._initialize_api_client()

        assert self.api_instance is not None

        try:
            started = self.api_instance.get_started_signal(run_id)

            if started:
                print("Optimization started")

                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                stream_paths = Endpoints.stream_rel_endpoints(run_id)

                # Create tasks for each path
                tasks = [self.process_stream(path) for path in stream_paths]

                # Run all tasks concurrently
                loop.run_until_complete(asyncio.gather(*tasks))
                loop.close()

        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->get_started_signal: %s\n" % e)


    def optimize(self, opti: RestOptimization) -> Optional[RestOptimization]:
        """
        Runs an optimization process using the given RestOptimization object.
        First starts a run to get a run_id, then subscribes to streams and fetches the result.

        :param opti: RestOptimization object to be optimized.
        :return: Result of the optimization process, or None on failure.
        """
        print("Init Optimization")
        if self.api_instance is None:
            self._initialize_api_client()

        assert self.api_instance is not None

        try:
            print("Starting Run")
            run_accepted = self.api_instance.start_run(opti)
            run_id = run_accepted.run_id
            print(f"Run accepted with run_id: {run_id}")

            print("Attaching to streams")
            thread = threading.Thread(target=self.attach_to_streams, args=(run_id,))
            thread.start()

            print("Fetching Optimization Result")
            result = self.api_instance.get_run_result(run_id)
            return result
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi: %s\n" % e)
            return None

    # Job-based optimization (replaces FAF)
    def optimize_job(self, opti: RestOptimization, tenant_id: str = "DEFAULT_TENANT") -> Optional[str]:
        """
        Executes a job-based (fire-and-forget) optimization process.

        :param opti: RestOptimization object to be optimized.
        :param tenant_id: Tenant identifier for multi-tenant setups.
        :return: The job_id of the created job, or None on failure.
        """

        print("Starting Job Optimization")
        if self.api_job_instance is None:
            self._initialize_api_job_client()

        assert self.api_job_instance is not None

        try:
            job_accepted = self.api_job_instance.create_job(tenant_id, opti)
            print(f"Job accepted with job_id: {job_accepted.job_id}")
            return job_accepted.job_id
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling JobApi->create_job: %s\n" % e)
            return None

    # Job Read
    def list_jobs(self, search_info: DatabaseInfoSearch, tenant_id: Optional[str] = None) -> Optional[List[DatabaseInfoSearchResult]]:
        """
        Lists jobs matching the search criteria.

        :param search_info: Search criteria for finding jobs.
        :param tenant_id: Optional tenant identifier.
        :return: List of matching job info results, or None on failure.
        """
        print("Search Job info")
        if self.api_job_instance is None:
            self._initialize_api_job_client()

        assert self.api_job_instance is not None

        try:
            infos = self.api_job_instance.list_jobs(search_info, x_tenant_id=tenant_id)
            return infos
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling JobApi->list_jobs: %s\n" % e)
            return None

    # Job Read
    def get_job_result(self, job_id: str, tenant_id: str = "DEFAULT_TENANT", secret: Optional[str] = None, time_out: str = "PT1M") -> Optional[RestOptimization]:
        """
        Gets the result of a job by its ID.

        :param job_id: The job identifier.
        :param tenant_id: Tenant identifier.
        :param secret: Optional decryption secret for encrypted results.
        :param time_out: Maximum wait time (ISO 8601 duration). Defaults to PT1M.
        :return: The optimization result, or None on failure.
        """
        print("Get Job Result")
        if self.api_job_instance is None:
            self._initialize_api_job_client()

        assert self.api_job_instance is not None

        try:
            result = self.api_job_instance.get_job_result(job_id, tenant_id, x_encryption_secret=secret, time_out=time_out)
            return result
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling JobApi->get_job_result: %s\n" % e)
            return None

    # Health
    def health(self) -> Optional[Status]:
        """
        Checks the health status of the server.

        :return: Status indicating the health of the server, or None on failure.
        """

        print("Checking Health")
        if self.api_health_instance is None:
            self._initialize_health_api_client()

        assert self.api_health_instance is not None

        try:
            status = self.api_health_instance.get_health()
            return status
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling HealthApi->get_health: %s\n" % e)
            return None

    # Further helper

    @staticmethod
    def default_date_converter(o):
        if isinstance(o, datetime):
            return o.isoformat()

    @staticmethod
    def save_to_json_file(opti: RestOptimization, file_path: str):
        """
        Saves the given RestOptimization object to a JSON file.

        :param opti: RestOptimization object to be saved.
        :param file_path: Path of the file where the JSON data will be saved.
        """

        with open(file_path, 'w', encoding='utf-8') as f:
            # Convert the RestOptimization object to a dictionary
            opti_dict = opti.to_dict()
            # Use the default_converter function to handle datetime objects
            json.dump(opti_dict, f, ensure_ascii=False, indent=4, default=TourOptimizerRestCaller.default_date_converter)

    @staticmethod
    def to_json(opti: RestOptimization):
        """
        Converts a RestOptimization object to a JSON string.

        :param opti: RestOptimization object to be converted.
        :return: JSON string representation of the RestOptimization object.
        """

        opti_dict = opti.to_dict()
        # Use the default_converter function to handle datetime objects
        return json.dumps(opti_dict, ensure_ascii=False, indent=4, default=TourOptimizerRestCaller.default_date_converter)


## ------- Main program -------
if __name__ == "__main__":

    ress = TestElementsCreator.conv_poss_to_ress(TestPositionsInput.default_sydney_resource_positions())
    nodes = TestElementsCreator.conv_poss_to_nodes(TestPositionsInput.default_sydney_node_positions())

    print("Created Nodes for Rest Optimization: ")
    pprint(nodes)
    print("Created Ress for Rest Optimization: ")
    pprint(ress)

    opti = TestRestOptimizationCreator.default_touroptimizer_test_input(nodes, ress)

    rest_caller = TourOptimizerRestCaller()

    opti_ran = rest_caller.optimize(opti)
    if opti_ran and opti_ran.extension:
        pprint(opti_ran.extension.text_solution.text_solution)

    pprint(TourOptimizerRestCaller.to_json(opti))
