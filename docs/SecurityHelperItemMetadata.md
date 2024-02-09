# SecurityHelperItemMetadata

SecurityHelperItemMetadata model for encrypted data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iv** | **str** | The iv vector used for initiailization the encryption as base 64 encoded String. | 
**salt** | **str** | The salt used for initiailization as base 64 encoded String. | 
**enc_algo** | **str** | The algorithm used for encryption. | 
**secret_key_fac_algo** | **str** | Secret Key Factory algorithm. | 
**secret_key_spec_algo** | **str** | Secret Key Factory algorithm spec. | 

## Example

```python
from touroptimizer_py_client.models.security_helper_item_metadata import SecurityHelperItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityHelperItemMetadata from a JSON string
security_helper_item_metadata_instance = SecurityHelperItemMetadata.from_json(json)
# print the JSON string representation of the object
print SecurityHelperItemMetadata.to_json()

# convert the object into a dict
security_helper_item_metadata_dict = security_helper_item_metadata_instance.to_dict()
# create an instance of SecurityHelperItemMetadata from a dict
security_helper_item_metadata_form_dict = security_helper_item_metadata.from_dict(security_helper_item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


