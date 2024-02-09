# AbsoluteNodeColorCapacity

The absoluteNodeColorCapacities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_color** | [**NodeColor**](NodeColor.md) |  | 
**min_usage** | **int** | The minUsage  of the AbsoluteNodeColorCapacity | 
**max_usage** | **int** | The maxUsage  of the AbsoluteNodeColorCapacity | 

## Example

```python
from touroptimizer_py_client.models.absolute_node_color_capacity import AbsoluteNodeColorCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of AbsoluteNodeColorCapacity from a JSON string
absolute_node_color_capacity_instance = AbsoluteNodeColorCapacity.from_json(json)
# print the JSON string representation of the object
print AbsoluteNodeColorCapacity.to_json()

# convert the object into a dict
absolute_node_color_capacity_dict = absolute_node_color_capacity_instance.to_dict()
# create an instance of AbsoluteNodeColorCapacity from a dict
absolute_node_color_capacity_form_dict = absolute_node_color_capacity.from_dict(absolute_node_color_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


