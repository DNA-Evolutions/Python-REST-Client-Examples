# OptimizationPersistenceSetting

The persistenceSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_settings** | [**MongoOptimizationPersistenceSetting**](MongoOptimizationPersistenceSetting.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.optimization_persistence_setting import OptimizationPersistenceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationPersistenceSetting from a JSON string
optimization_persistence_setting_instance = OptimizationPersistenceSetting.from_json(json)
# print the JSON string representation of the object
print OptimizationPersistenceSetting.to_json()

# convert the object into a dict
optimization_persistence_setting_dict = optimization_persistence_setting_instance.to_dict()
# create an instance of OptimizationPersistenceSetting from a dict
optimization_persistence_setting_form_dict = optimization_persistence_setting.from_dict(optimization_persistence_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


