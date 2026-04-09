# RangeWeekDay

Matches any ISO weekday within the interval [from, to] (inclusive, wrapping). typeName must be \"Range.WeekDay\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**WeekDay**](WeekDay.md) |  | [optional] 
**to** | [**WeekDay**](WeekDay.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.range_week_day import RangeWeekDay

# TODO update the JSON string below
json = "{}"
# create an instance of RangeWeekDay from a JSON string
range_week_day_instance = RangeWeekDay.from_json(json)
# print the JSON string representation of the object
print(RangeWeekDay.to_json())

# convert the object into a dict
range_week_day_dict = range_week_day_instance.to_dict()
# create an instance of RangeWeekDay from a dict
range_week_day_from_dict = RangeWeekDay.from_dict(range_week_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


