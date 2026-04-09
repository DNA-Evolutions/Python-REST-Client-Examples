# NodeColor

The color category assigned to this node. Used in conjunction with NodeColorCapacity or AbsoluteNodeColorCapacity constraints on the resource's working hours to control route composition (e.g. limit the number of hazardous-goods stops per route). Defaults to the system DEFAULT color.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_code** | **int** | A numeric color code identifying this color category. Must match the codes used in NodeColorCapacity constraints. | 
**color_id** | **str** | A human-readable identifier for this color category (e.g. &#39;HAZARDOUS&#39;, &#39;PRIORITY_A&#39;, &#39;COLD_CHAIN&#39;). | 
**count_value** | **int** | The contribution count of this node towards its color category. Defaults to 1. A higher value means this node &#39;consumes&#39; more of the route&#39;s color capacity budget. | [optional] 

## Example

```python
from touroptimizer_py_client.models.node_color import NodeColor

# TODO update the JSON string below
json = "{}"
# create an instance of NodeColor from a JSON string
node_color_instance = NodeColor.from_json(json)
# print the JSON string representation of the object
print(NodeColor.to_json())

# convert the object into a dict
node_color_dict = node_color_instance.to_dict()
# create an instance of NodeColor from a dict
node_color_from_dict = NodeColor.from_dict(node_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


