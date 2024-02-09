# ExcludingResourceConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ResourceWithPriority]**](ResourceWithPriority.md) | The list of resources that should NOT visit a certain node. | 
**type_name** | **str** | The typeName of the object | [default to 'ExcludingResource']

## Example

```python
from touroptimizer_py_client.models.excluding_resource_constraint import ExcludingResourceConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludingResourceConstraint from a JSON string
excluding_resource_constraint_instance = ExcludingResourceConstraint.from_json(json)
# print the JSON string representation of the object
print ExcludingResourceConstraint.to_json()

# convert the object into a dict
excluding_resource_constraint_dict = excluding_resource_constraint_instance.to_dict()
# create an instance of ExcludingResourceConstraint from a dict
excluding_resource_constraint_form_dict = excluding_resource_constraint.from_dict(excluding_resource_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


