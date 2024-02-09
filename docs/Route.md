# Route

The routes of the solution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**RouteHeader**](RouteHeader.md) |  | [optional] 
**id** | **int** | The id is an optimizer provided number identifiying a route. | 
**resource_id** | **str** | The resourceId of the Visitor owning this route. | 
**route_trip** | [**RouteTrip**](RouteTrip.md) |  | [optional] 
**start_time** | **datetime** | The startTime of the route. This is usually the start of the workingHours of the Resource. However, when using flextime/reduction-time the starttime can be different from the working hours start. | 
**start_element_id** | **str** | The startElementId, is the element from where the route starts. By default, it is the Resource itself. | 
**start_position** | [**Position**](Position.md) |  | [optional] 
**end_element_id** | **str** | The endElementId, is the element where the route stops. By default, it is the Resource itself. | 
**end_position** | [**Position**](Position.md) |  | [optional] 
**optimizable_element_ids** | **List[str]** | The optimizableElementIds. The list of optimizable elements that are part of the route. | 
**non_optimizable_element_ids** | **List[str]** | The nonOptimizableElementIds. The list of non-optimizable elements that are part of the route. | 
**optional_optimizable_element_ids** | **List[str]** | The optionalOptimizableElementIds. The list of optional elements that are part of the route. | 
**pillar_element_ids** | **List[str]** | The pillarElementIds. The list of pillar elements that are part of the route. | 
**element_details** | [**List[RouteElementDetail]**](RouteElementDetail.md) | The elementDetails. The list of details describing the route schedule. | 
**pillar_latest_effective_arrival_offset_map** | **Dict[str, int]** | The pillarLatestEffectiveArrivalOffsetMap. A map of additional time offsets for pillar elements. Each pillar has a latest possible arrival. As a route can consist of multiple pillars, the latest arrival at a certain pillar is also a function of  subsequent pillars. This latest arrival may shifted to a later time spot to allow shifitig a pillar around a normal node, even the normal node would fit before the pillar. | [optional] 
**flags** | **List[str]** | The flags. A list of flags indicating statii like which source finalized a route. | [optional] 
**additional_route_start_offset** | **int** | The additionalRouteStartOffset | [optional] 
**is_inactive** | **bool** | The isInactive boolean describes if a route is deactivated. | [optional] 
**is_locked_down** | **bool** | The isLockedDown. Describes if a route was undergoing lockdown. | [optional] 
**is_finalized** | **bool** | The isFinalized. Describes if a route was undergoing finalization. | [optional] 

## Example

```python
from touroptimizer_py_client.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print Route.to_json()

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_form_dict = route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


