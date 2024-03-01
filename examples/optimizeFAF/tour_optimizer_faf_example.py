import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from util.test_faf_helper import TestFAFHelper
from pprint import pprint



def main():
    """
    Example of using the TourOptimizer REST API in Python.
    """

    # Modify these variables as needed
    is_azure_call = False  # Set to True if using Azure, make sure a local docker container is running otherwise
    my_azure_api_key = None  # Empty key will be ignored
    my_tour_optimizer_key = None # Empty key will fallback to default public JSON license
    do_hash_creator = False
    secret = "" # leave empty for unencrypted run
    
    run_only_result = False

    # Default positions for nodes and resources
    node_positions = TestPositionsInput.default_sydney_node_positions()
    resource_positions = TestPositionsInput.default_sydney_resource_positions()
    
    # Empty connections will trigger automatic haversine distance calculations
    empty_connections = []
    empty_node_relations = [] 
    
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
        
        
        
    # Create a RestOptimization instance
    opti = TestRestOptimizationCreator.default_touroptimizer_position_test_input(node_positions, 
                                                                                 resource_positions, 
                                                                                 empty_node_relations, 
                                                                                 empty_connections,
                                                                                 my_tour_optimizer_key)
    
    # Set some properties, we could do that already during creation (recommended)
    opti.ident = "TEST_PY_FAF_IDENT"
    
    # Check TestFAFHelper for details
    optimization_persistence_settings = TestFAFHelper.default_optimization_persistence_settings(secret=secret)
    
    opti.extension.persistence_setting = optimization_persistence_settings
    
    # ATTENTION: After already creating the opti instance, do not set the creator again here, as this would override the 
    # creator from the persistence settings object
    #creator = "TEST_CREATOR"
    
    
    # It is fine to set the creator for the database via extension
    if(do_hash_creator):
        creator  = "hash:"+creator
    
    opti.extension.creator_setting = TestFAFHelper.default_creator_settings(creator)
    
    # Print opti
    pprint(TourOptimizerRestCaller.to_json(opti))

    # Call the optimizer
    if(run_only_result):
        was_started = tour_optimizer_caller.optimize_only_result_faf(opti)
    else:
        was_started = tour_optimizer_caller.optimize_faf(opti)

    
    # Print result
    pprint(was_started)


if __name__ == "__main__":
    main()