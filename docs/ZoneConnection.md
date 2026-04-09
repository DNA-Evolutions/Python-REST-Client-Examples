# ZoneConnection

Zone connections define penalties or restrictions for crossing geographic zone boundaries (e.g. bridge tolls, tunnel crossings, or administrative borders). Each ZoneConnection specifies a pair of zone numbers and an associated crossing cost. When a route transitions between zones, the optimizer accumulates these costs, which discourages unnecessary zone crossings and promotes geographically cohesive routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_zone_id** | **str** | The zone that is left. | 
**to_zone_id** | **str** | The zone that is entered. | 
**crossing_penalty_multiplier** | **float** | The crossingPenaltyMultiplier when going fromZoneId to toZoneId | [optional] 

## Example

```python
from touroptimizer_py_client.models.zone_connection import ZoneConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneConnection from a JSON string
zone_connection_instance = ZoneConnection.from_json(json)
# print the JSON string representation of the object
print(ZoneConnection.to_json())

# convert the object into a dict
zone_connection_dict = zone_connection_instance.to_dict()
# create an instance of ZoneConnection from a dict
zone_connection_from_dict = ZoneConnection.from_dict(zone_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


