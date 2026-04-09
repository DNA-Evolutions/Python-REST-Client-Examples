# ElementConnection

Pre-computed pairwise connections between elements (nodes and resources). Each connection specifies the travel distance and time between a source and a target element, optionally including time-dependent traffic profiles via connectionByTime. If connections are not provided, the optimizer falls back to a Haversine-based distance approximation or a configured backup connector. Providing accurate connections significantly improves solution quality. In persisted results, this list may be omitted to conserve storage (controlled via saveConnections).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_element_id** | **str** | The fromElementId defines the element where the connections starts. | 
**to_element_id** | **str** | The toElementId defines the element where the connections ends. | 
**type** | [**ElementConnectionType**](ElementConnectionType.md) |  | 

## Example

```python
from touroptimizer_py_client.models.element_connection import ElementConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ElementConnection from a JSON string
element_connection_instance = ElementConnection.from_json(json)
# print the JSON string representation of the object
print(ElementConnection.to_json())

# convert the object into a dict
element_connection_dict = element_connection_instance.to_dict()
# create an instance of ElementConnection from a dict
element_connection_from_dict = ElementConnection.from_dict(element_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


