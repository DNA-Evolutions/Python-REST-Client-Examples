import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from pprint import pprint

def main():
    """
    Example of using the TourOptimizer REST API in Python.
    """

    # Modify these variables as needed
    is_azure_call = False  # Set to True if using Azure, make sure a local docker container is running otherwise
    my_azure_api_key = None  # Empty key will be ignored
    my_tour_optimizer_key = None # Empty key will fallback to default public JSON license
    is_save_to_json = True
    pprint_json_result = True

    # Default positions for nodes and resources
    node_positions = TestPositionsInput.default_sydney_node_positions()
    resource_positions = TestPositionsInput.default_sydney_resource_positions()
    
    # Empty connections will trigger automatic haversine distance calculations
    empty_connections = []
    empty_node_relations = [] 
    
    
    # We use:
    # LOCAL_SWAGGER_TOUROPTIMIZER_FROM_DOCKER_URL = "http://host.docker.internal:8081"
    #
    # This way we can access a running tourOptimizer on the host system of this containerized sandbox
    
    # Initialize TourOptimizer REST caller
    if is_azure_call:
        tour_optimizer_caller = TourOptimizerRestCaller(
            tour_optimizer_url=Endpoints.AZURE_SWAGGER_TOUROPTIMIZER_URL,
            azure_api_key=my_azure_api_key
        )
    else:
        tour_optimizer_caller = TourOptimizerRestCaller(
            tour_optimizer_url=Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_FROM_DOCKER_URL
        )
        
        
        
    # Create a RestOptimization instance
    opti = TestRestOptimizationCreator.default_touroptimizer_position_test_input(node_positions, 
                                                                                 resource_positions, 
                                                                                 empty_node_relations, 
                                                                                 empty_connections,
                                                                                 my_tour_optimizer_key)
    
    
    
    # Set some properties, we could do that already during creation (recommended)
    opti.ident = "TEST_PY_IDENT"
    
    # Call the optimizer
    result = tour_optimizer_caller.optimize(opti)
    
    # Print result
    pprint(result.extension.text_solution.text_solution)
    
    # Print as json result
    if pprint_json_result:
        pprint(TourOptimizerRestCaller.to_json(opti))
    
    # Save to JSON file
    if is_save_to_json:
        json_file = "OptimizationExportTest.json"
        TourOptimizerRestCaller.save_to_json_file(opti, json_file)


if __name__ == "__main__":
    main()