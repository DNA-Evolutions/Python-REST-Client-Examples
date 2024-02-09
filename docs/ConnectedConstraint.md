# ConnectedConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_one** | [**Constraint**](Constraint.md) |  | 
**constraint_two** | [**Constraint**](Constraint.md) |  | 
**connection_type** | **str** | The connectionType | 
**type_name** | **str** | The typeName of the object | [default to 'ConnectedConstraint']

## Example

```python
from touroptimizer_py_client.models.connected_constraint import ConnectedConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedConstraint from a JSON string
connected_constraint_instance = ConnectedConstraint.from_json(json)
# print the JSON string representation of the object
print ConnectedConstraint.to_json()

# convert the object into a dict
connected_constraint_dict = connected_constraint_instance.to_dict()
# create an instance of ConnectedConstraint from a dict
connected_constraint_form_dict = connected_constraint.from_dict(connected_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


