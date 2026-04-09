# StringIntegerPair

A list of key-value pairs mapping element identifiers to integer values. Used internally to mirror multi-route constraint configurations across working hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | A string key, typically a node or element identifier. | 
**right** | **int** | An integer value associated with the key (e.g. a count, index, or capacity value). | 

## Example

```python
from touroptimizer_py_client.models.string_integer_pair import StringIntegerPair

# TODO update the JSON string below
json = "{}"
# create an instance of StringIntegerPair from a JSON string
string_integer_pair_instance = StringIntegerPair.from_json(json)
# print the JSON string representation of the object
print(StringIntegerPair.to_json())

# convert the object into a dict
string_integer_pair_dict = string_integer_pair_instance.to_dict()
# create an instance of StringIntegerPair from a dict
string_integer_pair_from_dict = StringIntegerPair.from_dict(string_integer_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


