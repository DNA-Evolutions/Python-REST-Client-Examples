"""
Minimal getting-started example using the generated API client directly.

Shows how to use the HealthApi without the TourOptimizerRestCaller wrapper.
This is useful for understanding the raw API client pattern:
1. Create an ApiClient instance.
2. Instantiate the desired API class (HealthApi, OptimizationApi, etc.).
3. Configure the host URL.
4. Call the API method.

Prerequisites:
- A running TourOptimizer instance on http://localhost:8081.

Usage:
    python examples/first_optimization_example.py
"""

import touroptimizer_py_client
from touroptimizer_py_client.api.health_api import HealthApi
from pprint import pprint


if __name__ == "__main__":
    # Create an API client and call the health endpoint directly
    api_client = touroptimizer_py_client.ApiClient()
    api_instance = HealthApi(api_client)
    api_instance.api_client.configuration.host = "http://localhost:8081"

    try:
        api_response = api_instance.get_health()
        pprint(api_response)
    except touroptimizer_py_client.ApiException as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)
