# JSONConfig

A generic extension object that carries environment-specific configuration outside the core optimization model. In the REST/Docker variant (where EXT = JSONConfig), this typically includes: the license key setting (keySetting), persistence settings for Fire-and-Forget mode (persistenceSetting with MongoDB configuration, encryption secrets, stream persistence strategies, and TTL expiry), a creator setting for tenant identification, and a timeout duration. The extension is stripped of sensitive fields (e.g. keySetting) before the result is persisted to the database.

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
print(JSONConfig.to_json())

# convert the object into a dict
json_config_dict = json_config_instance.to_dict()
# create an instance of JSONConfig from a dict
json_config_from_dict = JSONConfig.from_dict(json_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


