from touroptimizer_py_client.models.rest_optimization import RestOptimization

from touroptimizer_py_client.api import optimization_service_controller_api
from touroptimizer_py_client.api import optimization_faf_service_controller_api
from touroptimizer_py_client.api import read_database_service_controller_api
from touroptimizer_py_client.api import read_database_encrypted_service_controller_api
from touroptimizer_py_client.api import optimization_health_controller_api

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

import aiohttp
from builtins import staticmethod

from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult
from touroptimizer_py_client.models.database_encrypted_item_search import DatabaseEncryptedItemSearch

from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch

from typing import List

class TourOptimizerRestCaller:
    """
    A class to handle interactions with the Tour Optimizer REST API. It provides methods for running optimizations,
    handling response streams, and managing output data.
    """
    
    def __init__(self, tour_optimizer_url=Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_URL, azure_api_key=None):
        """
        Initializes the TourOptimizerRestCaller with the given URL and Azure API key.

        :param tour_optimizer_url: URL of the Tour Optimizer API.
        :param azure_api_key: Optional Azure API key for authentication.
        """
        self.tour_optimizer_url = tour_optimizer_url
        self.api_instance = None
        self.api_faf_instance = None
        self.api_read_faf_instance = None
        self.api_read_encrypted_faf_instance = None
        self.api_health_instance = None

    def _initialize_api_client(self):
        """
        Initializes the API client for general optimization processes.
        """
        with touroptimizer_py_client.ApiClient() as api_client:
            self.api_instance = optimization_service_controller_api.OptimizationServiceControllerApi(api_client)
            self.api_instance.api_client.configuration.host = self.tour_optimizer_url
            pprint(self.api_instance.api_client.configuration.host)
            
    def _initialize_api_faf_client(self):
        """
        Initializes the API client for fire-and-forget optimization processes.
        """
        with touroptimizer_py_client.ApiClient() as api_client:
            self.api_faf_instance = optimization_faf_service_controller_api.OptimizationFAFServiceControllerApi(api_client)
            self.api_faf_instance.api_client.configuration.host = self.tour_optimizer_url
            pprint(self.api_faf_instance.api_client.configuration.host)

    def _initialize_api_read_faf_client(self):
        """
        Initializes the API client for search in database of fire-and-forget optimization processes.
        """
        with touroptimizer_py_client.ApiClient() as api_client:
            self.api_read_faf_instance = read_database_service_controller_api.ReadDatabaseServiceControllerApi(api_client)
            self.api_read_faf_instance.api_client.configuration.host = self.tour_optimizer_url
            pprint(self.api_read_faf_instance.api_client.configuration.host)
            

    def _initialize_api_read_encrypted_faf_client(self):
        """
        Initializes the API client for search in database of fire-and-forget optimization processes.
        """
        with touroptimizer_py_client.ApiClient() as api_client:
            self.api_read_encrypted_faf_instance = read_database_encrypted_service_controller_api.ReadDatabaseEncryptedServiceControllerApi(api_client)
            self.api_read_encrypted_faf_instance.api_client.configuration.host = self.tour_optimizer_url
            pprint(self.api_read_encrypted_faf_instance.api_client.configuration.host)
            
    def _initialize_health_api_client(self):
        """
        Initializes the API client for search in database of fire-and-forget optimization processes.
        """
        with touroptimizer_py_client.ApiClient() as api_client:
            self.api_health_instance = optimization_health_controller_api.OptimizationHealthControllerApi(api_client)
            self.api_health_instance.api_client.configuration.host = self.tour_optimizer_url
            pprint(self.api_health_instance.api_client.configuration.host)

    #
    #
    #
            
    async def process_stream(self, path):
        """
        Asynchronously processes the stream from the given path.

        :param path: Path of the stream to be processed.
        """
        async with aiohttp.ClientSession() as session:
            url = self.tour_optimizer_url + path
            print(f"Accessing URL: {url}")
            async with session.get(url) as response:
                stream = response.content
                
                # Writing the stream
                async for line in stream:
                    print(line.decode().strip())       
    
    def attach_to_streams(self):
        """
        Sets up and manages the processing of streams. If optimization has started, it runs stream processing tasks concurrently.
        """
        if self._initialize_api_client is None:
            self._initialize_api_client()
          
        try: 
            started = self.api_instance.run_started_sginal()
        
            if started:
                print("Optimization stated")
                
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                stream_paths = Endpoints.STREAM_REL_ENDPOINTS
                
                # Create tasks for each path
                tasks = [self.process_stream(path) for path in stream_paths]
                
                # Run all tasks concurrently
                loop.run_until_complete(asyncio.gather(*tasks))
                loop.close()

        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->run_started_sginal: %s\n" % e)   
            
                  
    def optimize(self, opti: RestOptimization) -> RestOptimization:
        """
        Runs an optimization process using the given RestOptimization object.

        :param opti: RestOptimization object to be optimized.
        :return: Result of the optimization process.
        """
        print("Init Optimization")
        if self.api_instance is None:
            self._initialize_api_client()
        
        print("Attaching to streams")
        
        thread = threading.Thread(target=self.attach_to_streams)
        thread.start()
        
        try:
            print("Run Optimization")
            opti_ran = self.api_instance.run(opti)
            return opti_ran
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->run: %s\n" % e)

    # FAF        
    def optimize_faf(self, opti: RestOptimization) -> bool:
        """
        Executes a fire-and-forget optimization process.

        :param opti: RestOptimization object to be optimized.
        :return: Boolean indicating the success of the operation.
        """

        print("Starting Optimization")
        if self.api_faf_instance is None:
            self._initialize_api_faf_client()
        
        try:
            opti_ran_bool = self.api_faf_instance.run_faf(opti)
            return opti_ran_bool
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->run_faf: %s\n" % e)
            
        # FAF        
    def optimize_only_result_faf(self, opti: RestOptimization) -> bool:
        """
        Executes a fire-and-forget optimization process.

        :param opti: RestOptimization object to be optimized.
        :return: Boolean indicating the success of the operation.
        """

        print("Starting Optimization - Only Result")
        if self.api_faf_instance is None:
            self._initialize_api_faf_client()
        
        try:
            opti_ran_bool = self.api_faf_instance.run_only_result_faf(opti)
            return opti_ran_bool
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->run_only_result_faf: %s\n" % e)
            
    # FAF Read       
    def find_optimization_infos_in_database(self, search_info: DatabaseInfoSearch) -> List[DatabaseInfoSearchResult]:
        print("Search Optimization info")
        if self.api_read_faf_instance is None:
            self._initialize_api_read_faf_client()
        
        try:
            infos = self.api_read_faf_instance.finds_optimization_infos(search_info)
            return infos
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->find_optimization_infos_in_database: %s\n" % e)
            
            
    # FAF Read       
    def find_optimization_in_database(self, search_item: DatabaseItemSearch) -> RestOptimization:
        print("Search Optimization")
        if self.api_read_faf_instance is None:
            self._initialize_api_read_faf_client()
        
        try:
            opti = self.api_read_faf_instance.find_optimization(search_item)
            return opti
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->find_optimization_in_database: %s\n" % e)
            
        # FAF Read       
    def find_encrypted_optimization_in_database(self, search_item: DatabaseEncryptedItemSearch) -> RestOptimization:
        print("Search encrypted Optimization")
        if self.api_read_encrypted_faf_instance is None:
            self._initialize_api_read_encrypted_faf_client()
        
        try:
            opti = self.api_read_encrypted_faf_instance.find_encrypted_optimization(search_item)
            return opti
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->find_encrypted_optimization_in_database: %s\n" % e)
    
    # Health        
    def health(self) -> Status:
        """
        Executes a fire-and-forget optimization process.

        :return: Status indicating the success of the sever.
        """

        print("Starting Optimization")
        if self.api_health_instance is None:
            self._initialize_health_api_client()
        
        try:
            status = self.api_health_instance.health_status()
            return status
        except touroptimizer_py_client.ApiException as e:
            print("Exception when calling OptimizationApi->health_status: %s\n" % e)       
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
    pprint(opti_ran.extension.text_solution.text_solution)
    
    pprint(TourOptimizerRestCaller.to_json(opti))
