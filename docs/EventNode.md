# EventNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pillar_node** | [**EventPillarNode**](EventPillarNode.md) |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'Event']
**is_partial_exchange_idle_for_driving_time** | **bool** | An EventNode is allowed to be visited BEWTWEEN two Nodes and does not need to be positioned at a node. | [optional] [default to True]

## Example

```python
from touroptimizer_py_client.models.event_node import EventNode

# TODO update the JSON string below
json = "{}"
# create an instance of EventNode from a JSON string
event_node_instance = EventNode.from_json(json)
# print the JSON string representation of the object
print EventNode.to_json()

# convert the object into a dict
event_node_dict = event_node_instance.to_dict()
# create an instance of EventNode from a dict
event_node_form_dict = event_node.from_dict(event_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


