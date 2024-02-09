# OpeningHours

The list of non-overlapping openingHours of the nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **datetime** | The begin of the Opening Hour | 
**end** | **datetime** | The end of the Opening Hour | 
**zone_id** | **str** | The zoneId of the Opening Hour | 
**service_hours_offsets** | [**List[LongLongPair]**](LongLongPair.md) | The serviceHoursOffsets | [optional] 
**is_preffered** | **bool** | The isPreffered boolean. If an Opening Hour is preffered the Optimizer will try to visit the node inside this Opening Hour. By default, the first Openinghour of a node is the preffered opening hour. | [optional] [default to False]
**is_solo_access_hours** | **bool** | The isSoloAccessHours | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.opening_hours import OpeningHours

# TODO update the JSON string below
json = "{}"
# create an instance of OpeningHours from a JSON string
opening_hours_instance = OpeningHours.from_json(json)
# print the JSON string representation of the object
print OpeningHours.to_json()

# convert the object into a dict
opening_hours_dict = opening_hours_instance.to_dict()
# create an instance of OpeningHours from a dict
opening_hours_form_dict = opening_hours.from_dict(opening_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


