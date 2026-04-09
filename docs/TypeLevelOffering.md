# TypeLevelOffering

Specifies the expertise level a resource offers for a given skill type. Matched against TypeLevelRequirement on the node side to determine constraint satisfaction and cost penalties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | The expertise level | 

## Example

```python
from touroptimizer_py_client.models.type_level_offering import TypeLevelOffering

# TODO update the JSON string below
json = "{}"
# create an instance of TypeLevelOffering from a JSON string
type_level_offering_instance = TypeLevelOffering.from_json(json)
# print the JSON string representation of the object
print(TypeLevelOffering.to_json())

# convert the object into a dict
type_level_offering_dict = type_level_offering_instance.to_dict()
# create an instance of TypeLevelOffering from a dict
type_level_offering_from_dict = TypeLevelOffering.from_dict(type_level_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


