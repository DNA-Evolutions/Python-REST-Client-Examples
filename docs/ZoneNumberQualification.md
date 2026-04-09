# ZoneNumberQualification

A resource qualification declaring which numeric zone territories the resource is authorized to operate in. Matched against ZoneNumberConstraint on nodes to enforce territory assignments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_code** | [**ZoneCodeType**](ZoneCodeType.md) |  | [optional] 
**my_extra_codes** | [**List[ZoneCodeType]**](ZoneCodeType.md) | Additional zone codes this resource is also qualified to serve, beyond the primary code. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'ZoneNumberQualification']

## Example

```python
from touroptimizer_py_client.models.zone_number_qualification import ZoneNumberQualification

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneNumberQualification from a JSON string
zone_number_qualification_instance = ZoneNumberQualification.from_json(json)
# print the JSON string representation of the object
print(ZoneNumberQualification.to_json())

# convert the object into a dict
zone_number_qualification_dict = zone_number_qualification_instance.to_dict()
# create an instance of ZoneNumberQualification from a dict
zone_number_qualification_from_dict = ZoneNumberQualification.from_dict(zone_number_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


