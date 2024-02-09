# ElementConnection

The list of connections

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
print ElementConnection.to_json()

# convert the object into a dict
element_connection_dict = element_connection_instance.to_dict()
# create an instance of ElementConnection from a dict
element_connection_form_dict = element_connection.from_dict(element_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


