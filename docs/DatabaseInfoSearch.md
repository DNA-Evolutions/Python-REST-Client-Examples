# DatabaseInfoSearch

DatabaseInfoSearch model for a databse search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | A related creator. | [optional] 
**ident** | **str** | The ident of the optimization to serach for. Leave blank if not required | [optional] 
**limit** | **int** | The max number of results. Results are sorted by creation. Newest first by default | [optional] 
**sort_direction** | **str** | The sort direction of the createdDate. By default descending (DESC) newest first. For oldest first, use ASC (ascending) | [optional] 
**created_date_start** | **datetime** | The snapshot was created AFTER this time. Leave blank if not required. | [optional] 
**created_date_end** | **datetime** | The snapshot was created BEFORE this time. Leave blank if not required. | [optional] 
**time_out** | **str** | The timeOut for the request. By default one minute | [optional] 

## Example

```python
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInfoSearch from a JSON string
database_info_search_instance = DatabaseInfoSearch.from_json(json)
# print the JSON string representation of the object
print DatabaseInfoSearch.to_json()

# convert the object into a dict
database_info_search_dict = database_info_search_instance.to_dict()
# create an instance of DatabaseInfoSearch from a dict
database_info_search_form_dict = database_info_search.from_dict(database_info_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


