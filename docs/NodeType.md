# NodeType

The Nodetype that can contain different Nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.node_type import NodeType

# TODO update the JSON string below
json = "{}"
# create an instance of NodeType from a JSON string
node_type_instance = NodeType.from_json(json)
# print the JSON string representation of the object
print NodeType.to_json()

# convert the object into a dict
node_type_dict = node_type_instance.to_dict()
# create an instance of NodeType from a dict
node_type_form_dict = node_type.from_dict(node_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


