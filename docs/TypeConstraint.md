# TypeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_names** | **List[str]** | A list of user-provided type-names. A Contraint type name must match to a Qualification type name to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'Type']

## Example

```python
from touroptimizer_py_client.models.type_constraint import TypeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of TypeConstraint from a JSON string
type_constraint_instance = TypeConstraint.from_json(json)
# print the JSON string representation of the object
print TypeConstraint.to_json()

# convert the object into a dict
type_constraint_dict = type_constraint_instance.to_dict()
# create an instance of TypeConstraint from a dict
type_constraint_form_dict = type_constraint.from_dict(type_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


