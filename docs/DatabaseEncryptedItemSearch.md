# DatabaseEncryptedItemSearch

DatabaseEncryptedItemSearch model for a databse serach of encypted items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | A related creator. | [optional] 
**id** | **str** | The unique id.Can not be empty. | [optional] 
**time_out** | **str** | The timeOut for the request. By default one minute | [optional] 
**secret** | **str** | An optional password for encryption. Can not be empty. | [optional] 

## Example

```python
from touroptimizer_py_client.models.database_encrypted_item_search import DatabaseEncryptedItemSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseEncryptedItemSearch from a JSON string
database_encrypted_item_search_instance = DatabaseEncryptedItemSearch.from_json(json)
# print the JSON string representation of the object
print DatabaseEncryptedItemSearch.to_json()

# convert the object into a dict
database_encrypted_item_search_dict = database_encrypted_item_search_instance.to_dict()
# create an instance of DatabaseEncryptedItemSearch from a dict
database_encrypted_item_search_form_dict = database_encrypted_item_search.from_dict(database_encrypted_item_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


