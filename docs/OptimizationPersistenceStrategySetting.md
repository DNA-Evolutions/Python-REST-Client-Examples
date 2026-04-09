# OptimizationPersistenceStrategySetting

The optimizationPersistenceStrategySetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_connections** | **bool** | The saveConnections. Only takes action if saveOnlyResult is false. | [optional] 

## Example

```python
from touroptimizer_py_client.models.optimization_persistence_strategy_setting import OptimizationPersistenceStrategySetting

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationPersistenceStrategySetting from a JSON string
optimization_persistence_strategy_setting_instance = OptimizationPersistenceStrategySetting.from_json(json)
# print the JSON string representation of the object
print(OptimizationPersistenceStrategySetting.to_json())

# convert the object into a dict
optimization_persistence_strategy_setting_dict = optimization_persistence_strategy_setting_instance.to_dict()
# create an instance of OptimizationPersistenceStrategySetting from a dict
optimization_persistence_strategy_setting_from_dict = OptimizationPersistenceStrategySetting.from_dict(optimization_persistence_strategy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


