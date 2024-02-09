# WorkingHours

The list of non-overlapping workingHours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **datetime** | The begin of the Working hours. | 
**end** | **datetime** | The end of the Working hours. | 
**zone_id** | **str** | The zoneId of the Working hours. | 
**max_time** | **str** | The maximal time a Resource should work within the WorkingHour. | [optional] 
**max_distance** | **str** | The maximla distance a resource should cover within the WorkingHour. | [optional] 
**stay_out_cycle_definition** | [**StayOutCycleDefinition**](StayOutCycleDefinition.md) |  | [optional] 
**start_reduction_time_definition** | [**StartReductionTimeDefinition**](StartReductionTimeDefinition.md) |  | [optional] 
**start_reduction_time_pillar_definition** | [**StartReductionTimePillarDefinition**](StartReductionTimePillarDefinition.md) |  | [optional] 
**start_reduction_time_include_definition** | [**StartReductionTimeIncludeDefinition**](StartReductionTimeIncludeDefinition.md) |  | [optional] 
**local_flex_time** | **str** | The local flexible time. In some cases a Resource should start working later compared to what is defined in the working hours. This way idle time can be reduced. The local flex time is the maximum a Resource is allowed to start working later, depending on the Optimization maybe flex time is not or only partially used. | [optional] 
**local_post_flex_time** | **str** | The localPostFlexTime | [optional] 
**local_post_flex_time_only_on_overtime** | **bool** | The post flextime is only applied to reduce overtime. | [optional] [default to False]
**max_local_pillar_after_hours_time** | **str** | The maxLocalPillarAfterHoursTime | [optional] 
**node_color_capacities** | [**List[NodeColorCapacity]**](NodeColorCapacity.md) | The nodeColorCapacities | [optional] 
**working_hours_constraints** | [**List[Constraint]**](Constraint.md) | The constraints for this working hour. | [optional] 
**multi_working_hours_constraints** | [**List[Constraint]**](Constraint.md) | The multiWorkingHoursConstraints | [optional] 
**qualifications** | [**List[Qualification]**](Qualification.md) | The qualification of the Resource for this working hour. For example, the Resource is allowed to visit a node needing a skill (defined via a constraint) and the Resource is providing this skill. | [optional] 
**route_start_time_hook** | **str** | The routeStartTimeHook | [optional] 
**hook_element_connections** | [**List[ReducedNodeEdgeConnectorItem]**](ReducedNodeEdgeConnectorItem.md) | The list of hook connections | [optional] 
**is_available_for_stay** | **bool** | The boolean isAvailableForStay defines if this working hour is allowed to end at an overnight stay. | [optional] [default to True]
**is_closed_route** | **bool** | The isClosedRoute boolean describes if a Resource has to visit the termination element of the Route. By default, the start element and the termination element of a Route is the Resource itself. In case of a closed route, by default, the Resource returns to its original starting location. | [optional] [default to True]

## Example

```python
from touroptimizer_py_client.models.working_hours import WorkingHours

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingHours from a JSON string
working_hours_instance = WorkingHours.from_json(json)
# print the JSON string representation of the object
print WorkingHours.to_json()

# convert the object into a dict
working_hours_dict = working_hours_instance.to_dict()
# create an instance of WorkingHours from a dict
working_hours_form_dict = working_hours.from_dict(working_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


