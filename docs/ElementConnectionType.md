# ElementConnectionType

The type of the connection. Usually a connection of tyoe 'Edge' is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.element_connection_type import ElementConnectionType

# TODO update the JSON string below
json = "{}"
# create an instance of ElementConnectionType from a JSON string
element_connection_type_instance = ElementConnectionType.from_json(json)
# print the JSON string representation of the object
print ElementConnectionType.to_json()

# convert the object into a dict
element_connection_type_dict = element_connection_type_instance.to_dict()
# create an instance of ElementConnectionType from a dict
element_connection_type_form_dict = element_connection_type.from_dict(element_connection_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


