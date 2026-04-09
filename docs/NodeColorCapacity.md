# NodeColorCapacity

Per-color capacity limits for routes produced from this working hour. Controls the composition of the route by limiting how many nodes of a given color category may appear (e.g. at most 40% hazardous-goods stops). Overrides any resource-level color capacity when set at the working-hour level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_color** | [**NodeColor**](NodeColor.md) |  | 
**max_usage** | **float** | The maximum usage ratio (0.0–1.0) of this node color within a single route. For example, 0.5 means at most 50% of the nodes on a route may carry this color. | 

## Example

```python
from touroptimizer_py_client.models.node_color_capacity import NodeColorCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of NodeColorCapacity from a JSON string
node_color_capacity_instance = NodeColorCapacity.from_json(json)
# print the JSON string representation of the object
print(NodeColorCapacity.to_json())

# convert the object into a dict
node_color_capacity_dict = node_color_capacity_instance.to_dict()
# create an instance of NodeColorCapacity from a dict
node_color_capacity_from_dict = NodeColorCapacity.from_dict(node_color_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


