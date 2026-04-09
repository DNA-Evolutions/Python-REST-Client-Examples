# Resource

A mobile agent (vehicle, driver, technician) available to visit nodes. Defines a home position, one or more working-hour windows with time/distance constraints, optional qualifications (skills), an optional resource depot for pickup-and-delivery, connection efficiency factors, overnight-stay policies, and route configuration (open/closed, alternate destination, return-to-start).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the Resource. It is not possible, to create mutliple elements (also Nodes) with the same id. | 
**extra_info** | **str** | A custom extra info string that is attached to the Resource. | [optional] 
**location_id** | **str** | The location id can relate a Resouce to the connection of another resource. See also locationId of Node. | [optional] 
**constraint_alias_id** | **str** | The constraintAliasId. If set is used during constraint assessment instead of using the normal id. | [optional] 
**type** | [**ResourceType**](ResourceType.md) |  | 
**position** | [**Position**](Position.md) |  | 
**working_hours** | [**List[WorkingHours]**](WorkingHours.md) | The list of non-overlapping workingHours. | 
**max_time** | **str** | The maxTime. The maximal time a Resource should work within the WorkingHour. This value is NOT logically coupled to the workingHours. For example, a working hour is defined from 8 in the morning till  5 in the afternoon and the maxTime is defined as 4 hours. In this situation an overime violation will be already  generated  when the Resource works from 8 till 1 (one hour of overtime). As JOpt supports flexible start times, the Resource might work from 12-4 (4 hours &#x3D;&gt; not violation). The workingHour itself should be seen as a frame that is used primarily for matching WokingHours of Resources and OpeningHours of nodes. If no flexTime is used, the Resource will always start working at the beginning of its current working hours. | 
**max_distance** | **str** | The maxDistance. The maximal distance a Resource is allowed to drive within a certain working hours. | 
**destination_position** | [**Position**](Position.md) |  | [optional] 
**stay_out_definition** | [**StayOutDefinition**](StayOutDefinition.md) |  | [optional] 
**stay_out_cycle_definition** | [**StayOutCycleDefinition**](StayOutCycleDefinition.md) |  | [optional] 
**stay_out_policy_time** | **str** | The maximum additional working time a resource is allowed to accumulate during an overnight-stay route beyond its normal working-hour boundaries. Acts as a buffer for late arrivals at stay nodes. | [optional] 
**stay_out_policy_distance** | **str** | The maximum additional driving distance a resource is allowed to accumulate during an overnight-stay route beyond its normal per-working-hour distance limit. Prevents the resource from driving excessively far to reach a stay node. | [optional] 
**capacity** | **List[float]** | The multi-dimensional capacity vector of the resource (e.g. weight in kg, volume in m³, number of pallets). Each element represents the maximum capacity for one dimension. Used in pickup-and-delivery (PND) scenarios to enforce load constraints. The index positions must align with the load dimensions defined on the nodes. | [optional] 
**initial_load** | **List[float]** | The initial load the resource carries at the start of each route, per capacity dimension. For delivery scenarios, this represents the pre-loaded goods at the depot. For pickup scenarios, this is typically zero. Must have the same dimensionality as the capacity vector. | [optional] 
**min_degrated_capacity** | **List[float]** | The minimum degraded capacity per dimension. As the resource visits more stops, its effective capacity may degrade (e.g. due to fatigue, compartment loss, or reorganization overhead). This vector defines the floor below which the capacity cannot degrade, regardless of the number of stops visited. | [optional] 
**capacity_deg_per_stop** | **List[float]** | The capacity degradation per stop, per dimension. After each node visit, the resource&#39;s effective capacity is reduced by this amount (down to the minDegratedCapacity floor). Models real-world effects such as compartment unavailability after partial unloading or diminishing usable space. | [optional] 
**start_reduction_time_definition** | [**StartReductionTimeDefinition**](StartReductionTimeDefinition.md) |  | [optional] 
**start_reduction_time_pillar_definition** | [**StartReductionTimePillarDefinition**](StartReductionTimePillarDefinition.md) |  | [optional] 
**start_reduction_time_include_definition** | [**StartReductionTimeIncludeDefinition**](StartReductionTimeIncludeDefinition.md) |  | [optional] 
**flex_time** | **str** | The local flexible time. In some cases a Resource should start working later compared to what is defined in the working hours. This way idle time can be reduced. The local flex time is the maximum a Resource is allowed to start working later, depending on the Optimization maybe flex time is not or only partially used. | [optional] 
**post_flex_time** | **str** | The maximum duration by which the resource is allowed to end its working day earlier than the working-hour boundary. Reduces unnecessary idle time at the end of a route. See also postFlexTimeOnlyOnOvertime to restrict usage to overtime-reduction scenarios. | [optional] 
**post_flex_time_only_on_overtime** | **bool** | The post flextime is only applied to reduce overtime. | [optional] [default to False]
**max_pillar_after_hours_time** | **str** | The maximum duration a pillar node may be served after the resource&#39;s official working-hours end. Applies globally across all working hours of this resource. For per-working-hour overrides, use maxLocalPillarAfterHoursTime on the individual WorkingHours object. | [optional] 
**max_drive_time_first_node** | **str** | The maximum driving time allowed from the resource&#39;s start position to the first node of a route. Prevents the optimizer from assigning a distant first stop that would consume excessive travel time before productive work begins. | [optional] 
**max_drive_distance_first_node** | **str** | The maximum driving distance allowed from the resource&#39;s start position to the first node of a route. Complements maxDriveTimeFirstNode to enforce both time- and distance-based proximity constraints. | [optional] 
**max_drive_time_last_node** | **str** | The maximum driving time allowed from the last visited node to the route termination element (typically the resource&#39;s home position or alternate destination). Prevents the optimizer from placing a final stop that would require an excessively long return journey. | [optional] 
**max_drive_distance_last_node** | **str** | The maximum driving distance allowed from the last visited node to the route termination element. Complements maxDriveTimeLastNode to enforce both time- and distance-based return constraints. | [optional] 
**kilometer_cost** | **float** | The kilometerCost defines how much arbitrary cost arises per kilometer driven. | [optional] 
**hour_cost** | **float** | The hourCost defines how much arbitrary cost arises per hour scheduled (idling, working, driving). | [optional] 
**production_hour_cost** | **float** | The productionHourCost defines how much arbitrary cost arises per hour working. | [optional] 
**fix_cost** | **float** | The fixCost defines an abstract cost that arrises when this node is visited. | [optional] 
**pre_work_driving_time** | **str** | DEPRECATED. Use startReductionTimeDefinition instead. Legacy field that defined how long before the official working-hour start the resource was allowed to drive. | [optional] 
**skill_efficiency_factor** | **float** | DEPRECATED. Use the visitDurationEfficiency mechanism on individual nodes and ResourceVisitDurationEfficiency instead. Legacy factor that scaled visit durations for this resource. | [optional] 
**acceptable_overtime** | **str** | The acceptableOvertime. By default if nodes are constantly leading to overtime for a resource, at some point they might get unassigned (if AutoFilter is activated). The acceptable overtime assigns a margin to avoid filtering nodes if they lead to overtime below this margin. By defaul the property  &#39;JoptAutoFilterWorkingHoursExceedMargin&#39; can be used to globally define this value. | [optional] 
**strict_overtime** | **str** | The strictOvertime. By default if nodes are constantly leading to overtime for a resource, at some point they might get unassigned (if AutoFilter is activated). The strictOvertime overtime assigns a margin to avoid filtering nodes if they lead to overtime below this margin. By defaul the property  &#39;JoptAutoFilterWorkingHoursStrictExceedMargin&#39; can be used to globally define this value. In contrast to acceptable  overtime, the strict overtime is used during the last fitlering step of the AutoFilter (if strict mode is enabled). | [optional] 
**acceptable_overdistance** | **str** | The acceptableOverdistance. Like acceptableOvertime for distance. | [optional] 
**strict_overdistance** | **str** | The strictOverdistance. Like strictOvertime for distance. | [optional] 
**average_speed** | **float** | The averageSpeed of the Resource. By default this value is set to be 22[m/s] (79.2[km/h]). This value is mainly used, in case no external node connections are provided. | [optional] 
**qualifications** | [**List[Qualification]**](Qualification.md) | The qualifications of the Resource. | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) | The constraints  of the Resource | [optional] 
**connection_time_efficiency_factor** | **float** | The connectionTimeEfficiencyFactor. The default time for passing a connection is devided by this factor. For example, if a connections needs 30 minutes to be passed by default, a Resource with a connectionTimeEfficiencyFactor of 1.5 only needs 20 minutes. By default this factor is one. | [optional] [default to 1.0]
**co2emission_factor** | **float** | The co2emissionFactor. | [optional] 
**resource_depot** | [**IResourceDepot**](IResourceDepot.md) |  | [optional] 
**overall_visit_duration_efficiency** | **float** | The overallVisitDurationEfficiency. The base duration a Resource spends at a node is devided by this factor. For example, if a node has 30 minutes of visit duration assigned, a Resource with a overallVisitDurationEfficiency of 1.5 only needs 20 minutes. By default this factor is one. | [optional] [default to 1.0]
**is_reduction_time_included_in_total_working_time** | **bool** | DEPRECATED. Use StartReductionTimeIncludeDefinition instead. Legacy flag that controlled whether reduction time was counted toward the resource&#39;s total working time. | [optional] [default to False]
**is_reduction_time_only_used_for_driving** | **bool** | DEPRECATED. Use startReductionTimeDefinition instead. Legacy flag that restricted reduction time to driving only (no working at the first node before the shift starts). | [optional] [default to False]
**is_service_hub** | **bool** | A resource is hub mode gets visited by nodes. | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


