# DayMonthYear

Matches a specific date (year, month, day).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | Year. | [optional] 
**month** | **int** | Month of the year (1–12). | [optional] 
**day** | **int** | Day of the month (1–31). | [optional] 

## Example

```python
from touroptimizer_py_client.models.day_month_year import DayMonthYear

# TODO update the JSON string below
json = "{}"
# create an instance of DayMonthYear from a JSON string
day_month_year_instance = DayMonthYear.from_json(json)
# print the JSON string representation of the object
print(DayMonthYear.to_json())

# convert the object into a dict
day_month_year_dict = day_month_year_instance.to_dict()
# create an instance of DayMonthYear from a dict
day_month_year_from_dict = DayMonthYear.from_dict(day_month_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


