# BindingResourceConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ResourceWithPriority]**](ResourceWithPriority.md) | The resources that can be choosen to visit a certain node. | 
**type_name** | **str** | The typeName of the object | [default to 'BindingResource']

## Example

```python
from touroptimizer_py_client.models.binding_resource_constraint import BindingResourceConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BindingResourceConstraint from a JSON string
binding_resource_constraint_instance = BindingResourceConstraint.from_json(json)
# print the JSON string representation of the object
print BindingResourceConstraint.to_json()

# convert the object into a dict
binding_resource_constraint_dict = binding_resource_constraint_instance.to_dict()
# create an instance of BindingResourceConstraint from a dict
binding_resource_constraint_form_dict = binding_resource_constraint.from_dict(binding_resource_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


