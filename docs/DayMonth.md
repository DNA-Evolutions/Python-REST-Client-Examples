# DayMonth

Matches a specific day within a specific month.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | Month of the year (1–12). | [optional] 
**day** | **int** | Day of the month (1–31). | [optional] 

## Example

```python
from touroptimizer_py_client.models.day_month import DayMonth

# TODO update the JSON string below
json = "{}"
# create an instance of DayMonth from a JSON string
day_month_instance = DayMonth.from_json(json)
# print the JSON string representation of the object
print(DayMonth.to_json())

# convert the object into a dict
day_month_dict = day_month_instance.to_dict()
# create an instance of DayMonth from a dict
day_month_from_dict = DayMonth.from_dict(day_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


