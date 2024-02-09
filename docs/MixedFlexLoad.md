# MixedFlexLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_id** | **str** |  | [optional] 
**is_request** | **bool** |  | [optional] 
**is_fuzzy_visit** | **bool** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'MixedFlexLoad']

## Example

```python
from touroptimizer_py_client.models.mixed_flex_load import MixedFlexLoad

# TODO update the JSON string below
json = "{}"
# create an instance of MixedFlexLoad from a JSON string
mixed_flex_load_instance = MixedFlexLoad.from_json(json)
# print the JSON string representation of the object
print MixedFlexLoad.to_json()

# convert the object into a dict
mixed_flex_load_dict = mixed_flex_load_instance.to_dict()
# create an instance of MixedFlexLoad from a dict
mixed_flex_load_form_dict = mixed_flex_load.from_dict(mixed_flex_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


