# ILoad

A load attached to a node depot that represents goods to be picked up (supply) or delivered (request). Subtypes include simple loads, unload-all loads, timed loads (with maximum transport duration), and flexible loads (mixed, supply-only, or request-only flex loads that adjust dynamically during optimization).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] 
**load_value** | **float** |  | [optional] 
**request** | **bool** |  | [optional] 
**fuzzy_visit** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.i_load import ILoad

# TODO update the JSON string below
json = "{}"
# create an instance of ILoad from a JSON string
i_load_instance = ILoad.from_json(json)
# print the JSON string representation of the object
print(ILoad.to_json())

# convert the object into a dict
i_load_dict = i_load_instance.to_dict()
# create an instance of ILoad from a dict
i_load_from_dict = ILoad.from_dict(i_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


