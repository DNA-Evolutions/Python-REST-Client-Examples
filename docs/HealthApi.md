# touroptimizer_py_client.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /api/v1/health | Get the health status of this service.


# **get_health**
> Status get_health()

Get the health status of this service.

Returns the current health status reported by Spring Boot Actuator. HTTP 200 indicates the service is UP and ready to accept requests. HTTP 503 indicates the service is DOWN, OUT_OF_SERVICE, or in an UNKNOWN state.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.status import Status
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.HealthApi(api_client)

    try:
        # Get the health status of this service.
        api_response = api_instance.get_health()
        print("The response of HealthApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is UP. |  -  |
**503** | Service is DOWN, OUT_OF_SERVICE, or UNKNOWN. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

