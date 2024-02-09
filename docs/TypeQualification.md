# TypeQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_names** | **List[str]** | A list of user-provided type-names. A Contraint type name must match to a Qualification type name to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'Type']

## Example

```python
from touroptimizer_py_client.models.type_qualification import TypeQualification

# TODO update the JSON string below
json = "{}"
# create an instance of TypeQualification from a JSON string
type_qualification_instance = TypeQualification.from_json(json)
# print the JSON string representation of the object
print TypeQualification.to_json()

# convert the object into a dict
type_qualification_dict = type_qualification_instance.to_dict()
# create an instance of TypeQualification from a dict
type_qualification_form_dict = type_qualification.from_dict(type_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


