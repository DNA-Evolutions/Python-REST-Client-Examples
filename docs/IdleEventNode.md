# IdleEventNode

A system-generated non-geographical node that represents idle time or a synthetic event inserted by the optimizer during construction or heuristic phases. This node type is never created by the user — it is produced internally to model waiting periods, return-to-start segments, or inter-route padding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pillar_node** | [**PillarType**](PillarType.md) |  | [optional] 
**master_id** | **str** | The id of the master node that triggered the creation of this idle event (e.g. in relation-based or return-to-start scenarios). | [optional] 
**related_id** | **str** | The id of the related node associated with this idle event (e.g. the node the resource is waiting for). | [optional] 
**creation_time_stamp** | **int** | The epoch-millisecond timestamp when this idle event node was created by the optimizer. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'IdleEvent']

## Example

```python
from touroptimizer_py_client.models.idle_event_node import IdleEventNode

# TODO update the JSON string below
json = "{}"
# create an instance of IdleEventNode from a JSON string
idle_event_node_instance = IdleEventNode.from_json(json)
# print the JSON string representation of the object
print(IdleEventNode.to_json())

# convert the object into a dict
idle_event_node_dict = idle_event_node_instance.to_dict()
# create an instance of IdleEventNode from a dict
idle_event_node_from_dict = IdleEventNode.from_dict(idle_event_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


