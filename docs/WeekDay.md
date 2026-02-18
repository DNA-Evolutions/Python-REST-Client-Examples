# WeekDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**WeekDay**](WeekDay.md) |  | [optional] 
**to** | [**WeekDay**](WeekDay.md) |  | [optional] 

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


