# touroptimizer_py_client.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobApi.md#create_job) | **POST** /api/v1/jobs | Submit an optimization job.
[**delete_job**](JobApi.md#delete_job) | **DELETE** /api/v1/jobs/{jobId} | Delete all persisted data for a job.
[**export_job**](JobApi.md#export_job) | **GET** /api/v1/jobs/{jobId}/export | Download the optimization result as a ZIP archive.
[**get_job_errors**](JobApi.md#get_job_errors) | **GET** /api/v1/jobs/{jobId}/errors | Retrieve error messages for a job.
[**get_job_progress**](JobApi.md#get_job_progress) | **GET** /api/v1/jobs/{jobId}/progress | Retrieve progress snapshots for a job.
[**get_job_result**](JobApi.md#get_job_result) | **GET** /api/v1/jobs/{jobId}/result | Retrieve the full optimization result for a job.
[**get_job_solution**](JobApi.md#get_job_solution) | **GET** /api/v1/jobs/{jobId}/solution | Retrieve the solution payload for a job.
[**get_job_status**](JobApi.md#get_job_status) | **GET** /api/v1/jobs/{jobId}/status | Retrieve status updates for a job.
[**get_job_warnings**](JobApi.md#get_job_warnings) | **GET** /api/v1/jobs/{jobId}/warnings | Retrieve warning messages for a job.
[**import_job**](JobApi.md#import_job) | **POST** /api/v1/jobs/import | Import a pre-computed optimization result into the database.
[**list_jobs**](JobApi.md#list_jobs) | **POST** /api/v1/jobs/search | Search persisted optimization jobs and return metadata summaries.
[**stop_job**](JobApi.md#stop_job) | **POST** /api/v1/jobs/{jobId}/stop | Stop a running job gracefully.


# **create_job**
> JobAcceptedResponse create_job(x_tenant_id, rest_optimization)

Submit an optimization job.

Accepts a RestOptimization payload and starts processing asynchronously. Returns HTTP 202 with a JobAcceptedResponse containing a unique jobId. Use the jobId with X-Tenant-Id to poll the job read endpoints for status, progress, warnings, errors, and the final result. Persistence is scoped to the tenant identified by the X-Tenant-Id header.

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.models.job_accepted_response import JobAcceptedResponse
from touroptimizer_py_client.models.rest_optimization import RestOptimization
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant.
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Submit an optimization job.
        api_response = api_instance.create_job(x_tenant_id, rest_optimization)
        print("The response of JobApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant. | 
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

[**JobAcceptedResponse**](JobAcceptedResponse.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job accepted. Optimization is running asynchronously. Poll /api/v1/jobs/{jobId}/status for progress. |  -  |
**400** | Bad request: invalid input or weak encryption secret. |  -  |
**401** | Unauthorized: license not valid, element limit exceeded, or tenant not identified. |  -  |
**500** | Internal server error during optimization startup. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> bool delete_job(job_id, x_tenant_id)

Delete all persisted data for a job.

Permanently removes the optimization result and all associated stream documents (progress, status, warnings, errors) for the given jobId from the database. Does not stop a running optimization — call POST /api/v1/jobs/{jobId}/stop first and wait for the job to terminate before deleting. Idempotent: returns 200 even if no data exists for this jobId.

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'x_tenant_id_example' # str | Tenant identifier injected by the API gateway.

    try:
        # Delete all persisted data for a job.
        api_response = api_instance.delete_job(job_id, x_tenant_id)
        print("The response of JobApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 

### Return type

**bool**

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All persisted data for this job has been removed. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: deletion failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_job**
> bytearray export_job(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)

Download the optimization result as a ZIP archive.

Returns a ZIP archive of the persisted optimization result for the given job. If the result was stored with client-side encryption, provide the original passphrase via X-Encryption-Secret and the archive will be decrypted before streaming. For KMS-encrypted or unencrypted results the header can be omitted — decryption is handled transparently by the server. The Content-Disposition header carries the suggested filename.

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    x_encryption_secret = 'x_encryption_secret_example' # str | Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Download the optimization result as a ZIP archive.
        api_response = api_instance.export_job(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)
        print("The response of JobApi->export_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->export_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **x_encryption_secret** | **str**| Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

**bytearray**

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ZIP archive of the optimization result. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**404** | No result found for this jobId. The job may still be running. |  -  |
**500** | Internal server error: database read or decryption failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_errors**
> List[JOptOptimizationError] get_job_errors(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)

Retrieve error messages for a job.

Returns persisted error messages for the given job. Errors are only persisted if saveError was enabled in the MongoOptimizationPersistenceSetting.

### Example

* Api Key Authentication (TenantId):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    limit = 56 # int | Maximum number of errors to return. (optional)
    sort_direction = 'sort_direction_example' # str | Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve error messages for a job.
        api_response = api_instance.get_job_errors(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)
        print("The response of JobApi->get_job_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **limit** | **int**| Maximum number of errors to return. | [optional] 
 **sort_direction** | **str**| Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**List[JOptOptimizationError]**](JOptOptimizationError.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error messages for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: database read failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_progress**
> List[JOptOptimizationProgress] get_job_progress(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)

Retrieve progress snapshots for a job.

Returns persisted progress snapshots for the given job. Progress events are only persisted if saveProgress was enabled in the MongoOptimizationPersistenceSetting.

### Example

* Api Key Authentication (TenantId):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    limit = 56 # int | Maximum number of snapshots to return. (optional)
    sort_direction = 'sort_direction_example' # str | Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve progress snapshots for a job.
        api_response = api_instance.get_job_progress(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)
        print("The response of JobApi->get_job_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **limit** | **int**| Maximum number of snapshots to return. | [optional] 
 **sort_direction** | **str**| Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**List[JOptOptimizationProgress]**](JOptOptimizationProgress.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Progress snapshots for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: database read failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_result**
> RestOptimization get_job_result(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)

Retrieve the full optimization result for a job.

Loads the complete persisted optimization snapshot for the given jobId, scoped to the authenticated tenant. If the result was client-encrypted, provide the original secret via X-Encryption-Secret; for KMS-encrypted or unencrypted results the header can be omitted.

### Example

* Api Key Authentication (TenantId):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    x_encryption_secret = 'x_encryption_secret_example' # str | Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve the full optimization result for a job.
        api_response = api_instance.get_job_result(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)
        print("The response of JobApi->get_job_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **x_encryption_secret** | **str**| Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**RestOptimization**](RestOptimization.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full optimization result for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: database read or decryption failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_solution**
> Solution get_job_solution(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)

Retrieve the solution payload for a job.

Returns the Solution portion of the optimization result only, omitting the full optimization input echo. Useful for lightweight integrations that do not need the complete RestOptimization envelope. If the result was client-encrypted, provide X-Encryption-Secret.

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.models.solution import Solution
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    x_encryption_secret = 'x_encryption_secret_example' # str | Client decryption secret. Required only for CLIENT-mode encrypted results. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve the solution payload for a job.
        api_response = api_instance.get_job_solution(job_id, x_tenant_id, x_encryption_secret=x_encryption_secret, time_out=time_out)
        print("The response of JobApi->get_job_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_solution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **x_encryption_secret** | **str**| Client decryption secret. Required only for CLIENT-mode encrypted results. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**Solution**](Solution.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution payload for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**404** | No solution found: the job may still be running or produced no result. |  -  |
**500** | Internal server error: database read or decryption failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_status**
> List[JOptOptimizationStatus] get_job_status(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)

Retrieve status updates for a job.

Returns persisted status lifecycle events for the given job (e.g. RUNNING, SUCCESS_WITH_SOLUTION, ERROR). Status events are only persisted if saveStatus was enabled in the MongoOptimizationPersistenceSetting.

### Example

* Api Key Authentication (TenantId):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    limit = 56 # int | Maximum number of events to return. (optional)
    sort_direction = 'sort_direction_example' # str | Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve status updates for a job.
        api_response = api_instance.get_job_status(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)
        print("The response of JobApi->get_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **limit** | **int**| Maximum number of events to return. | [optional] 
 **sort_direction** | **str**| Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**List[JOptOptimizationStatus]**](JOptOptimizationStatus.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status events for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: database read failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_warnings**
> List[JOptOptimizationWarning] get_job_warnings(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)

Retrieve warning messages for a job.

Returns persisted warning messages for the given job. Warnings are only persisted if saveWarning was enabled in the MongoOptimizationPersistenceSetting.

### Example

* Api Key Authentication (TenantId):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway.
    limit = 56 # int | Maximum number of warnings to return. (optional)
    sort_direction = 'sort_direction_example' # str | Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. (optional)
    time_out = 'time_out_example' # str | Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. (optional)

    try:
        # Retrieve warning messages for a job.
        api_response = api_instance.get_job_warnings(job_id, x_tenant_id, limit=limit, sort_direction=sort_direction, time_out=time_out)
        print("The response of JobApi->get_job_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job_warnings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 
 **limit** | **int**| Maximum number of warnings to return. | [optional] 
 **sort_direction** | **str**| Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC. | [optional] 
 **time_out** | **str**| Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M. | [optional] 

### Return type

[**List[JOptOptimizationWarning]**](JOptOptimizationWarning.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Warning messages for the given jobId. |  -  |
**401** | Unauthorized: jobId/tenantId missing, invalid, or not matching. |  -  |
**500** | Internal server error: database read failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_job**
> JobAcceptedResponse import_job(x_tenant_id, rest_optimization)

Import a pre-computed optimization result into the database.

Persists a RestOptimization payload directly without running the optimizer. The call blocks until the write completes. Returns a JobAcceptedResponse containing the generated jobId, which can be used immediately with GET /api/v1/jobs/{jobId}/result to retrieve the imported result. Persistence must be enabled in the RestOptimization extension settings. The tenant is scoped by the X-Tenant-Id header.

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.models.job_accepted_response import JobAcceptedResponse
from touroptimizer_py_client.models.rest_optimization import RestOptimization
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant.
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Import a pre-computed optimization result into the database.
        api_response = api_instance.import_job(x_tenant_id, rest_optimization)
        print("The response of JobApi->import_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->import_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant. | 
 **rest_optimization** | [**RestOptimization**](RestOptimization.md)|  | 

### Return type

[**JobAcceptedResponse**](JobAcceptedResponse.md)

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Import successful. The returned jobId can be used with the job read endpoints. |  -  |
**400** | Bad request: persistence is disabled in the RestOptimization extension settings. Enable persistence before calling this endpoint. |  -  |
**401** | Unauthorized: tenant not identified. |  -  |
**500** | Internal server error: database write failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> List[DatabaseInfoSearchResult] list_jobs(database_info_search, x_tenant_id=x_tenant_id)

Search persisted optimization jobs and return metadata summaries.

Accepts a DatabaseInfoSearch body and returns a stream of metadata summaries for all matching optimization jobs. All fields in the search body are optional and combinable. Results are sorted by upload date, newest first by default. Each entry contains a jobId that can be used directly with GET /api/v1/jobs/{jobId}/result to retrieve the full optimization result. Fields absent for encrypted jobs (creator, ident, status, createdTimeStamp) are omitted from each result entry. On-premise only: requires a connected database.

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
    api_instance = touroptimizer_py_client.JobApi(api_client)
    database_info_search = touroptimizer_py_client.DatabaseInfoSearch() # DatabaseInfoSearch | 
    x_tenant_id = 'tenant-abc-123' # str | Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted. (optional)

    try:
        # Search persisted optimization jobs and return metadata summaries.
        api_response = api_instance.list_jobs(database_info_search, x_tenant_id=x_tenant_id)
        print("The response of JobApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_info_search** | [**DatabaseInfoSearch**](DatabaseInfoSearch.md)|  | 
 **x_tenant_id** | **str**| Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted. | [optional] 

### Return type

[**List[DatabaseInfoSearchResult]**](DatabaseInfoSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata summaries for jobs matching the search criteria. Empty stream if no jobs match. |  -  |
**400** | Bad request: malformed or unreadable request body. |  -  |
**401** | Unauthorized: no usable filter criteria provided. Supply at least one of jobId, creator, or ident in the request body. |  -  |
**500** | Internal server error: database query failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_job**
> bool stop_job(job_id, x_tenant_id)

Stop a running job gracefully.

Sends a graceful stop signal to the running optimization identified by jobId. The optimizer finishes its current iteration and persists the best result found so far. Returns immediately — the stop may take several seconds to complete. Poll GET /api/v1/jobs/{jobId}/status to confirm termination. Returns 200 if the job was found and the signal was sent. Returns 404 if the job is not running (already completed or never started).

### Example

* Api Key Authentication (TenantId):

```python
import touroptimizer_py_client
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TenantId
configuration.api_key['TenantId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TenantId'] = 'Bearer'

# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.JobApi(api_client)
    job_id = 'job_id_example' # str | Unique job identifier from the JobAcceptedResponse.
    x_tenant_id = 'x_tenant_id_example' # str | Tenant identifier injected by the API gateway.

    try:
        # Stop a running job gracefully.
        api_response = api_instance.stop_job(job_id, x_tenant_id)
        print("The response of JobApi->stop_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->stop_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier from the JobAcceptedResponse. | 
 **x_tenant_id** | **str**| Tenant identifier injected by the API gateway. | 

### Return type

**bool**

### Authorization

[TenantId](../README.md#TenantId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stop signal sent. The job will terminate shortly. |  -  |
**404** | No active run found for this jobId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

