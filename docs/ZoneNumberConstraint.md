# ZoneNumberConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_codes** | [**List[ZoneNumber]**](ZoneNumber.md) | The zoneCodes | 
**type_name** | **str** | The typeName of the object | [default to 'ZoneNumberConstraint']

## Example

```python
from touroptimizer_py_client.models.zone_number_constraint import ZoneNumberConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneNumberConstraint from a JSON string
zone_number_constraint_instance = ZoneNumberConstraint.from_json(json)
# print the JSON string representation of the object
print ZoneNumberConstraint.to_json()

# convert the object into a dict
zone_number_constraint_dict = zone_number_constraint_instance.to_dict()
# create an instance of ZoneNumberConstraint from a dict
zone_number_constraint_form_dict = zone_number_constraint.from_dict(zone_number_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


