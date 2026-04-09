# EventPillarNode

A non-geographic pillar node representing a time-based task (e.g. a meeting, phone call, or administrative block) locked to a specific resource. Like GeoPillarNode but without spatial coordinates — the optimizer schedules it based on time constraints only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_resource_id** | **str** | The attached resourceId. An event pillar must be visited by this specific resource. The optimizer guarantees architectural compliance — this is a hard constraint. | [optional] 
**only_scheduled_in_company** | **bool** | If true, this event pillar is only scheduled when the attached resource belongs to the same organizational group. Prevents cross-company assignments in multi-fleet scenarios. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'EventPillarNode']
**is_extendable_end** | **bool** | If true, the event pillar&#39;s end time can be extended beyond its defined opening-hour boundary to accommodate scheduling needs. Useful for flexible-duration events like meetings or calls. | [optional] 
**is_schedulable_after_working_hours** | **bool** | If true, the optimizer may schedule this event pillar after the resource&#39;s official working-hours end. Enables post-shift mandatory events (e.g. end-of-day reporting, handover calls). | [optional] 
**is_overwriting_route_termination** | **bool** | The boolean isOverwritingRouteTermination. Instead of using the default termination element of the route, the geoPillar will be used as so-called endAnchor. | [optional] 
**is_schedulable_before_working_hours** | **bool** | If true, the optimizer may schedule this event pillar before the resource&#39;s official working-hours start. Enables pre-shift mandatory events (e.g. morning briefings, pre-route phone calls). | [optional] 
**is_time_adjustable_anchor** | **bool** | If true, the anchor timing derived from this event pillar is allowed to shift within the working-hour boundaries. Enables the optimizer to adjust the schedule around fixed events while maintaining the pillar&#39;s role as a route anchor point. | [optional] 

## Example

```python
from touroptimizer_py_client.models.event_pillar_node import EventPillarNode

# TODO update the JSON string below
json = "{}"
# create an instance of EventPillarNode from a JSON string
event_pillar_node_instance = EventPillarNode.from_json(json)
# print the JSON string representation of the object
print(EventPillarNode.to_json())

# convert the object into a dict
event_pillar_node_dict = event_pillar_node_instance.to_dict()
# create an instance of EventPillarNode from a dict
event_pillar_node_from_dict = EventPillarNode.from_dict(event_pillar_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


