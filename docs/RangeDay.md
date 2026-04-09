# RangeDay

Matches any day of the month within the interval [from.day, to.day] (inclusive). typeName must be \"Range.Day\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**Day**](Day.md) |  | [optional] 
**to** | [**Day**](Day.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.range_day import RangeDay

# TODO update the JSON string below
json = "{}"
# create an instance of RangeDay from a JSON string
range_day_instance = RangeDay.from_json(json)
# print the JSON string representation of the object
print(RangeDay.to_json())

# convert the object into a dict
range_day_dict = range_day_instance.to_dict()
# create an instance of RangeDay from a dict
range_day_from_dict = RangeDay.from_dict(range_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


