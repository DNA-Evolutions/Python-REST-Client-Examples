# UKPostCodeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_codes** | [**List[UKPostCode]**](UKPostCode.md) | The zoneCodes | 
**type_name** | **str** | The typeName of the object | [default to 'UKPostCodeConstraint']

## Example

```python
from touroptimizer_py_client.models.uk_post_code_constraint import UKPostCodeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of UKPostCodeConstraint from a JSON string
uk_post_code_constraint_instance = UKPostCodeConstraint.from_json(json)
# print the JSON string representation of the object
print UKPostCodeConstraint.to_json()

# convert the object into a dict
uk_post_code_constraint_dict = uk_post_code_constraint_instance.to_dict()
# create an instance of UKPostCodeConstraint from a dict
uk_post_code_constraint_form_dict = uk_post_code_constraint.from_dict(uk_post_code_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


