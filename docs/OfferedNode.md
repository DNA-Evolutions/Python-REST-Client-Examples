# OfferedNode

Defines if the node should be treated as offered node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**individual_multiplier** | **float** | The cost multiplier for an offered node. If the multiplier is bigger than 1.0 the chances that the node shows violations is getting less. | [optional] 

## Example

```python
from touroptimizer_py_client.models.offered_node import OfferedNode

# TODO update the JSON string below
json = "{}"
# create an instance of OfferedNode from a JSON string
offered_node_instance = OfferedNode.from_json(json)
# print the JSON string representation of the object
print OfferedNode.to_json()

# convert the object into a dict
offered_node_dict = offered_node_instance.to_dict()
# create an instance of OfferedNode from a dict
offered_node_form_dict = offered_node.from_dict(offered_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


