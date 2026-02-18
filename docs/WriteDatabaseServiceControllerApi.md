# touroptimizer_py_client.WriteDatabaseServiceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_optimization**](WriteDatabaseServiceControllerApi.md#save_optimization) | **POST** /api/db/wirte/saveOptimization | Save optimizations. Only works, if connected to a database.


# **save_optimization**
> bool save_optimization(rest_optimization)

Save optimizations. Only works, if connected to a database.

Save optimization. Return mongo ID

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
    api_instance = touroptimizer_py_client.WriteDatabaseServiceControllerApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Save optimizations. Only works, if connected to a database.
        api_response = api_instance.save_optimization(rest_optimization)
        print("The response of WriteDatabaseServiceControllerApi->save_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WriteDatabaseServiceControllerApi->save_optimization: %s\n" % e)
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
**200** | Save optimization. If saved correctly, true is returned |  -  |
**500** | Internal Server Error / A problem occurred during saving optimization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

