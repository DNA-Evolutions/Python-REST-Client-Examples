# TypeWithExpertiseConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types_with_expertise** | [**List[TypeWithExpertise]**](TypeWithExpertise.md) | The types with expertise | 
**cost_model** | **str** | The cost model for matching the expertise. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'TypeWithExpertise']

## Example

```python
from touroptimizer_py_client.models.type_with_expertise_constraint import TypeWithExpertiseConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of TypeWithExpertiseConstraint from a JSON string
type_with_expertise_constraint_instance = TypeWithExpertiseConstraint.from_json(json)
# print the JSON string representation of the object
print TypeWithExpertiseConstraint.to_json()

# convert the object into a dict
type_with_expertise_constraint_dict = type_with_expertise_constraint_instance.to_dict()
# create an instance of TypeWithExpertiseConstraint from a dict
type_with_expertise_constraint_form_dict = type_with_expertise_constraint.from_dict(type_with_expertise_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


