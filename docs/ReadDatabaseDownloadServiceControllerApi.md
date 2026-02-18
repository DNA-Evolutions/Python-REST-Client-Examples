# touroptimizer_py_client.ReadDatabaseDownloadServiceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_zipped_optimization**](ReadDatabaseDownloadServiceControllerApi.md#download_zipped_optimization) | **POST** /api/db/download/downloadZippedOptimization | Download optimization by id and creator. Only works, if connected to a database.
[**download_zipped_solution**](ReadDatabaseDownloadServiceControllerApi.md#download_zipped_solution) | **POST** /api/db/download/downloadZippedSolution | Download decrypted solution by id and creator. Only works, if connected to a database.


# **download_zipped_optimization**
> bytearray download_zipped_optimization(database_item_search)

Download optimization by id and creator. Only works, if connected to a database.

Download optimizations by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseDownloadServiceControllerApi(api_client)
    database_item_search = touroptimizer_py_client.DatabaseItemSearch() # DatabaseItemSearch | 

    try:
        # Download optimization by id and creator. Only works, if connected to a database.
        api_response = api_instance.download_zipped_optimization(database_item_search)
        print("The response of ReadDatabaseDownloadServiceControllerApi->download_zipped_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseDownloadServiceControllerApi->download_zipped_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_item_search** | [**DatabaseItemSearch**](DatabaseItemSearch.md)|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-bzip2, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Optimizations triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting optimizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_zipped_solution**
> bytearray download_zipped_solution(database_item_search)

Download decrypted solution by id and creator. Only works, if connected to a database.

Download encrypted solution by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseDownloadServiceControllerApi(api_client)
    database_item_search = touroptimizer_py_client.DatabaseItemSearch() # DatabaseItemSearch | 

    try:
        # Download decrypted solution by id and creator. Only works, if connected to a database.
        api_response = api_instance.download_zipped_solution(database_item_search)
        print("The response of ReadDatabaseDownloadServiceControllerApi->download_zipped_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseDownloadServiceControllerApi->download_zipped_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_item_search** | [**DatabaseItemSearch**](DatabaseItemSearch.md)|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-bzip2, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Optimizations triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting optimizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

