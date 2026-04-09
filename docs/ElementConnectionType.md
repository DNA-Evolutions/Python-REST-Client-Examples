# ElementConnectionType

A precomputed connection (distance and driving time) between two elements (nodes or resources). Used to supply custom or externally calculated travel data instead of relying on the optimizer's internal distance calculation. Currently supports edge-based connections.

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
print(ElementConnectionType.to_json())

# convert the object into a dict
element_connection_type_dict = element_connection_type_instance.to_dict()
# create an instance of ElementConnectionType from a dict
element_connection_type_from_dict = ElementConnectionType.from_dict(element_connection_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


