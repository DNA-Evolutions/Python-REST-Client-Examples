# LongLongPair

Optional offset pairs that define sub-windows within this opening hour during which the node can actually be serviced. Each pair specifies a start offset and an end offset (in milliseconds) relative to the opening-hour begin. Useful for modeling lunch breaks, shift handovers, or restricted access periods within an otherwise open time window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **int** | The start offset value (in milliseconds). | 
**right** | **int** | The end offset value (in milliseconds). | 

## Example

```python
from touroptimizer_py_client.models.long_long_pair import LongLongPair

# TODO update the JSON string below
json = "{}"
# create an instance of LongLongPair from a JSON string
long_long_pair_instance = LongLongPair.from_json(json)
# print the JSON string representation of the object
print(LongLongPair.to_json())

# convert the object into a dict
long_long_pair_dict = long_long_pair_instance.to_dict()
# create an instance of LongLongPair from a dict
long_long_pair_from_dict = LongLongPair.from_dict(long_long_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


