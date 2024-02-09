# Qualification

The qualifications of the Resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QualificationType**](QualificationType.md) |  | 

## Example

```python
from touroptimizer_py_client.models.qualification import Qualification

# TODO update the JSON string below
json = "{}"
# create an instance of Qualification from a JSON string
qualification_instance = Qualification.from_json(json)
# print the JSON string representation of the object
print Qualification.to_json()

# convert the object into a dict
qualification_dict = qualification_instance.to_dict()
# create an instance of Qualification from a dict
qualification_form_dict = qualification.from_dict(qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


