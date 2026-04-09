# DatabaseInfoSearchResult

Metadata summary for a persisted optimization job. Fields absent in encrypted results (creator, ident, createdTimeStamp, status) are omitted from the response. The sec field is present only for encrypted results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | MongoDB document identifier. | [optional] 
**length** | **int** | Size of the stored document in bytes. | [optional] 
**upload_date** | **datetime** | Timestamp when the result document was written to GridFS. | [optional] 
**content_type** | **str** | MIME type of the stored content. | [optional] 
**job_id** | **str** | Unique job identifier. Matches the jobId from the JobAcceptedResponse and can be used directly with the job read endpoints. | [optional] 
**tenant_id** | **str** | Tenant identifier under which this job was persisted. | [optional] 
**type** | **str** | Internal type label of the persisted document. | [optional] 
**compression** | **str** | Compression algorithm applied before storage. | [optional] 
**encrypted** | **bool** | Whether this result is encrypted at rest. | [optional] 
**expire_at** | **datetime** | Scheduled expiry time. The database will automatically remove this document after this timestamp. | [optional] 
**creator** | **str** | Creator identifier associated with this job. Absent for client-encrypted results where cleartext metadata is not stored. | [optional] 
**ident** | **str** | User-defined label assigned to the optimization run. Absent for client-encrypted results. | [optional] 
**created_time_stamp** | **int** | Epoch-millisecond timestamp when the optimization was created internally. Absent for client-encrypted results. | [optional] 
**status** | [**OptimizationStatus**](OptimizationStatus.md) |  | [optional] 
**sec** | [**SecurityHelperItemMetadata**](SecurityHelperItemMetadata.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInfoSearchResult from a JSON string
database_info_search_result_instance = DatabaseInfoSearchResult.from_json(json)
# print the JSON string representation of the object
print(DatabaseInfoSearchResult.to_json())

# convert the object into a dict
database_info_search_result_dict = database_info_search_result_instance.to_dict()
# create an instance of DatabaseInfoSearchResult from a dict
database_info_search_result_from_dict = DatabaseInfoSearchResult.from_dict(database_info_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


