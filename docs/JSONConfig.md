# JSONConfig

The extension of the configuration. For example, to provide a license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_setting** | [**CreatorSetting**](CreatorSetting.md) |  | [optional] 
**text_solution** | [**TextSolution**](TextSolution.md) |  | [optional] 
**key_setting** | [**OptimizationKeySetting**](OptimizationKeySetting.md) |  | [optional] 
**persistence_setting** | [**OptimizationPersistenceSetting**](OptimizationPersistenceSetting.md) |  | [optional] 
**plugin_settings** | [**PluginSettings**](PluginSettings.md) |  | [optional] 
**time_out** | **str** | The timeout for the optimization run. | [optional] 

## Example

```python
from touroptimizer_py_client.models.json_config import JSONConfig

# TODO update the JSON string below
json = "{}"
# create an instance of JSONConfig from a JSON string
json_config_instance = JSONConfig.from_json(json)
# print the JSON string representation of the object
print JSONConfig.to_json()

# convert the object into a dict
json_config_dict = json_config_instance.to_dict()
# create an instance of JSONConfig from a dict
json_config_form_dict = json_config.from_dict(json_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


