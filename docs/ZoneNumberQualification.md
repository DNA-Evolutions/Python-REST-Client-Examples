# ZoneNumberQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_extra_codes** | [**List[ZoneNumber]**](ZoneNumber.md) | The myExtraCodes | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'ZoneNumberQualification']

## Example

```python
from touroptimizer_py_client.models.zone_number_qualification import ZoneNumberQualification

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneNumberQualification from a JSON string
zone_number_qualification_instance = ZoneNumberQualification.from_json(json)
# print the JSON string representation of the object
print ZoneNumberQualification.to_json()

# convert the object into a dict
zone_number_qualification_dict = zone_number_qualification_instance.to_dict()
# create an instance of ZoneNumberQualification from a dict
zone_number_qualification_form_dict = zone_number_qualification.from_dict(zone_number_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


