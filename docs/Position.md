# Position

The end position of the route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of the position | 
**longitude** | **float** | The longitude of the position | 
**location_id** | **str** | An optional location identifier that links this position to a shared location. Elements with the same locationId share the same geographic coordinates and connection data, reducing input size. | [optional] 
**geo_address** | [**GeoAddress**](GeoAddress.md) |  | [optional] 
**location_parameters** | [**LocationParameters**](LocationParameters.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


