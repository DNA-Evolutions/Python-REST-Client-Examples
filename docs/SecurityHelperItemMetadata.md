# SecurityHelperItemMetadata

Cryptographic metadata stored alongside encrypted data in GridFS. Contains the IV, salt (CLIENT mode), algorithm identifiers, and in KMS mode the wrapped DEK and KEK identifier. Used to reconstruct the decryption key at retrieval time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enc_mode** | **str** | The encryption mode that was used. &#39;CLIENT&#39; &#x3D; key derived from a client passphrase via PBKDF2. &#39;KMS&#39; &#x3D; key is a server-generated DEK wrapped by an external KMS. Old metadata without this field defaults to CLIENT for backward compatibility. | [optional] 
**iv** | **str** | The IV used for AES-GCM initialization as base64-encoded String. Should be 12 bytes (96 bits) for GCM per NIST SP 800-38D. | 
**enc_algo** | **str** | The algorithm used for encryption. | 
**key_length** | **int** | AES key length in bits. | [optional] 
**salt** | **str** | The salt used for PBKDF2 key derivation as base64-encoded String. Only present in CLIENT mode. Empty in KMS mode. | [optional] 
**secret_key_fac_algo** | **str** | Secret Key Factory algorithm. Only used in CLIENT mode. | [optional] 
**secret_key_spec_algo** | **str** | Secret Key Spec algorithm. | [optional] 
**iteration_count** | **int** | PBKDF2 iteration count. Only used in CLIENT mode. Old snapshots without this field used 65536. KMS mode sets this to 0. | [optional] 
**wrapped_dek** | **str** | The data encryption key (DEK) wrapped (encrypted) by the tenant&#39;s key encryption key (KEK) via an external KMS, stored as a base64-encoded String. Only present in KMS mode. The plaintext DEK is never stored it must be unwrapped via the KMS before decryption. | [optional] 
**kek_id** | **str** | The identifier (URI or ARN) of the key encryption key (KEK) in the external KMS that was used to wrap the DEK. Only present in KMS mode. Required for unwrapping the DEK at retrieval time. Example for Azure Key Vault: &#39;https://myvault.vault.azure.net/keys/tenant-kek/abc123&#39;. Example for AWS KMS: &#39;arn:aws:kms:eu-west-1:123456789:key/mrk-abc123&#39;. | [optional] 
**kms_mode** | **bool** | Convenience flag derived from encMode. True when encMode is KMS, false for CLIENT mode or legacy documents without an encMode field. | [optional] 

## Example

```python
from touroptimizer_py_client.models.security_helper_item_metadata import SecurityHelperItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityHelperItemMetadata from a JSON string
security_helper_item_metadata_instance = SecurityHelperItemMetadata.from_json(json)
# print the JSON string representation of the object
print(SecurityHelperItemMetadata.to_json())

# convert the object into a dict
security_helper_item_metadata_dict = security_helper_item_metadata_instance.to_dict()
# create an instance of SecurityHelperItemMetadata from a dict
security_helper_item_metadata_from_dict = SecurityHelperItemMetadata.from_dict(security_helper_item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


