# UKPostCodeQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_code** | [**UKPostCode**](UKPostCode.md) |  | 
**my_extra_codes** | [**List[UKPostCode]**](UKPostCode.md) | The myExtraCodes | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'UKPostCodeQualification']

## Example

```python
from touroptimizer_py_client.models.uk_post_code_qualification import UKPostCodeQualification

# TODO update the JSON string below
json = "{}"
# create an instance of UKPostCodeQualification from a JSON string
uk_post_code_qualification_instance = UKPostCodeQualification.from_json(json)
# print the JSON string representation of the object
print UKPostCodeQualification.to_json()

# convert the object into a dict
uk_post_code_qualification_dict = uk_post_code_qualification_instance.to_dict()
# create an instance of UKPostCodeQualification from a dict
uk_post_code_qualification_form_dict = uk_post_code_qualification.from_dict(uk_post_code_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


