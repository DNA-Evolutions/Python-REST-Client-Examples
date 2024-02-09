# AbsoluteNodeColorMultiRouteConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mirror_item** | [**IntegerMultiConstraintHelperItem**](IntegerMultiConstraintHelperItem.md) |  | 
**absolute_node_color_capacities** | [**List[AbsoluteNodeColorCapacity]**](AbsoluteNodeColorCapacity.md) | The absoluteNodeColorCapacities | 
**type_name** | **str** | The typeName of the object | [default to 'AbsoluteNodeColorMultiRouteConstraint']

## Example

```python
from touroptimizer_py_client.models.absolute_node_color_multi_route_constraint import AbsoluteNodeColorMultiRouteConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AbsoluteNodeColorMultiRouteConstraint from a JSON string
absolute_node_color_multi_route_constraint_instance = AbsoluteNodeColorMultiRouteConstraint.from_json(json)
# print the JSON string representation of the object
print AbsoluteNodeColorMultiRouteConstraint.to_json()

# convert the object into a dict
absolute_node_color_multi_route_constraint_dict = absolute_node_color_multi_route_constraint_instance.to_dict()
# create an instance of AbsoluteNodeColorMultiRouteConstraint from a dict
absolute_node_color_multi_route_constraint_form_dict = absolute_node_color_multi_route_constraint.from_dict(absolute_node_color_multi_route_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


