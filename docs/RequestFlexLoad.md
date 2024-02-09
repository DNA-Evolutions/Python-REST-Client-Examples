# RequestFlexLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_id** | **str** |  | [optional] 
**is_request** | **bool** |  | [optional] 
**is_fuzzy_visit** | **bool** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'RequestFlexLoad']

## Example

```python
from touroptimizer_py_client.models.request_flex_load import RequestFlexLoad

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFlexLoad from a JSON string
request_flex_load_instance = RequestFlexLoad.from_json(json)
# print the JSON string representation of the object
print RequestFlexLoad.to_json()

# convert the object into a dict
request_flex_load_dict = request_flex_load_instance.to_dict()
# create an instance of RequestFlexLoad from a dict
request_flex_load_form_dict = request_flex_load.from_dict(request_flex_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


