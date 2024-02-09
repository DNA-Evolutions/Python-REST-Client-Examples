import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from util.test_faf_helper import TestFAFHelper
from pprint import pprint

from touroptimizer_py_client.models.database_encrypted_item_search import DatabaseEncryptedItemSearch

from typing import List

def main():
    """
    Example of using the TourOptimizer REST API in Python.
    """

    # Modify these variables as needed
    is_azure_call = False  # Set to True if using Azure, make sure a local docker container is running otherwise
    my_azure_api_key = None  # Empty key will be ignored
 
    
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
    
    search_item = DatabaseEncryptedItemSearch();
    search_item.creator = "TEST_PY_FAF_CREATOR" # magic "hash:" does NOT work here!
    search_item.id = "655dfd91d6423b007cea1fbb" # Needs to be a valid id. Either save externally, or search it first
    search_item.time_out = "PT1M";
    search_item.secret = "TEST123"
    

    loaded_opti = tour_optimizer_caller.find_encrypted_optimization_in_database(search_item)
    
    
    
    # Print result
    pprint(TourOptimizerRestCaller.to_json(loaded_opti))


if __name__ == "__main__":
    main()