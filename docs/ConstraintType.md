# ConstraintType

A node-level constraint that restricts which resources may visit a node, or penalizes undesirable assignments. Subtypes include binding/excluding resource constraints, type-based skill matching (with optional expertise levels and cost models), zone number and UK post code territory constraints, magneto (node-to-node attraction/repulsion) constraints, and multi-route node color constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.constraint_type import ConstraintType

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintType from a JSON string
constraint_type_instance = ConstraintType.from_json(json)
# print the JSON string representation of the object
print(ConstraintType.to_json())

# convert the object into a dict
constraint_type_dict = constraint_type_instance.to_dict()
# create an instance of ConstraintType from a dict
constraint_type_from_dict = ConstraintType.from_dict(constraint_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


