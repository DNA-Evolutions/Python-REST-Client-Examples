# GeoPillarNode

The optional pillarNode. If a node has the pillarNode attibute attached, it becomes a pillar node itself. A pillar nodes openingHour cannot be violated. If a violation cannot be avoided, the pillar will be unassigned instead of being violated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_resource_id** | **str** | The attached resourceId. A geoPillar must be visited by this resource. | [optional] 
**only_scheduled_in_company** | **bool** | The onlyScheduledInCompany | [optional] 
**connection_related_late_margin** | [**ConnectionRelatedLateMargin**](ConnectionRelatedLateMargin.md) |  | [optional] 
**is_auto_transformable2_start_anchor** | **bool** | The isAutoTransformable2StartAnchor | [optional] 
**is_schedulable_after_working_hours** | **bool** | The isSchedulableAfterWorkingHours | [optional] 
**is_overwriting_route_start** | **bool** | The boolean isOverwritingRouteStart. Instead of using the default start element of the route, the geoPillar will be used as so-called startAnchor. | [optional] 
**is_overwriting_route_termination** | **bool** | The boolean isOverwritingRouteTermination. Instead of using the default termination element of the route, the geoPillar will be used as so-called endAnchor. | [optional] 
**is_time_adjustable_anchor** | **bool** | The isTimeAdjustableAnchor | [optional] 
**is_schedulable_before_working_hours** | **bool** | The isSchedulableBeforeWorkingHours | [optional] 
**is_forced_stay_node** | **bool** | The isForcedStayNode | [optional] 

## Example

```python
from touroptimizer_py_client.models.geo_pillar_node import GeoPillarNode

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPillarNode from a JSON string
geo_pillar_node_instance = GeoPillarNode.from_json(json)
# print the JSON string representation of the object
print GeoPillarNode.to_json()

# convert the object into a dict
geo_pillar_node_dict = geo_pillar_node_instance.to_dict()
# create an instance of GeoPillarNode from a dict
geo_pillar_node_form_dict = geo_pillar_node.from_dict(geo_pillar_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


