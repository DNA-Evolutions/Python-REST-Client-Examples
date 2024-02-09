# touroptimizer_py_client.HealthStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_status**](HealthStatusApi.md#health_status) | **GET** /healthStatus | Get the health status of this endpoint.


# **health_status**
> Status health_status()

Get the health status of this endpoint.

Get the health status of this endpoint.

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
    api_instance = touroptimizer_py_client.HealthStatusApi(api_client)

    try:
        # Get the health status of this endpoint.
        api_response = api_instance.health_status()
        print("The response of HealthStatusApi->health_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthStatusApi->health_status: %s\n" % e)
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
**503** | The server is in UNKNOWN, OUT_OF_SERVICE, or DOWN state. |  -  |
**200** | The endpoint is up and running. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

