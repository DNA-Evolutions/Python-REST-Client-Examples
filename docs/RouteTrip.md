# RouteTrip

Additional data aobut the route trip. For example, the polylines for map reprsentation purposes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trips** | [**List[ResourceTrip]**](ResourceTrip.md) | Trips representing the route. | 

## Example

```python
from touroptimizer_py_client.models.route_trip import RouteTrip

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTrip from a JSON string
route_trip_instance = RouteTrip.from_json(json)
# print the JSON string representation of the object
print RouteTrip.to_json()

# convert the object into a dict
route_trip_dict = route_trip_instance.to_dict()
# create an instance of RouteTrip from a dict
route_trip_form_dict = route_trip.from_dict(route_trip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


