# OptimizationPersistenceStratgySetting

The optimizationPersistenceStratgySetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_only_result** | **bool** | The saveOnlyResult | 
**save_connections** | **bool** | The saveConnections. Only takes action if saveOnlyResult is false. | [optional] 

## Example

```python
from touroptimizer_py_client.models.optimization_persistence_stratgy_setting import OptimizationPersistenceStratgySetting

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationPersistenceStratgySetting from a JSON string
optimization_persistence_stratgy_setting_instance = OptimizationPersistenceStratgySetting.from_json(json)
# print the JSON string representation of the object
print OptimizationPersistenceStratgySetting.to_json()

# convert the object into a dict
optimization_persistence_stratgy_setting_dict = optimization_persistence_stratgy_setting_instance.to_dict()
# create an instance of OptimizationPersistenceStratgySetting from a dict
optimization_persistence_stratgy_setting_form_dict = optimization_persistence_stratgy_setting.from_dict(optimization_persistence_stratgy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


