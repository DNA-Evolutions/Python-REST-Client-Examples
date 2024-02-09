# DatabaseItemSearch

DatabaseItemSearch model for a databse serach of items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | A related creator. | [optional] 
**id** | **str** | The unique id.Can not be empty. | [optional] 
**time_out** | **str** | The timeOut for the request. By default one minute | [optional] 

## Example

```python
from touroptimizer_py_client.models.database_item_search import DatabaseItemSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseItemSearch from a JSON string
database_item_search_instance = DatabaseItemSearch.from_json(json)
# print the JSON string representation of the object
print DatabaseItemSearch.to_json()

# convert the object into a dict
database_item_search_dict = database_item_search_instance.to_dict()
# create an instance of DatabaseItemSearch from a dict
database_item_search_form_dict = database_item_search.from_dict(database_item_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


