"""
Load an encrypted job result from the database.

Same as tour_optimizer_load_faf_example.py, but passes a decryption secret
to retrieve a result that was encrypted at submission time. The secret must
match the one provided when the job was created.

Uses JobApi's get_job_result endpoint with the x_encryption_secret parameter.

Prerequisites:
- A running TourOptimizer instance with database support.
- A valid job_id from a previously completed encrypted job.
- The decryption secret used when the job was submitted.

Usage:
    python examples/loadFAF/tour_optimizer_load_encrypted_faf_example.py
"""

import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from util.test_faf_helper import TestFAFHelper
from pprint import pprint

from typing import List

def main():
    """Load and print an encrypted optimization result from the database."""

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
    #    content_type='application/octet-stream',
    #    id='655dd1d3c59d291272f566c9')
    # ]

    job_id = "655dfd91d6423b007cea1fbb" # Needs to be a valid job_id. Either save externally, or search it first via list_jobs
    secret = "TEST123" # Decryption secret for encrypted results

    loaded_opti = tour_optimizer_caller.get_job_result(job_id, tenant_id=tenant_id, secret=secret, time_out="PT1M")

    # Print result
    pprint(TourOptimizerRestCaller.to_json(loaded_opti))


if __name__ == "__main__":
    main()
