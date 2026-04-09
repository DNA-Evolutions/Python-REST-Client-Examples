# RangeDayMonth

Matches any month-day combination within the interval [from, to] (inclusive). typeName must be \"Range.DayMonth\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**DayMonth**](DayMonth.md) |  | [optional] 
**to** | [**DayMonth**](DayMonth.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.range_day_month import RangeDayMonth

# TODO update the JSON string below
json = "{}"
# create an instance of RangeDayMonth from a JSON string
range_day_month_instance = RangeDayMonth.from_json(json)
# print the JSON string representation of the object
print(RangeDayMonth.to_json())

# convert the object into a dict
range_day_month_dict = range_day_month_instance.to_dict()
# create an instance of RangeDayMonth from a dict
range_day_month_from_dict = RangeDayMonth.from_dict(range_day_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


