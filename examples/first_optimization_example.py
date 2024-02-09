import time
import touroptimizer_py_client
from touroptimizer_py_client.api import optimization_health_controller_api
from touroptimizer_py_client.models.status import Status
from pprint import pprint
from touroptimizer_py_client.models.geo_node import GeoNode
from touroptimizer_py_client.models.opening_hours import OpeningHours

from touroptimizer_py_client.models.position import Position

from datetime import datetime, timedelta
from typing import List

from util.test_element_creator import TestElementsCreator


# # Defining the host is optional and defaults to http://localhost
# # See configuration.py for a list of all supported configuration parameters.
# configuration = touroptimizer_py_client.Configuration(
#     host = "http://localhost:8081"
# )
#
# from touroptimizer_py_client.model_utils import (  # noqa: F401
#     ApiTypeError,
#     ModelComposed,
#     ModelNormal,
#     ModelSimple,
#     cached_property,
#     change_keys_js_to_python,
#     convert_js_args_to_python_args,
#     date,
#     datetime,
#     file_type,
#     none_type,
#     validate_get_composed_info,
#     OpenApiModel
# )


# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = optimization_health_controller_api.OptimizationHealthControllerApi(api_client)
    api_instance.api_client.configuration.host = "http://localhost:8081"
    #pprint(api_instance.api_client.configuration.host)

    # # example, this endpoint has no required or optional parameters
    # try:
    #     # Get the health status of this endpoint.
    #     api_response = api_instance.health_status()
    #     pprint(api_response)
    #
    # except touroptimizer_py_client.ApiException as e:
    #     print("Exception when calling OptimizationHealthControllerApi->health_status: %s\n" % e)
        
        

        
# HELPERS#
    

    
## ------- Main program -------
if __name__ == "__main__":
    print("TODO")
    #TestElementsCreator.create_opening_hours(datetime(2030,12,28,8,0,0,0), datetime(2030,12,28,17,0,0,0), 'Europe/Berlin')
    #TestElementsCreator.default_geo_node(Position(51.0,52.0), "TestNode")
    #TestElementsCreator.dummy()
    #TestElementsCreator.default_test_opening_hours()
    
        # example, this endpoint has no required or optional parameters
    try:
        # Get the health status of this endpoint.
        api_response = api_instance.health_status()
        pprint(api_response)

    except touroptimizer_py_client.ApiException as e:
        print("Exception when calling OptimizationHealthControllerApi->health_status: %s\n" % e)
