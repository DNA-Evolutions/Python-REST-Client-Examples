# WorkingHours

A time window during which a resource is available for work. Defined by a begin and end instant with a time zone. Supports maximum working time and distance constraints, overtime/overdistance allowances, start-reduction-time (flex-time) policies, stay-out (overnight) definitions, node color capacities, and optional qualifications and depot configurations per working-hour window.

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
**local_post_flex_time** | **str** | The maximum duration by which the resource is allowed to end work earlier than the working-hour boundary. Acts as a flexible end-of-shift buffer — if the last node finishes ahead of schedule, the resource may clock off early by up to this amount, reducing unnecessary idle time at the end of the route. See also localPostFlexTimeOnlyOnOvertime to restrict this behavior to overtime-reduction scenarios only. | [optional] 
**local_post_flex_time_only_on_overtime** | **bool** | The post flextime is only applied to reduce overtime. | [optional] [default to False]
**max_local_pillar_after_hours_time** | **str** | The maximum duration a pillar node is allowed to be served after the official working-hours end for this specific working-hour window. Enables late-shift mandatory stops (e.g. end-of-day depot return) that extend slightly beyond the defined working-hour boundary. | [optional] 
**node_color_capacities** | [**List[NodeColorCapacity]**](NodeColorCapacity.md) | Per-color capacity limits for routes produced from this working hour. Controls the composition of the route by limiting how many nodes of a given color category may appear (e.g. at most 40% hazardous-goods stops). Overrides any resource-level color capacity when set at the working-hour level. | [optional] 
**working_hours_constraints** | [**List[Constraint]**](Constraint.md) | The constraints for this working hour. | [optional] 
**multi_working_hours_constraints** | [**List[Constraint]**](Constraint.md) | Constraints that span across multiple working hours of the same resource. Unlike workingHoursConstraints (which apply to a single working-hour window), these constraints enforce policies across the full planning horizon — for example, limiting the total number of a certain node type visited across all days. | [optional] 
**construction_hooks** | [**List[ConstructionHook]**](ConstructionHook.md) | The hooks for this working hour. | [optional] 
**qualifications** | [**List[Qualification]**](Qualification.md) | The qualification of the Resource for this working hour. For example, the Resource is allowed to visit a node needing a skill (defined via a constraint) and the Resource is providing this skill. | [optional] 
**route_start_time_hook** | **str** | An optional time offset applied to the route start. Shifts the effective departure time from the resource&#39;s home location, for example to account for vehicle preparation, warm-up, or loading time before the first stop. | [optional] 
**hook_element_connections** | [**List[ReducedNodeEdgeConnectorItem]**](ReducedNodeEdgeConnectorItem.md) | Pre-computed connections used exclusively during the construction hook phase. These connections override the default element connections for hook-related routing decisions, allowing special distance/time calculations during construction (e.g. depot-to-first-stop distances that differ from normal driving). | [optional] 
**is_local_service_hub** | **bool** | If true, this resource operates in service-hub mode during this working hour: instead of the resource traveling to visit nodes, nodes are conceptually &#39;brought to&#39; the resource&#39;s location. Useful for modeling stationary service points, reception desks, or warehouse processing stations. | [optional] [default to False]
**is_closed_route** | **bool** | The isClosedRoute boolean describes if a Resource has to visit the termination element of the Route. By default, the start element and the termination element of a Route is the Resource itself. In case of a closed route, by default, the Resource returns to its original starting location. | [optional] [default to True]
**is_available_for_stay** | **bool** | The boolean isAvailableForStay defines if this working hour is allowed to end at an overnight stay. | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.working_hours import WorkingHours

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingHours from a JSON string
working_hours_instance = WorkingHours.from_json(json)
# print the JSON string representation of the object
print(WorkingHours.to_json())

# convert the object into a dict
working_hours_dict = working_hours_instance.to_dict()
# create an instance of WorkingHours from a dict
working_hours_from_dict = WorkingHours.from_dict(working_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


