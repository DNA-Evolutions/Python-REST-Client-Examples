# NodeRelation

The list of inter-node relations that impose ordering or co-assignment constraints between nodes. Supported relation types include SAME_ROUTE (nodes must be on the same route), SAME_VISITOR (nodes must be served by the same resource), DIFFERENT_ROUTE (nodes must not share a route), and relative time-window relations that enforce temporal precedence (e.g. node A must be visited before node B within a defined time gap).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_node_id** | **str** | The id of the master node in this relation. The master node serves as the anchor point — constraints are evaluated relative to this node&#39;s scheduling (e.g. &#39;master must be visited before related&#39;). | 
**related_node_ids** | **List[str]** | The list of related node ids that are coupled to the master node via this relation. All listed nodes must satisfy the relation type (e.g. all must be on the same route as the master). | 
**type** | [**NodeRelationType**](NodeRelationType.md) |  | 
**relation_mode** | **str** | The enforcement mode of this relation. STRONG (default) means the optimizer always respects it. WEAK allows the optimizer to violate the relation at a cost if no feasible solution can satisfy it. | [optional] 

## Example

```python
from touroptimizer_py_client.models.node_relation import NodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRelation from a JSON string
node_relation_instance = NodeRelation.from_json(json)
# print the JSON string representation of the object
print(NodeRelation.to_json())

# convert the object into a dict
node_relation_dict = node_relation_instance.to_dict()
# create an instance of NodeRelation from a dict
node_relation_from_dict = NodeRelation.from_dict(node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


