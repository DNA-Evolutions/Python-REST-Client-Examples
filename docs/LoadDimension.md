# LoadDimension

The loadDimension

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unload_all_dimension** | **int** | The unloadAllDimension | 
**total_load_dimension** | **int** | The totalLoadDimension | 
**unload_all** | **bool** | The unloadAll | [optional] 

## Example

```python
from touroptimizer_py_client.models.load_dimension import LoadDimension

# TODO update the JSON string below
json = "{}"
# create an instance of LoadDimension from a JSON string
load_dimension_instance = LoadDimension.from_json(json)
# print the JSON string representation of the object
print LoadDimension.to_json()

# convert the object into a dict
load_dimension_dict = load_dimension_instance.to_dict()
# create an instance of LoadDimension from a dict
load_dimension_form_dict = load_dimension.from_dict(load_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


