# AnyDefAllOfTimeDefs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 
**time_defs** | [**List[AnyDefAllOfTimeDefs]**](AnyDefAllOfTimeDefs.md) | List of date predicates evaluated with OR logic. The containing AnyDef matches if at least one entry matches. | [optional] 
**day** | **int** | ISO-8601 day of the week (1 &#x3D; Monday, 7 &#x3D; Sunday). | [optional] 
**month** | **int** | Month of the year (1–12). | [optional] 
**year** | **int** | Year. | [optional] 
**var_from** | [**WeekDay**](WeekDay.md) |  | [optional] 
**to** | [**WeekDay**](WeekDay.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.any_def_all_of_time_defs import AnyDefAllOfTimeDefs

# TODO update the JSON string below
json = "{}"
# create an instance of AnyDefAllOfTimeDefs from a JSON string
any_def_all_of_time_defs_instance = AnyDefAllOfTimeDefs.from_json(json)
# print the JSON string representation of the object
print(AnyDefAllOfTimeDefs.to_json())

# convert the object into a dict
any_def_all_of_time_defs_dict = any_def_all_of_time_defs_instance.to_dict()
# create an instance of AnyDefAllOfTimeDefs from a dict
any_def_all_of_time_defs_from_dict = AnyDefAllOfTimeDefs.from_dict(any_def_all_of_time_defs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


