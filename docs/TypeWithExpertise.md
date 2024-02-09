# TypeWithExpertise

A list of user-provided type-names and expertise levels. A Contraint type-name with its required expertise must be fulfill by the type-with-expertise Qualification to result in a violation free solution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type name that in addition requires a certain expertise level. | 
**level** | **float** | The expertise level | 
**is_min** | **bool** | The boolean isMin. If isMin&#x3D;&#x3D;true, the level is a minimal level that needs to be fulfilled. | 

## Example

```python
from touroptimizer_py_client.models.type_with_expertise import TypeWithExpertise

# TODO update the JSON string below
json = "{}"
# create an instance of TypeWithExpertise from a JSON string
type_with_expertise_instance = TypeWithExpertise.from_json(json)
# print the JSON string representation of the object
print TypeWithExpertise.to_json()

# convert the object into a dict
type_with_expertise_dict = type_with_expertise_instance.to_dict()
# create an instance of TypeWithExpertise from a dict
type_with_expertise_form_dict = type_with_expertise.from_dict(type_with_expertise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


