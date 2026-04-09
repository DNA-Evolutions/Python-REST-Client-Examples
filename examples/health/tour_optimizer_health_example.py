"""
Health check example.

Calls the GET /api/v1/health endpoint to verify that the TourOptimizer
service is running and reachable. Prints the returned Status object.

Prerequisites:
- A running TourOptimizer instance on http://localhost:8081
  (or change is_azure_call to True and provide an Azure API key).

Usage:
    python examples/health/tour_optimizer_health_example.py
"""

import json
from util.test_element_creator import  TestElementsCreator
from util.test_rest_optimization_creator import  TestRestOptimizationCreator
from util.test_position_input import TestPositionsInput
from util.tour_optimizer_endpoints import Endpoints
from util.tour_optimizer_rest_caller import TourOptimizerRestCaller
from pprint import pprint
from touroptimizer_py_client.models.status import Status


def main():
    """Check and print the health status of the TourOptimizer service."""

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
    
    # Call the optimizer
    status = tour_optimizer_caller.health()
    
    # Print result
    pprint(status)


if __name__ == "__main__":
    main()
