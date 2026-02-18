# TypeDictionaries

The optional typeDictionaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_dictionaries** | [**List[TypeDictionary]**](TypeDictionary.md) | The optional list of typeDictionaries | [optional] 

## Example

```python
from touroptimizer_py_client.models.type_dictionaries import TypeDictionaries

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDictionaries from a JSON string
type_dictionaries_instance = TypeDictionaries.from_json(json)
# print the JSON string representation of the object
print(TypeDictionaries.to_json())

# convert the object into a dict
type_dictionaries_dict = type_dictionaries_instance.to_dict()
# create an instance of TypeDictionaries from a dict
type_dictionaries_from_dict = TypeDictionaries.from_dict(type_dictionaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


