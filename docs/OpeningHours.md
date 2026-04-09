# OpeningHours

A time window during which a node is available for visits. Defined by a begin and end instant with a time zone. Supports preferred-window hints, sub-window offsets (e.g. lunch breaks), and exclusive solo-access mode. Multiple non-overlapping opening hours per node are supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **datetime** | The begin of the Opening Hour | 
**end** | **datetime** | The end of the Opening Hour | 
**zone_id** | **str** | The zoneId of the Opening Hour | 
**service_hours_offsets** | [**List[LongLongPair]**](LongLongPair.md) | Optional offset pairs that define sub-windows within this opening hour during which the node can actually be serviced. Each pair specifies a start offset and an end offset (in milliseconds) relative to the opening-hour begin. Useful for modeling lunch breaks, shift handovers, or restricted access periods within an otherwise open time window. | [optional] 
**is_preffered** | **bool** | The isPreffered boolean. If an Opening Hour is preffered the Optimizer will try to visit the node inside this Opening Hour. By default, the first Openinghour of a node is the preffered opening hour. | [optional] [default to False]
**is_solo_access_hours** | **bool** | If true, this opening hour grants exclusive access — the node can only be visited during this specific time window and not during any other opening hour of the same node. Useful for modeling time slots that require dedicated attention (e.g. a VIP appointment slot that cannot overlap with general availability). | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.opening_hours import OpeningHours

# TODO update the JSON string below
json = "{}"
# create an instance of OpeningHours from a JSON string
opening_hours_instance = OpeningHours.from_json(json)
# print the JSON string representation of the object
print(OpeningHours.to_json())

# convert the object into a dict
opening_hours_dict = opening_hours_instance.to_dict()
# create an instance of OpeningHours from a dict
opening_hours_from_dict = OpeningHours.from_dict(opening_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


