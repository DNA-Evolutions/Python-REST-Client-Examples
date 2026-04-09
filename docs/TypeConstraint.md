# TypeConstraint

A string-based skill constraint on a node. The node requires resources whose TypeQualification includes at least one matching type name. Unmatched assignments produce violations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_names** | **List[str]** | A list of user-provided type-names. A Constraint type name must match to a Qualification type name to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'Type']

## Example

```python
from touroptimizer_py_client.models.type_constraint import TypeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of TypeConstraint from a JSON string
type_constraint_instance = TypeConstraint.from_json(json)
# print the JSON string representation of the object
print(TypeConstraint.to_json())

# convert the object into a dict
type_constraint_dict = type_constraint_instance.to_dict()
# create an instance of TypeConstraint from a dict
type_constraint_from_dict = TypeConstraint.from_dict(type_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


