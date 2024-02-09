# IdleEventNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pillar_node** | [**EventPillarNode**](EventPillarNode.md) |  | [optional] 
**master_id** | **str** | The masterId | [optional] 
**related_id** | **str** | The relatedId | [optional] 
**creation_time_stamp** | **int** | The creationTimeStamp | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'IdleEvent']

## Example

```python
from touroptimizer_py_client.models.idle_event_node import IdleEventNode

# TODO update the JSON string below
json = "{}"
# create an instance of IdleEventNode from a JSON string
idle_event_node_instance = IdleEventNode.from_json(json)
# print the JSON string representation of the object
print IdleEventNode.to_json()

# convert the object into a dict
idle_event_node_dict = idle_event_node_instance.to_dict()
# create an instance of IdleEventNode from a dict
idle_event_node_form_dict = idle_event_node.from_dict(idle_event_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


