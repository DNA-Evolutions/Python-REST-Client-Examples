# RangeDayMonthYear

Matches any full date within the interval [from, to] (inclusive). typeName must be \"Range.DayMonthYear\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**DayMonthYear**](DayMonthYear.md) |  | [optional] 
**to** | [**DayMonthYear**](DayMonthYear.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.range_day_month_year import RangeDayMonthYear

# TODO update the JSON string below
json = "{}"
# create an instance of RangeDayMonthYear from a JSON string
range_day_month_year_instance = RangeDayMonthYear.from_json(json)
# print the JSON string representation of the object
print(RangeDayMonthYear.to_json())

# convert the object into a dict
range_day_month_year_dict = range_day_month_year_instance.to_dict()
# create an instance of RangeDayMonthYear from a dict
range_day_month_year_from_dict = RangeDayMonthYear.from_dict(range_day_month_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


