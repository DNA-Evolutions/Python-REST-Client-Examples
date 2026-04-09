# NodeColorMultiRouteConstraint

A multi-route constraint that enforces per-color capacity limits across multiple working hours of a resource, using fractional (ratio-based) limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mirror_item** | [**IntegerMultiConstraintHelperItem**](IntegerMultiConstraintHelperItem.md) |  | 
**node_color_capacities** | [**List[NodeColorCapacity]**](NodeColorCapacity.md) | The per-color capacity limits (ratio-based) enforced by this multi-route constraint. | 
**type_name** | **str** | The typeName of the object | [default to 'NodeColorMultiRouteConstraint']

## Example

```python
from touroptimizer_py_client.models.node_color_multi_route_constraint import NodeColorMultiRouteConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of NodeColorMultiRouteConstraint from a JSON string
node_color_multi_route_constraint_instance = NodeColorMultiRouteConstraint.from_json(json)
# print the JSON string representation of the object
print(NodeColorMultiRouteConstraint.to_json())

# convert the object into a dict
node_color_multi_route_constraint_dict = node_color_multi_route_constraint_instance.to_dict()
# create an instance of NodeColorMultiRouteConstraint from a dict
node_color_multi_route_constraint_from_dict = NodeColorMultiRouteConstraint.from_dict(node_color_multi_route_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


