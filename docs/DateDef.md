# DateDef

Polymorphic date predicate. Use the typeName property to select the concrete subtype. Point types (Day, DayMonth, DayMonthYear, WeekDay) match a single date. Range types (Range.Day, Range.DayMonth, Range.DayMonthYear, Range.WeekDay) match any date within a from–to interval. AnyDef combines multiple predicates with OR logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.date_def import DateDef

# TODO update the JSON string below
json = "{}"
# create an instance of DateDef from a JSON string
date_def_instance = DateDef.from_json(json)
# print the JSON string representation of the object
print(DateDef.to_json())

# convert the object into a dict
date_def_dict = date_def_instance.to_dict()
# create an instance of DateDef from a dict
date_def_from_dict = DateDef.from_dict(date_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


