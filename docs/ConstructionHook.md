# ConstructionHook

The hooks for this working hour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**HookType**](HookType.md) |  | 

## Example

```python
from touroptimizer_py_client.models.construction_hook import ConstructionHook

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructionHook from a JSON string
construction_hook_instance = ConstructionHook.from_json(json)
# print the JSON string representation of the object
print(ConstructionHook.to_json())

# convert the object into a dict
construction_hook_dict = construction_hook_instance.to_dict()
# create an instance of ConstructionHook from a dict
construction_hook_from_dict = ConstructionHook.from_dict(construction_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


