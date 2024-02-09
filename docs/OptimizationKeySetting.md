# OptimizationKeySetting

The keySetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_license** | **str** | The jsonLicense | [optional] 

## Example

```python
from touroptimizer_py_client.models.optimization_key_setting import OptimizationKeySetting

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationKeySetting from a JSON string
optimization_key_setting_instance = OptimizationKeySetting.from_json(json)
# print the JSON string representation of the object
print OptimizationKeySetting.to_json()

# convert the object into a dict
optimization_key_setting_dict = optimization_key_setting_instance.to_dict()
# create an instance of OptimizationKeySetting from a dict
optimization_key_setting_form_dict = optimization_key_setting.from_dict(optimization_key_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


