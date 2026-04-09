"""
Load an unencrypted job result from the database.

Demonstrates how to retrieve a previously persisted optimization result using its
job_id. The job_id can be obtained either from the JobAcceptedResponse when the
job was created, or by searching via list_jobs (see the searchFAF example).

Uses JobApi's get_job_result endpoint (GET /api/v1/jobs/{jobId}/result).

Prerequisites:
- A running TourOptimizer instance with database support.
- A valid job_id from a previously completed job.

Usage:
    python examples/loadFAF/tour_optimizer_load_faf_example.py
"""

import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from util.test_faf_helper import TestFAFHelper
from pprint import pprint

from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult

from typing import List

def main():
    """Load and print an unencrypted optimization result from the database."""

    # Modify these variables as needed
    is_azure_call = False  # Set to True if using Azure, make sure a local docker container is running otherwise
    my_azure_api_key = None  # Empty key will be ignored
    tenant_id = "DEFAULT_TENANT"

    # Initialize TourOptimizer REST caller
    if is_azure_call:
        tour_optimizer_caller = TourOptimizerRestCaller(
            tour_optimizer_url=Endpoints.AZURE_SWAGGER_TOUROPTIMIZER_URL,
            azure_api_key=my_azure_api_key
        )
    else:
        tour_optimizer_caller = TourOptimizerRestCaller(
            tour_optimizer_url=Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_URL
        )


    # Let's assume we have a search result like:
    # [DatabaseInfoSearchResult(
    #    creator='TEST_PY_FAF_CREATOR',
    #    ident='TEST_PY_FAF_IDENT',
    #    created_date=None,
    #    type='OptimizationConfig<JSONConfig>',
    #    content_type='application/x-bzip2',
    #    id='655dd1d3c59d291272f566c9')
    # ]

    job_id = "655ddcc7c59d291272f566d1" # Needs to be a valid job_id. Either save externally, or search it first via list_jobs
    loaded_opti = tour_optimizer_caller.get_job_result(job_id, tenant_id=tenant_id, time_out="PT1M")

    # Print result
    pprint(TourOptimizerRestCaller.to_json(loaded_opti))


if __name__ == "__main__":
    main()
