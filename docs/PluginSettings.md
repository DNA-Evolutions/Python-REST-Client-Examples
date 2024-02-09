# PluginSettings

The PluginSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | [**List[PluginSetting]**](PluginSetting.md) | The plugins | 

## Example

```python
from touroptimizer_py_client.models.plugin_settings import PluginSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PluginSettings from a JSON string
plugin_settings_instance = PluginSettings.from_json(json)
# print the JSON string representation of the object
print PluginSettings.to_json()

# convert the object into a dict
plugin_settings_dict = plugin_settings_instance.to_dict()
# create an instance of PluginSettings from a dict
plugin_settings_form_dict = plugin_settings.from_dict(plugin_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


