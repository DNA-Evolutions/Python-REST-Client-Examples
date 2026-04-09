# MultiTimeWindowNodeRelation

An advanced relation type that supports multiple time-window constraints between a master node and related nodes. Optionally requires the same visitor for all elements and can allow temporal overlaps between visits. Supports anchor details for biasing the relation scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The typeName of the object | [default to 'MultiTimeWindow']
**anchor_details** | [**List[RouteElementDetail]**](RouteElementDetail.md) | The anchorDetails. The list of anchorDetails biasing the relation. | [optional] 
**is_need_same_visitor** | **bool** | Do we want the same visitor for all elements of the relation? | 
**is_overlap_allowed** | **bool** | Do we want to allow overlaps - makes sense if isNeedSameVisitor is false? | 

## Example

```python
from touroptimizer_py_client.models.multi_time_window_node_relation import MultiTimeWindowNodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTimeWindowNodeRelation from a JSON string
multi_time_window_node_relation_instance = MultiTimeWindowNodeRelation.from_json(json)
# print the JSON string representation of the object
print(MultiTimeWindowNodeRelation.to_json())

# convert the object into a dict
multi_time_window_node_relation_dict = multi_time_window_node_relation_instance.to_dict()
# create an instance of MultiTimeWindowNodeRelation from a dict
multi_time_window_node_relation_from_dict = MultiTimeWindowNodeRelation.from_dict(multi_time_window_node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


