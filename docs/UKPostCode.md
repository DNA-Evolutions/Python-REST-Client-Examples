# UKPostCode

The myExtraCodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_ident** | **str** | The areaIdent | 
**district_ident_opt** | **int** | The districtIdentOpt | [optional] 
**sector_ident_opt** | **int** | The sectorIdentOpt | [optional] 
**unit_ident_opt** | **str** | The unitIdentOpt | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'UKPostCode']

## Example

```python
from touroptimizer_py_client.models.uk_post_code import UKPostCode

# TODO update the JSON string below
json = "{}"
# create an instance of UKPostCode from a JSON string
uk_post_code_instance = UKPostCode.from_json(json)
# print the JSON string representation of the object
print UKPostCode.to_json()

# convert the object into a dict
uk_post_code_dict = uk_post_code_instance.to_dict()
# create an instance of UKPostCode from a dict
uk_post_code_form_dict = uk_post_code.from_dict(uk_post_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


