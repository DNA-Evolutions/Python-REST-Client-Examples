# GeoPillarNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_resource_id** | **str** | The attached resourceId. A geoPillar must be visited by this resource. | [optional] 
**only_scheduled_in_company** | **bool** | If true, this pillar node is only scheduled when the attached resource is part of the same organizational company/group. Prevents cross-company pillar assignments in multi-fleet scenarios. | [optional] 
**connection_related_late_margin** | [**ConnectionRelatedLateMargin**](ConnectionRelatedLateMargin.md) |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'GeoPillarNode']
**is_forced_stay_node** | **bool** | If true, the optimizer must treat this pillar node as an overnight-stay location. The route will terminate here and the next working-hour route will start from this position. | [optional] 
**is_auto_transformable2_start_anchor** | **bool** | If true, the optimizer may automatically promote this pillar to a route-start anchor when it determines that doing so improves the overall solution quality. Allows flexible anchor assignment without manual configuration. | [optional] 
**is_overwriting_route_start** | **bool** | The boolean isOverwritingRouteStart. Instead of using the default start element of the route, the geoPillar will be used as so-called startAnchor. | [optional] 
**is_schedulable_after_working_hours** | **bool** | If true, the optimizer is allowed to schedule this pillar node after the resource&#39;s official working-hours end. Useful for mandatory end-of-day stops (e.g. vehicle return, paperwork drop-off). | [optional] 
**is_overwriting_route_termination** | **bool** | The boolean isOverwritingRouteTermination. Instead of using the default termination element of the route, the geoPillar will be used as so-called endAnchor. | [optional] 
**is_schedulable_before_working_hours** | **bool** | If true, the optimizer is allowed to schedule this pillar node before the resource&#39;s official working-hours start. Useful for mandatory stops (e.g. depot loading) that must happen pre-shift. | [optional] 
**is_time_adjustable_anchor** | **bool** | If true, the anchor timing derived from this pillar is allowed to shift within the working-hour boundaries. Enables the optimizer to adjust the schedule around fixed appointments while maintaining the pillar&#39;s role as a route start or termination anchor. | [optional] 

## Example

```python
from touroptimizer_py_client.models.geo_pillar_node import GeoPillarNode

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPillarNode from a JSON string
geo_pillar_node_instance = GeoPillarNode.from_json(json)
# print the JSON string representation of the object
print(GeoPillarNode.to_json())

# convert the object into a dict
geo_pillar_node_dict = geo_pillar_node_instance.to_dict()
# create an instance of GeoPillarNode from a dict
geo_pillar_node_from_dict = GeoPillarNode.from_dict(geo_pillar_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


