# UKPostCode

A UK postcode zone code with hierarchical components: area identifier (e.g. 'SW'), optional district number, optional sector number, and optional unit identifier. Used for UK-specific territory partitioning in zone-based routing constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_ident** | **str** | The area identifier of the UK postcode (e.g. &#39;SW&#39;, &#39;EC&#39;, &#39;M&#39;). This is the outward code&#39;s letter prefix that identifies the postal area. | 
**district_ident_opt** | **int** | The optional district number within the postal area (e.g. 1 in &#39;SW1&#39;). | [optional] 
**sector_ident_opt** | **int** | The optional sector number from the inward code (e.g. 4 in &#39;SW1A 4&#39;). | [optional] 
**unit_ident_opt** | **str** | The optional unit identifier from the inward code (e.g. &#39;AA&#39; in &#39;SW1A 4AA&#39;). | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'UKPostCode']

## Example

```python
from touroptimizer_py_client.models.uk_post_code import UKPostCode

# TODO update the JSON string below
json = "{}"
# create an instance of UKPostCode from a JSON string
uk_post_code_instance = UKPostCode.from_json(json)
# print the JSON string representation of the object
print(UKPostCode.to_json())

# convert the object into a dict
uk_post_code_dict = uk_post_code_instance.to_dict()
# create an instance of UKPostCode from a dict
uk_post_code_from_dict = UKPostCode.from_dict(uk_post_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


