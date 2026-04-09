# AnyDef

Composite date predicate that matches when ANY of the contained timeDefs match (logical OR). Each entry in timeDefs can be any concrete DateDef subtype. typeName must be \"Any\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_defs** | [**List[AnyDefAllOfTimeDefs]**](AnyDefAllOfTimeDefs.md) | List of date predicates evaluated with OR logic. The containing AnyDef matches if at least one entry matches. | [optional] 

## Example

```python
from touroptimizer_py_client.models.any_def import AnyDef

# TODO update the JSON string below
json = "{}"
# create an instance of AnyDef from a JSON string
any_def_instance = AnyDef.from_json(json)
# print the JSON string representation of the object
print(AnyDef.to_json())

# convert the object into a dict
any_def_dict = any_def_instance.to_dict()
# create an instance of AnyDef from a dict
any_def_from_dict = AnyDef.from_dict(any_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


