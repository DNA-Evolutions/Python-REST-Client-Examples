# ResourceLocationConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_radius_distance** | **str** | The maxRadiusDistance | [optional] 
**max_radius_time** | **str** | The maxRadiusTime | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'ResourceLocationConstraint']

## Example

```python
from touroptimizer_py_client.models.resource_location_constraint import ResourceLocationConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLocationConstraint from a JSON string
resource_location_constraint_instance = ResourceLocationConstraint.from_json(json)
# print the JSON string representation of the object
print ResourceLocationConstraint.to_json()

# convert the object into a dict
resource_location_constraint_dict = resource_location_constraint_instance.to_dict()
# create an instance of ResourceLocationConstraint from a dict
resource_location_constraint_form_dict = resource_location_constraint.from_dict(resource_location_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


