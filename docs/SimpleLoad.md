# SimpleLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_id** | **str** |  | [optional] 
**is_request** | **bool** |  | [optional] 
**is_fuzzy_visit** | **bool** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'SimpleLoad']

## Example

```python
from touroptimizer_py_client.models.simple_load import SimpleLoad

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleLoad from a JSON string
simple_load_instance = SimpleLoad.from_json(json)
# print the JSON string representation of the object
print SimpleLoad.to_json()

# convert the object into a dict
simple_load_dict = simple_load_instance.to_dict()
# create an instance of SimpleLoad from a dict
simple_load_form_dict = simple_load.from_dict(simple_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


