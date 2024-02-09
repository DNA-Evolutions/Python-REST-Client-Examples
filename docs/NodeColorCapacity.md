# NodeColorCapacity

The nodeColorCapacities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_color** | [**NodeColor**](NodeColor.md) |  | 
**max_usage** | **float** | The maxUsage of the NodeColorCapacity | 

## Example

```python
from touroptimizer_py_client.models.node_color_capacity import NodeColorCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of NodeColorCapacity from a JSON string
node_color_capacity_instance = NodeColorCapacity.from_json(json)
# print the JSON string representation of the object
print NodeColorCapacity.to_json()

# convert the object into a dict
node_color_capacity_dict = node_color_capacity_instance.to_dict()
# create an instance of NodeColorCapacity from a dict
node_color_capacity_form_dict = node_color_capacity.from_dict(node_color_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


