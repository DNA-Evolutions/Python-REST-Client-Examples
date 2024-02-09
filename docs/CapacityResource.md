# CapacityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The typeName of the object | [default to 'Capacity']

## Example

```python
from touroptimizer_py_client.models.capacity_resource import CapacityResource

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityResource from a JSON string
capacity_resource_instance = CapacityResource.from_json(json)
# print the JSON string representation of the object
print CapacityResource.to_json()

# convert the object into a dict
capacity_resource_dict = capacity_resource_instance.to_dict()
# create an instance of CapacityResource from a dict
capacity_resource_form_dict = capacity_resource.from_dict(capacity_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


