# NodeRelation

The list of relations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_node_id** | **str** | The masterNodeId | 
**related_node_ids** | **List[str]** | The relatedNodeIds | 
**type** | [**NodeRelationType**](NodeRelationType.md) |  | 
**relation_mode** | **str** | The relationMode | [optional] 

## Example

```python
from touroptimizer_py_client.models.node_relation import NodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRelation from a JSON string
node_relation_instance = NodeRelation.from_json(json)
# print the JSON string representation of the object
print NodeRelation.to_json()

# convert the object into a dict
node_relation_dict = node_relation_instance.to_dict()
# create an instance of NodeRelation from a dict
node_relation_form_dict = node_relation.from_dict(node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


