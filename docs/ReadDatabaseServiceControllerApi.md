# touroptimizer_py_client.ReadDatabaseServiceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_error**](ReadDatabaseServiceControllerApi.md#find_error) | **POST** /api/db/read/findError | Find error by creator. Only works, if connected to a database.
[**find_optimization**](ReadDatabaseServiceControllerApi.md#find_optimization) | **POST** /api/db/read/findOptimization | Find optimizations by creator and id. Only works, if connected to a database.
[**find_progress**](ReadDatabaseServiceControllerApi.md#find_progress) | **POST** /api/db/read/findProgress | Find progress by creator. Only works, if connected to a database.
[**find_solution**](ReadDatabaseServiceControllerApi.md#find_solution) | **POST** /api/db/read/findSolution | Find solutions by creator and id. Only works, if connected to a database.
[**find_status**](ReadDatabaseServiceControllerApi.md#find_status) | **POST** /api/db/read/findStatus | Find status by creator. Only works, if connected to a database.
[**find_warning**](ReadDatabaseServiceControllerApi.md#find_warning) | **POST** /api/db/read/findWarning | Find warning by creator. Only works, if connected to a database.
[**finds_optimization_infos**](ReadDatabaseServiceControllerApi.md#finds_optimization_infos) | **POST** /api/db/read/findsOptimizationInfos | Find optimization-infos by creator. Only works, if connected to a database.
[**finds_solution_infos**](ReadDatabaseServiceControllerApi.md#finds_solution_infos) | **POST** /api/db/read/findsSolutionInfos | Find solution-infos by creator. Only works, if connected to a database.


# **find_error**
> List[JOptOptimizationError] find_error(database_info_search)

Find error by creator. Only works, if connected to a database.

Find error by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find error by creator. Only works, if connected to a database.
        api_response = api_instance.find_error(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->find_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[JOptOptimizationError]**](JOptOptimizationError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error / A problem occured during requesting error |  -  |
**200** | Get error triggered by the creator in fire and forget mode. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_optimization**
> RestOptimization find_optimization(database_item_search)

Find optimizations by creator and id. Only works, if connected to a database.

Find optimizations by creator and id.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_item_search = touroptimizer_py_client.DatabaseItemSearch() # DatabaseItemSearch | 

    try:
        # Find optimizations by creator and id. Only works, if connected to a database.
        api_response = api_instance.find_optimization(database_item_search)
        print("The response of ReadDatabaseServiceControllerApi->find_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_item_search** | [**DatabaseItemSearch**](DatabaseItemSearch.md)|  | 

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

# **find_progress**
> List[JOptOptimizationProgress] find_progress(database_info_search)

Find progress by creator. Only works, if connected to a database.

Find progress by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find progress by creator. Only works, if connected to a database.
        api_response = api_instance.find_progress(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->find_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[JOptOptimizationProgress]**](JOptOptimizationProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get progress triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_solution**
> Solution find_solution(database_item_search)

Find solutions by creator and id. Only works, if connected to a database.

Find solutions by creator and id.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_item_search = touroptimizer_py_client.DatabaseItemSearch() # DatabaseItemSearch | 

    try:
        # Find solutions by creator and id. Only works, if connected to a database.
        api_response = api_instance.find_solution(database_item_search)
        print("The response of ReadDatabaseServiceControllerApi->find_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_item_search** | [**DatabaseItemSearch**](DatabaseItemSearch.md)|  | 

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
**200** | Get Solutions triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting solutions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_status**
> List[JOptOptimizationStatus] find_status(database_info_search)

Find status by creator. Only works, if connected to a database.

Find status by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find status by creator. Only works, if connected to a database.
        api_response = api_instance.find_status(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->find_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[JOptOptimizationStatus]**](JOptOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_warning**
> List[JOptOptimizationWarning] find_warning(database_info_search)

Find warning by creator. Only works, if connected to a database.

Find warning by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find warning by creator. Only works, if connected to a database.
        api_response = api_instance.find_warning(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->find_warning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->find_warning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[JOptOptimizationWarning]**](JOptOptimizationWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error / A problem occured during requesting warning |  -  |
**200** | Get warning triggered by the creator in fire and forget mode. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finds_optimization_infos**
> List[DatabaseInfoSearchResult] finds_optimization_infos(database_info_search)

Find optimization-infos by creator. Only works, if connected to a database.

Find optimization-infos by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find optimization-infos by creator. Only works, if connected to a database.
        api_response = api_instance.finds_optimization_infos(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->finds_optimization_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->finds_optimization_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[DatabaseInfoSearchResult]**](DatabaseInfoSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error / A problem occured during requesting optimization infos |  -  |
**200** | Get optimization-infos triggered by the creator in fire and forget mode. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finds_solution_infos**
> List[DatabaseInfoSearchResult] finds_solution_infos(database_info_search)

Find solution-infos by creator. Only works, if connected to a database.

Find solution-infos by creator.

### Example


```python
import touroptimizer_py_client
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult
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
    api_instance = touroptimizer_py_client.ReadDatabaseServiceControllerApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 

    try:
        # Find solution-infos by creator. Only works, if connected to a database.
        api_response = api_instance.finds_solution_infos(database_info_search)
        print("The response of ReadDatabaseServiceControllerApi->finds_solution_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadDatabaseServiceControllerApi->finds_solution_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 

### Return type

[**List[DatabaseInfoSearchResult]**](DatabaseInfoSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get solution-infos triggered by the creator in fire and forget mode. |  -  |
**500** | Internal Server Error / A problem occured during requesting solution infos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

