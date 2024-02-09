# PluginSetting

The plugins

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_name** | **str** | The pluginName | 
**json_setting** | **str** | The jsonSetting | 
**is_active** | **bool** | The plugin can be deactivated. By default, if a setting exists, the plugin is also activated | 

## Example

```python
from touroptimizer_py_client.models.plugin_setting import PluginSetting

# TODO update the JSON string below
json = "{}"
# create an instance of PluginSetting from a JSON string
plugin_setting_instance = PluginSetting.from_json(json)
# print the JSON string representation of the object
print PluginSetting.to_json()

# convert the object into a dict
plugin_setting_dict = plugin_setting_instance.to_dict()
# create an instance of PluginSetting from a dict
plugin_setting_form_dict = plugin_setting.from_dict(plugin_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


