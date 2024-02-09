# touroptimizer_py_client.OptimizationServiceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error**](OptimizationServiceControllerApi.md#error) | **GET** /api/optimize/stream/error | Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
[**progress**](OptimizationServiceControllerApi.md#progress) | **GET** /api/optimize/stream/progress | Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
[**run**](OptimizationServiceControllerApi.md#run) | **POST** /api/optimize/run | Provide an optimization and let JOpt solve it.
[**run_only_result**](OptimizationServiceControllerApi.md#run_only_result) | **POST** /api/optimize/runOnlyResult | Provide an optimization and let JOpt solve it. You only get back the result
[**run_started_sginal**](OptimizationServiceControllerApi.md#run_started_sginal) | **GET** /api/optimize/startedSginal | Emmits once an optimization started
[**status**](OptimizationServiceControllerApi.md#status) | **GET** /api/optimize/stream/status | Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
[**stop_optimization_run**](OptimizationServiceControllerApi.md#stop_optimization_run) | **POST** /api/optimize/stop | This entrypoint stops the optimization gracefully.
[**warning**](OptimizationServiceControllerApi.md#warning) | **GET** /api/optimize/stream/warning | Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream


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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
        api_response = api_instance.error()
        print("The response of OptimizationServiceControllerApi->error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->error: %s\n" % e)
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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
        api_response = api_instance.progress()
        print("The response of OptimizationServiceControllerApi->progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->progress: %s\n" % e)
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

# **run**
> RestOptimization run(rest_optimization)

Provide an optimization and let JOpt solve it.

The entry point to access the JOpt.TourOptimization optimization service. Once you have set up an input, you can let JOpt find an optimal solution for your setup.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.rest_optimization import RestOptimization
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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it.
        api_response = api_instance.run(rest_optimization)
        print("The response of OptimizationServiceControllerApi->run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

[**RestOptimization**](RestOptimization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Once the optimizer has finished the optimization run, it will return an OptimizationConfig JSON that contains the initial definition and the solution. |  -  |
**504** | Timeout / Optimization took too long |  -  |
**500** | Internal Server Error / A problem occured during Optimization |  -  |
**401** | Unauthorized Access / License not valid / Limited Endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_only_result**
> Solution run_only_result(rest_optimization)

Provide an optimization and let JOpt solve it. You only get back the result

The entry point to access the JOpt.TourOptimization optimization service. Once you have set up an input, you can let JOpt find an optimal solution for your setup.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.rest_optimization import RestOptimization
from touroptimizer_py_client.models.solution import Solution
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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it. You only get back the result
        api_response = api_instance.run_only_result(rest_optimization)
        print("The response of OptimizationServiceControllerApi->run_only_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->run_only_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

[**Solution**](Solution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Once the optimizer has finished the optimization run, it will return a solution/result JSON. |  -  |
**504** | Timeout / Optimization took too long |  -  |
**500** | Internal Server Error / A problem occured during Optimization |  -  |
**401** | Unauthorized Access / License not valid / Limited Endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_started_sginal**
> bool run_started_sginal()

Emmits once an optimization started

Emmits once an optimization started

### Example


```python
import touroptimizer_py_client
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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # Emmits once an optimization started
        api_response = api_instance.run_started_sginal()
        print("The response of OptimizationServiceControllerApi->run_started_sginal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->run_started_sginal: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
        api_response = api_instance.status()
        print("The response of OptimizationServiceControllerApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->status: %s\n" % e)
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

# **stop_optimization_run**
> bool stop_optimization_run()

This entrypoint stops the optimization gracefully.

Stopping the optimization gracefully (if optimization was already started) and returning the latestknown result.

### Example


```python
import touroptimizer_py_client
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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # This entrypoint stops the optimization gracefully.
        api_response = api_instance.stop_optimization_run()
        print("The response of OptimizationServiceControllerApi->stop_optimization_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->stop_optimization_run: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Once the optimizer was stopped it will return a boolean indicating it was stopped. The previously called start method will emit soon. |  -  |
**400** | Bad Request / Optimization was not started yet or already stopped. |  -  |

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
    api_instance = touroptimizer_py_client.OptimizationServiceControllerApi(api_client)

    try:
        # Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream
        api_response = api_instance.warning()
        print("The response of OptimizationServiceControllerApi->warning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationServiceControllerApi->warning: %s\n" % e)
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

