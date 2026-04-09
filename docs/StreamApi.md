# touroptimizer_py_client.StreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_started_signal**](StreamApi.md#get_started_signal) | **GET** /api/v1/runs/{runId}/started | Emits once the run has transitioned to the running state.
[**stop_run**](StreamApi.md#stop_run) | **DELETE** /api/v1/runs/{runId} | Stop an active optimization run gracefully.
[**stream_errors**](StreamApi.md#stream_errors) | **GET** /api/v1/runs/{runId}/stream/errors | SSE stream of optimization errors for a run.
[**stream_progress**](StreamApi.md#stream_progress) | **GET** /api/v1/runs/{runId}/stream/progress | SSE stream of optimization progress for a run.
[**stream_status**](StreamApi.md#stream_status) | **GET** /api/v1/runs/{runId}/stream/status | SSE stream of optimization status messages for a run.
[**stream_warnings**](StreamApi.md#stream_warnings) | **GET** /api/v1/runs/{runId}/stream/warnings | SSE stream of optimization warnings for a run.


# **get_started_signal**
> bool get_started_signal(run_id)

Emits once the run has transitioned to the running state.

Returns a single boolean true when the optimizer for the given runId transitions to the running state. Useful for clients that want to begin subscribing to event streams only after the optimizer has actually started.

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
    api_instance = touroptimizer_py_client.StreamApi(api_client)
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # Emits once the run has transitioned to the running state.
        api_response = api_instance.get_started_signal(run_id)
        print("The response of StreamApi->get_started_signal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->get_started_signal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

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
**200** | Optimization has started. |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_run**
> bool stop_run(run_id)

Stop an active optimization run gracefully.

Requests a graceful stop of the run identified by runId. The optimizer finishes its current iteration and emits the best result found so far, which is then returned by the blocking GET result endpoint. Returns 404 if the runId is unknown or already completed.

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
    api_instance = touroptimizer_py_client.StreamApi(api_client)
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # Stop an active optimization run gracefully.
        api_response = api_instance.stop_run(run_id)
        print("The response of StreamApi->stop_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->stop_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

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
**200** | Stop signal accepted. The run will terminate shortly. |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_errors**
> List[JOptOptimizationError] stream_errors(run_id)

SSE stream of optimization errors for a run.

Subscribe to receive error events for the run identified by runId. Errors indicate serious problems that may affect result quality.

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
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # SSE stream of optimization errors for a run.
        api_response = api_instance.stream_errors(run_id)
        print("The response of StreamApi->stream_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->stream_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

### Return type

[**List[JOptOptimizationError]**](JOptOptimizationError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_progress**
> List[JOptOptimizationProgress] stream_progress(run_id)

SSE stream of optimization progress for a run.

Subscribe to receive real-time progress updates for the run identified by runId. Each event contains the current progress percentage and timing information.

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
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # SSE stream of optimization progress for a run.
        api_response = api_instance.stream_progress(run_id)
        print("The response of StreamApi->stream_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->stream_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

### Return type

[**List[JOptOptimizationProgress]**](JOptOptimizationProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_status**
> List[JOptOptimizationStatus] stream_status(run_id)

SSE stream of optimization status messages for a run.

Subscribe to receive status lifecycle events for the run identified by runId (e.g. STARTED, RUNNING, FINISHED).

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
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # SSE stream of optimization status messages for a run.
        api_response = api_instance.stream_status(run_id)
        print("The response of StreamApi->stream_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->stream_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

### Return type

[**List[JOptOptimizationStatus]**](JOptOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_warnings**
> List[JOptOptimizationWarning] stream_warnings(run_id)

SSE stream of optimization warnings for a run.

Subscribe to receive warning events for the run identified by runId. Warnings indicate non-fatal issues such as unserviceable nodes or soft constraint violations.

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
    run_id = 'run_id_example' # str | Run identifier returned by POST /api/v1/runs.

    try:
        # SSE stream of optimization warnings for a run.
        api_response = api_instance.stream_warnings(run_id)
        print("The response of StreamApi->stream_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamApi->stream_warnings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier returned by POST /api/v1/runs. | 

### Return type

[**List[JOptOptimizationWarning]**](JOptOptimizationWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No active run found for this runId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

