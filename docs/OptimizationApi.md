# touroptimizer_py_client.OptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run**](OptimizationApi.md#run) | **POST** /api/optimize/run | Provide an optimization and let JOpt solve it.
[**run_only_result**](OptimizationApi.md#run_only_result) | **POST** /api/optimize/runOnlyResult | Provide an optimization and let JOpt solve it. You only get back the result
[**stop_optimization_run**](OptimizationApi.md#stop_optimization_run) | **POST** /api/optimize/stop | This entrypoint stops the optimization gracefully.


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
    api_instance = touroptimizer_py_client.OptimizationApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it.
        api_response = api_instance.run(rest_optimization)
        print("The response of OptimizationApi->run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationApi->run: %s\n" % e)
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
    api_instance = touroptimizer_py_client.OptimizationApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it. You only get back the result
        api_response = api_instance.run_only_result(rest_optimization)
        print("The response of OptimizationApi->run_only_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationApi->run_only_result: %s\n" % e)
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
    api_instance = touroptimizer_py_client.OptimizationApi(api_client)

    try:
        # This entrypoint stops the optimization gracefully.
        api_response = api_instance.stop_optimization_run()
        print("The response of OptimizationApi->stop_optimization_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationApi->stop_optimization_run: %s\n" % e)
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

