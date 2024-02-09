# Resource

The list of resoruces

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
**stay_out_policy_time** | **str** | The stayOutPolicyTime | [optional] 
**stay_out_policy_distance** | **str** | The stayOutPolicyDistance | [optional] 
**capacity** | **List[float]** | The capacity | [optional] 
**initial_load** | **List[float]** | The initialLoad | [optional] 
**min_degrated_capacity** | **List[float]** | The minDegratedCapacity | [optional] 
**capacity_deg_per_stop** | **List[float]** | The capacityDegPerStop | [optional] 
**start_reduction_time_definition** | [**StartReductionTimeDefinition**](StartReductionTimeDefinition.md) |  | [optional] 
**start_reduction_time_pillar_definition** | [**StartReductionTimePillarDefinition**](StartReductionTimePillarDefinition.md) |  | [optional] 
**start_reduction_time_include_definition** | [**StartReductionTimeIncludeDefinition**](StartReductionTimeIncludeDefinition.md) |  | [optional] 
**flex_time** | **str** | The local flexible time. In some cases a Resource should start working later compared to what is defined in the working hours. This way idle time can be reduced. The local flex time is the maximum a Resource is allowed to start working later, depending on the Optimization maybe flex time is not or only partially used. | [optional] 
**post_flex_time** | **str** | The postFlexTime | [optional] 
**post_flex_time_only_on_overtime** | **bool** | The post flextime is only applied to reduce overtime. | [optional] [default to False]
**max_pillar_after_hours_time** | **str** | The maxPillarAfterHoursTime | [optional] 
**max_drive_time_first_node** | **str** | The maxDriveTimeFirstNode | [optional] 
**max_drive_distance_first_node** | **str** | The maxDriveDistanceFirstNode | [optional] 
**max_drive_time_last_node** | **str** | The maxDriveTimeLastNode | [optional] 
**max_drive_distance_last_node** | **str** | The maxDriveDistanceLastNode | [optional] 
**kilometer_cost** | **float** | The kilometerCost defines how much arbitrary cost arises per kilometer driven. | [optional] 
**hour_cost** | **float** | The hourCost defines how much arbitrary cost arises per hour scheduled (idling, working, driving). | [optional] 
**production_hour_cost** | **float** | The productionHourCost defines how much arbitrary cost arises per hour working. | [optional] 
**fix_cost** | **float** | The fixCost defines an abstract cost that arrises when this node is visited. | [optional] 
**pre_work_driving_time** | **str** | The preWorkDrivingTime.  Use startReductionTimeDefinition instead. | [optional] 
**skill_efficiency_factor** | **float** | The skillEfficiencyFactor | [optional] 
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
**is_reduction_time_included_in_total_working_time** | **bool** | The isReductionTimeIncludedInTotalWorkingTime. Use StartReductionTimeIncludeDefinition instead | [optional] [default to False]
**is_reduction_time_only_used_for_driving** | **bool** | The isReductionTimeOnlyUsedForDriving. Use startReductionTimeDefinition instead. | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print Resource.to_json()

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_form_dict = resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


