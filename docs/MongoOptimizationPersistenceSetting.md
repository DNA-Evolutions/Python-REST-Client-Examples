# MongoOptimizationPersistenceSetting

The mongoSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_persistence** | **bool** | The enablePersistence | 
**secret** | **str** | The secret that encrypts the result. If empty, no encryption is assigned. Important: Metadata and stream information like progress is always saved as decrypted clear text. Attention: The secret is not saved by DNA evolutions. If you loose the secret, the file CAN NOT be restored. | 
**expiry** | **str** | The document will be automatically deleted after this duration. The default value is 48 hours. | [optional] 
**optimization_persistence_stratgy_setting** | [**OptimizationPersistenceStratgySetting**](OptimizationPersistenceStratgySetting.md) |  | 
**stream_persistence_stratgy_setting** | [**StreamPersistenceStratgySetting**](StreamPersistenceStratgySetting.md) |  | 

## Example

```python
from touroptimizer_py_client.models.mongo_optimization_persistence_setting import MongoOptimizationPersistenceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of MongoOptimizationPersistenceSetting from a JSON string
mongo_optimization_persistence_setting_instance = MongoOptimizationPersistenceSetting.from_json(json)
# print the JSON string representation of the object
print MongoOptimizationPersistenceSetting.to_json()

# convert the object into a dict
mongo_optimization_persistence_setting_dict = mongo_optimization_persistence_setting_instance.to_dict()
# create an instance of MongoOptimizationPersistenceSetting from a dict
mongo_optimization_persistence_setting_form_dict = mongo_optimization_persistence_setting.from_dict(mongo_optimization_persistence_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


