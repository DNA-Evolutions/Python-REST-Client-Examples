# ILoad

The Load type that can contain different loads

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] 
**load_value** | **float** |  | [optional] 
**fuzzy_visit** | **bool** |  | [optional] 
**request** | **bool** |  | [optional] 
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
print ILoad.to_json()

# convert the object into a dict
i_load_dict = i_load_instance.to_dict()
# create an instance of ILoad from a dict
i_load_form_dict = i_load.from_dict(i_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


