# EventPillarNode

The pillarNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_resource_id** | **str** | The attached resourceId. A geoPillar must be visited by this resource. | [optional] 
**only_scheduled_in_company** | **bool** | The onlyScheduledInCompany | [optional] 
**is_extendable_end** | **bool** | The isExtendableEnd | [optional] 
**is_schedulable_after_working_hours** | **bool** | The isSchedulableAfterWorkingHours | [optional] 
**is_overwriting_route_termination** | **bool** | The boolean isOverwritingRouteTermination. Instead of using the default termination element of the route, the geoPillar will be used as so-called endAnchor. | [optional] 
**is_time_adjustable_anchor** | **bool** | The isTimeAdjustableAnchor | [optional] 
**is_schedulable_before_working_hours** | **bool** | The isSchedulableBeforeWorkingHours | [optional] 

## Example

```python
from touroptimizer_py_client.models.event_pillar_node import EventPillarNode

# TODO update the JSON string below
json = "{}"
# create an instance of EventPillarNode from a JSON string
event_pillar_node_instance = EventPillarNode.from_json(json)
# print the JSON string representation of the object
print EventPillarNode.to_json()

# convert the object into a dict
event_pillar_node_dict = event_pillar_node_instance.to_dict()
# create an instance of EventPillarNode from a dict
event_pillar_node_form_dict = event_pillar_node.from_dict(event_pillar_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


