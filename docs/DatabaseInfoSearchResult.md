# DatabaseInfoSearchResult

DatabaseInfoSearchResult model for a serach result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | An id related to the creator that is filled out autmatically | [optional] 
**ident** | **str** | The ident of the optimization | [optional] 
**created_date** | **int** | The timestamp the snapshot was created | [optional] 
**type** | **str** | The orignal type of the search result | [optional] 
**content_type** | **str** | The content type of the search result | [optional] 
**id** | **str** | The unique id | [optional] 
**sec** | [**SecurityHelperItemMetadata**](SecurityHelperItemMetadata.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInfoSearchResult from a JSON string
database_info_search_result_instance = DatabaseInfoSearchResult.from_json(json)
# print the JSON string representation of the object
print DatabaseInfoSearchResult.to_json()

# convert the object into a dict
database_info_search_result_dict = database_info_search_result_instance.to_dict()
# create an instance of DatabaseInfoSearchResult from a dict
database_info_search_result_form_dict = database_info_search_result.from_dict(database_info_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


