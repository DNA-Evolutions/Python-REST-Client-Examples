# QualificationType

A resource-side qualification that declares what skills, territories, or capabilities a resource offers. Matched against node-level constraints during optimization. Subtypes include type-based qualifications (with optional expertise levels), zone number and UK post code qualifications, and high-performance bitset-based type qualifications (with optional expertise).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.qualification_type import QualificationType

# TODO update the JSON string below
json = "{}"
# create an instance of QualificationType from a JSON string
qualification_type_instance = QualificationType.from_json(json)
# print the JSON string representation of the object
print(QualificationType.to_json())

# convert the object into a dict
qualification_type_dict = qualification_type_instance.to_dict()
# create an instance of QualificationType from a dict
qualification_type_from_dict = QualificationType.from_dict(qualification_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


