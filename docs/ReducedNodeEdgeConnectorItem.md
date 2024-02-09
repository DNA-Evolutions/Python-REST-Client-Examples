# ReducedNodeEdgeConnectorItem

The list of hook connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **str** | The distance of the hook connection. | 
**time** | **str** | The time needed to pass the hook connection. | 
**from_element_id** | **str** | The fromElementId defines the element where the connections starts. | 
**to_element_id** | **str** | The toElementId defines the element where the connections ends. | 

## Example

```python
from touroptimizer_py_client.models.reduced_node_edge_connector_item import ReducedNodeEdgeConnectorItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedNodeEdgeConnectorItem from a JSON string
reduced_node_edge_connector_item_instance = ReducedNodeEdgeConnectorItem.from_json(json)
# print the JSON string representation of the object
print ReducedNodeEdgeConnectorItem.to_json()

# convert the object into a dict
reduced_node_edge_connector_item_dict = reduced_node_edge_connector_item_instance.to_dict()
# create an instance of ReducedNodeEdgeConnectorItem from a dict
reduced_node_edge_connector_item_form_dict = reduced_node_edge_connector_item.from_dict(reduced_node_edge_connector_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


