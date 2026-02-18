# TypeLevelRequirement

The mapping of a certain type. or multiple types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | The expertise level | 
**is_min** | **bool** | The boolean isMin. If isMin&#x3D;&#x3D;true, the level is a minimal level that needs to be fulfilled. | 

## Example

```python
from touroptimizer_py_client.models.type_level_requirement import TypeLevelRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of TypeLevelRequirement from a JSON string
type_level_requirement_instance = TypeLevelRequirement.from_json(json)
# print the JSON string representation of the object
print(TypeLevelRequirement.to_json())

# convert the object into a dict
type_level_requirement_dict = type_level_requirement_instance.to_dict()
# create an instance of TypeLevelRequirement from a dict
type_level_requirement_from_dict = TypeLevelRequirement.from_dict(type_level_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


