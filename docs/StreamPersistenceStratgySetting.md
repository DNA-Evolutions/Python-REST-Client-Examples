# StreamPersistenceStratgySetting

The streamPersistenceStratgySetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_progress** | **bool** | The saveProgress | 
**cycle_progress** | **bool** | Cycle progress. Only takes action if saveProgress is true. | [optional] 
**save_status** | **bool** | The saveStatus | 
**cycle_status** | **bool** | Cycle status. Only takes action if saveStatus is true. | [optional] 
**save_warning** | **bool** | The saveWarning | 
**save_error** | **bool** | The saveError | 

## Example

```python
from touroptimizer_py_client.models.stream_persistence_stratgy_setting import StreamPersistenceStratgySetting

# TODO update the JSON string below
json = "{}"
# create an instance of StreamPersistenceStratgySetting from a JSON string
stream_persistence_stratgy_setting_instance = StreamPersistenceStratgySetting.from_json(json)
# print the JSON string representation of the object
print StreamPersistenceStratgySetting.to_json()

# convert the object into a dict
stream_persistence_stratgy_setting_dict = stream_persistence_stratgy_setting_instance.to_dict()
# create an instance of StreamPersistenceStratgySetting from a dict
stream_persistence_stratgy_setting_form_dict = stream_persistence_stratgy_setting.from_dict(stream_persistence_stratgy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


