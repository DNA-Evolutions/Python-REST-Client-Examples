# RouteElementDetail

The elementDetails. The list of details describing the route schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_id** | **str** | The elementId that the detail item belongs to. | 
**start_time** | **datetime** | The startTime defines the time when a vistior (Resource) starts serving a node. | 
**arrival_time** | **datetime** | The arrivalTime defines the time when a vistior (Resource) arrives at a node. It is possible that a Visitior needs to idle at the node until a node opens. | 
**departure_time** | **datetime** | The departureTime defines the time a resource is leaving a node. | 
**transition_time** | **str** | The transitionTime gives the time taken for the connection from the previous element to this element. | 
**effective_position** | [**Position**](Position.md) |  | [optional] 
**idle_time** | **str** | The idleTime is the time the Visitor has to wait until a node can be served. By default idle time arrises at the node to be visited. For example, a the arrival time of a Visitor is at 7 in the morning but the node opens at 8. The Visitor has to wait for one hour at the node location until the node can be served. | 
**zone_id** | **str** | The zoneId of detail | 
**white_space_idle_time** | **str** | The whiteSpaceIdleTime only occurs if the Visitor is using a different reduction time definition for normal nodes and PillarNodes. It is usually introduced to avoid a violation where Pillars are allowed to be served before workingTime and Nodes are not. | [optional] 
**duration_time** | **str** | The durationTime defines how long a node is serverd by a Visitor. | 
**transition_distance** | **str** | The transitionDistance gives the distance taken for the connection from the previous element to this element. | 
**choosen_working_hours_index** | **int** | Each visitor can have a list of workingHours. The choosenWorkingHoursIndex is the index of the Visitors workingHour in which the element is visited. | [optional] 
**early_deviation** | **str** | The earlyDeviation. The early deviation describes how long before the element opens the Visitor arrives. If the value is negative, the Vistor arrives after the element already opens. | [optional] 
**late_deviation** | **str** | The lateDeviation. The late deviation describes how much lateness the Vistor has. For example, the element to be visited is open from 8-11 and the desired visit duration is 2 hours. The Visitor has to arrive latest by 9 to finish the Job until 11. If the Visitor arrives at 10 the late deviation will be one hour, as the Visitor needs till 12 to finish the Job. The late deviation can be also negative indicating not beeing late. For example if the Visitor reaches the element by 8 and finishes the Job by 10 and the element closes at 11 the late deviation will be -1 hour. | [optional] 
**schedule_status** | **str** | The scheduleStatus. | [optional] 
**visitor_id** | **str** | The visitorId. The id of the Visitor serving the element. | [optional] 
**load_change** | **List[float]** | LEGACY: The change of the load of the element caused by the Visitor. For example, when the element requested 2 items and the Visitor provided only 1 item the loadChange value would be 1. | [optional] 
**cur_capacity** | **List[float]** | LEGACY: The curCapacity of the visitor after visiting the element. | [optional] 
**before_visit_node_depot** | [**INodeDepot**](INodeDepot.md) |  | [optional] 
**after_visit_node_depot** | [**INodeDepot**](INodeDepot.md) |  | [optional] 
**node_violations** | [**List[Violation]**](Violation.md) | The nodeViolations. The violations collected at the element/node. For example, lateViolation, early violation etc. | [optional] 
**is_unlocated_idle_time** | **bool** | The isUnlocatedIdleTime changes the representation of the idle time in the solution. By default idle time is located at the node to be waited for. If true, the idle time becomes unlocated. For example, a Visitor can reach a node (that opens at 8) by 7 in the morning. If the idle time is unlocated, the arrival time  will be represented as 8 (instead of 7).  | [optional] 

## Example

```python
from touroptimizer_py_client.models.route_element_detail import RouteElementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RouteElementDetail from a JSON string
route_element_detail_instance = RouteElementDetail.from_json(json)
# print the JSON string representation of the object
print RouteElementDetail.to_json()

# convert the object into a dict
route_element_detail_dict = route_element_detail_instance.to_dict()
# create an instance of RouteElementDetail from a dict
route_element_detail_form_dict = route_element_detail.from_dict(route_element_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


