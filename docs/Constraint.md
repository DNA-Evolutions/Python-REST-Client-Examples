# Constraint

The constraints  of the Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConstraintType**](ConstraintType.md) |  | 
**is_hard** | **bool** | Defines if a constraint is soft contrained or hard constraint. A hard constraint is fullfilled by the architectural design of the Optimzer. Therefore a hard constraint violation cannot occure. However, not all constraints can be hard-constraint- | 

## Example

```python
from touroptimizer_py_client.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print Constraint.to_json()

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_form_dict = constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


