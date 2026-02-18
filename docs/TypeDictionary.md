# TypeDictionary

The optional list of typeDictionaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | **Dict[str, str]** | The mapping of a certain type. or multiple types | 
**type_names** | **List[str]** | List of type names this dictionary applies to. | 

## Example

```python
from touroptimizer_py_client.models.type_dictionary import TypeDictionary

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDictionary from a JSON string
type_dictionary_instance = TypeDictionary.from_json(json)
# print the JSON string representation of the object
print(TypeDictionary.to_json())

# convert the object into a dict
type_dictionary_dict = type_dictionary_instance.to_dict()
# create an instance of TypeDictionary from a dict
type_dictionary_from_dict = TypeDictionary.from_dict(type_dictionary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


