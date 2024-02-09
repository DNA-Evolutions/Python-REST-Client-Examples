# ResourceTrip

Trips representing the route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | [**EncodedPolyline**](EncodedPolyline.md) |  | 
**from_element_id** | **str** | The position the polyline starts. | 
**to_element_id** | **str** | The position the polyline ends. | 
**raw_json** | **object** | The raw json descirbing the trip. | [optional] 

## Example

```python
from touroptimizer_py_client.models.resource_trip import ResourceTrip

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTrip from a JSON string
resource_trip_instance = ResourceTrip.from_json(json)
# print the JSON string representation of the object
print ResourceTrip.to_json()

# convert the object into a dict
resource_trip_dict = resource_trip_instance.to_dict()
# create an instance of ResourceTrip from a dict
resource_trip_form_dict = resource_trip.from_dict(resource_trip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


