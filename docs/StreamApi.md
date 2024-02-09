# touroptimizer_py_client.StreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error**](StreamApi.md#error) | **GET** /api/optimize/stream/error | Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
[**progress**](StreamApi.md#progress) | **GET** /api/optimize/stream/progress | Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
[**status**](StreamApi.md#status) | **GET** /api/optimize/stream/status | Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
[**warning**](StreamApi.md#warning) | **GET** /api/optimize/stream/warning | Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream


# **error**
> List[JOptOptimizationError] error()

Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream

Stream of error

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.j_opt_optimization_error import JOptOptimizationError
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
    api_instance = touroptimizer_py_client.StreamApi(api_client)

    try:
        # Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
        api_response = api_instance.error()
        print("The response of StreamApi->error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->error: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[JOptOptimizationError]**](JOptOptimizationError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **progress**
> List[JOptOptimizationProgress] progress()

Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream

Stream of progress

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.j_opt_optimization_progress import JOptOptimizationProgress
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
    api_instance = touroptimizer_py_client.StreamApi(api_client)

    try:
        # Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
        api_response = api_instance.progress()
        print("The response of StreamApi->progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[JOptOptimizationProgress]**](JOptOptimizationProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> List[JOptOptimizationStatus] status()

Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream

Stream of progress

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.j_opt_optimization_status import JOptOptimizationStatus
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
    api_instance = touroptimizer_py_client.StreamApi(api_client)

    try:
        # Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
        api_response = api_instance.status()
        print("The response of StreamApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[JOptOptimizationStatus]**](JOptOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning**
> List[JOptOptimizationWarning] warning()

Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream

text/event-stream

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.j_opt_optimization_warning import JOptOptimizationWarning
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
    api_instance = touroptimizer_py_client.StreamApi(api_client)

    try:
        # Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream
        api_response = api_instance.warning()
        print("The response of StreamApi->warning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->warning: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[JOptOptimizationWarning]**](JOptOptimizationWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

