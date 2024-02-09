# touroptimizer_py_client.OptimizationFAFApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_faf**](OptimizationFAFApi.md#run_faf) | **POST** /api/optimizefaf/runFAF | Provide an optimization and let JOpt solve it.
[**run_only_result_faf**](OptimizationFAFApi.md#run_only_result_faf) | **POST** /api/optimizefaf/runOnlyResultFAF | 


# **run_faf**
> bool run_faf(rest_optimization)

Provide an optimization and let JOpt solve it.

The entry point to access the JOpt.TourOptimization optimization service in fire and forget mode. Once you have set up an input, you can let JOpt find an optimal solution for your setup.

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
    api_instance = touroptimizer_py_client.OptimizationFAFApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it.
        api_response = api_instance.run_faf(rest_optimization)
        print("The response of OptimizationFAFApi->run_faf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationFAFApi->run_faf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Once the optimizer has started, it will return a started signal. |  -  |
**401** | Unauthorized Access / License not valid / Limited Endpoint |  -  |
**500** | Internal Server Error / A problem occured during Optimization start |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_only_result_faf**
> bool run_only_result_faf(rest_optimization)



The entry point to access the JOpt.TourOptimization optimization service in fire and forget mode. Once you have set up an input, you can let JOpt find an optimal solution for your setup.

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
    api_instance = touroptimizer_py_client.OptimizationFAFApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        api_response = api_instance.run_only_result_faf(rest_optimization)
        print("The response of OptimizationFAFApi->run_only_result_faf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationFAFApi->run_only_result_faf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Once the optimizer has started, it will return a started signal. |  -  |
**500** | Internal Server Error / A problem occured during Optimization |  -  |
**401** | Unauthorized Access / License not valid / Limited Endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

