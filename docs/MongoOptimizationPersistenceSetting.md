# MongoOptimizationPersistenceSetting

The mongoSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_persistence** | **bool** | The enablePersistence | 
**require_unique_ident_creator_combination** | **bool** | The requireUniqueIdentCreatorCombination | 
**secret** | **str** | The secret that encrypts the result. If empty, no encryption is assigned. Important: Metadata and stream information like progress is always saved as decrypted clear text. Attention: The secret is not saved by DNA evolutions. If you loose the secret, the file CAN NOT be restored. | 
**expiry** | **str** | The document will be automatically deleted after this duration. The default value is 48 hours. | [optional] 
**optimization_persistence_strategy_setting** | [**OptimizationPersistenceStrategySetting**](OptimizationPersistenceStrategySetting.md) |  | 
**stream_persistence_strategy_setting** | [**StreamPersistenceStrategySetting**](StreamPersistenceStrategySetting.md) |  | 
**completion_webhook_url** | **str** | Optional URL the server calls (POST) when the job completes or fails. The payload contains jobId, tenantId, status, and completedAt only — no optimization data. Leave empty to disable. URL validation is controlled by the server&#39;s webhook-validation policy: in strict mode (SaaS default) only public HTTPS URLs are accepted; in relaxed mode (on-premise) HTTP and private network addresses are also allowed; in none mode (local development) any URL is accepted. Loopback addresses (127.x, ::1) are always rejected. Validation is performed at submission time. | [optional] 
**completion_webhook_secret** | **str** | Optional secret used to sign the webhook payload with HMAC-SHA256. When provided, the server includes an X-JOpt-Signature header on every delivery in the form &#39;sha256&#x3D;&lt;hex&gt;&#39;. The receiver should compute the same HMAC over the raw request body and compare it using a constant-time comparison before trusting the payload. Leave empty to send unsigned webhooks. Unsigned webhooks are acceptable in trusted internal networks but are not recommended when the webhook URL is reachable from untrusted clients. | [optional] 

## Example

```python
from touroptimizer_py_client.models.mongo_optimization_persistence_setting import MongoOptimizationPersistenceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of MongoOptimizationPersistenceSetting from a JSON string
mongo_optimization_persistence_setting_instance = MongoOptimizationPersistenceSetting.from_json(json)
# print the JSON string representation of the object
print(MongoOptimizationPersistenceSetting.to_json())

# convert the object into a dict
mongo_optimization_persistence_setting_dict = mongo_optimization_persistence_setting_instance.to_dict()
# create an instance of MongoOptimizationPersistenceSetting from a dict
mongo_optimization_persistence_setting_from_dict = MongoOptimizationPersistenceSetting.from_dict(mongo_optimization_persistence_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


