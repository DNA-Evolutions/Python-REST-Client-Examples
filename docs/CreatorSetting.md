# CreatorSetting

The creatorSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | The creator | [optional] 

## Example

```python
from touroptimizer_py_client.models.creator_setting import CreatorSetting

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorSetting from a JSON string
creator_setting_instance = CreatorSetting.from_json(json)
# print the JSON string representation of the object
print CreatorSetting.to_json()

# convert the object into a dict
creator_setting_dict = creator_setting_instance.to_dict()
# create an instance of CreatorSetting from a dict
creator_setting_form_dict = creator_setting.from_dict(creator_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


