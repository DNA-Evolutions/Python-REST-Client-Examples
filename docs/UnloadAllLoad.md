# UnloadAllLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_id** | **str** |  | [optional] 
**is_request** | **bool** |  | [optional] 
**is_fuzzy_visit** | **bool** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'UnloadAllLoad']

## Example

```python
from touroptimizer_py_client.models.unload_all_load import UnloadAllLoad

# TODO update the JSON string below
json = "{}"
# create an instance of UnloadAllLoad from a JSON string
unload_all_load_instance = UnloadAllLoad.from_json(json)
# print the JSON string representation of the object
print UnloadAllLoad.to_json()

# convert the object into a dict
unload_all_load_dict = unload_all_load_instance.to_dict()
# create an instance of UnloadAllLoad from a dict
unload_all_load_form_dict = unload_all_load.from_dict(unload_all_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


