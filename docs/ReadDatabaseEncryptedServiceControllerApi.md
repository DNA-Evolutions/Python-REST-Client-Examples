# touroptimizer_py_client.ReadDatabaseEncryptedServiceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_encrypted_optimization**](ReadDatabaseEncryptedServiceControllerApi.md#find_encrypted_optimization) | **POST** /api/db/read/findEncryptedOptimization | Find encrypted optimizations by id and creator. Only works, if connected to a database.
[**find_encrypted_solution**](ReadDatabaseEncryptedServiceControllerApi.md#find_encrypted_solution) | **POST** /api/db/read/findEncryptedSolution | Find encrypted solutions by id and creator. Only works, if connected to a database.


# **find_encrypted_optimization**
> RestOptimization find_encrypted_optimization(database_encrypted_item_search)

Find encrypted optimizations by id and creator. Only works, if connected to a database.

Find encrypted optimizations by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_encrypted_item_search import DatabaseEncryptedItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseEncryptedServiceControllerApi(api_client)
    database_encrypted_item_search = touroptimizer_py_client.DatabaseEncryptedItemSearch() # DatabaseEncryptedItemSearch | 

    try:
        # Find encrypted optimizations by id and creator. Only works, if connected to a database.
        api_response = api_instance.find_encrypted_optimization(database_encrypted_item_search)
        print("The response of ReadDatabaseEncryptedServiceControllerApi->find_encrypted_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseEncryptedServiceControllerApi->find_encrypted_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_encrypted_item_search** | [**DatabaseEncryptedItemSearch**](DatabaseEncryptedItemSearch.md)|  | 

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
**200** | Get Optimizations triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting optimizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_encrypted_solution**
> Solution find_encrypted_solution(database_encrypted_item_search)

Find encrypted solutions by id and creator. Only works, if connected to a database.

Find encrypted solutions by id and creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_encrypted_item_search import DatabaseEncryptedItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseEncryptedServiceControllerApi(api_client)
    database_encrypted_item_search = touroptimizer_py_client.DatabaseEncryptedItemSearch() # DatabaseEncryptedItemSearch | 

    try:
        # Find encrypted solutions by id and creator. Only works, if connected to a database.
        api_response = api_instance.find_encrypted_solution(database_encrypted_item_search)
        print("The response of ReadDatabaseEncryptedServiceControllerApi->find_encrypted_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseEncryptedServiceControllerApi->find_encrypted_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_encrypted_item_search** | [**DatabaseEncryptedItemSearch**](DatabaseEncryptedItemSearch.md)|  | 

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
**200** | Get encrypted Solutions triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting solutions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

