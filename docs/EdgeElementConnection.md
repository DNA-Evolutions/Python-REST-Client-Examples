# EdgeElementConnection

An edge-based connection between two elements specifying travel distance, optional travel time, and optional time-dependent traffic profiles via connectionByTime. The standard connection type used to supply precomputed routing data to the optimizer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **str** | The distance of the connection. | 
**time** | **str** | The time needed to pass the connection. | [optional] 
**from_position** | [**Position**](Position.md) |  | [optional] 
**to_position** | [**Position**](Position.md) |  | [optional] 
**connection_by_time** | [**ConnectionByTime**](ConnectionByTime.md) |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'Edge']

## Example

```python
from touroptimizer_py_client.models.edge_element_connection import EdgeElementConnection

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeElementConnection from a JSON string
edge_element_connection_instance = EdgeElementConnection.from_json(json)
# print the JSON string representation of the object
print(EdgeElementConnection.to_json())

# convert the object into a dict
edge_element_connection_dict = edge_element_connection_instance.to_dict()
# create an instance of EdgeElementConnection from a dict
edge_element_connection_from_dict = EdgeElementConnection.from_dict(edge_element_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


