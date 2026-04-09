# WeekDay

Matches a specific day of the week (1 = Monday … 7 = Sunday, ISO-8601).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | ISO-8601 day of the week (1 &#x3D; Monday, 7 &#x3D; Sunday). | [optional] 

## Example

```python
from touroptimizer_py_client.models.week_day import WeekDay

# TODO update the JSON string below
json = "{}"
# create an instance of WeekDay from a JSON string
week_day_instance = WeekDay.from_json(json)
# print the JSON string representation of the object
print(WeekDay.to_json())

# convert the object into a dict
week_day_dict = week_day_instance.to_dict()
# create an instance of WeekDay from a dict
week_day_from_dict = WeekDay.from_dict(week_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


