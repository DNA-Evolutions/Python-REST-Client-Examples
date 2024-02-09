# ZoneNumber

The myExtraCodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_number** | **int** | The zoneNumber | 
**type_name** | **str** | The typeName of the object | [default to 'ZoneNumber']

## Example

```python
from touroptimizer_py_client.models.zone_number import ZoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneNumber from a JSON string
zone_number_instance = ZoneNumber.from_json(json)
# print the JSON string representation of the object
print ZoneNumber.to_json()

# convert the object into a dict
zone_number_dict = zone_number_instance.to_dict()
# create an instance of ZoneNumber from a dict
zone_number_form_dict = zone_number.from_dict(zone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


