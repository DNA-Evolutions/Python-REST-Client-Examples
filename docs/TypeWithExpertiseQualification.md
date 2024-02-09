# TypeWithExpertiseQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types_with_expertise** | [**List[TypeWithExpertise]**](TypeWithExpertise.md) | A list of user-provided type-names and expertise levels. A Contraint type-name with its required expertise must be fulfill by the type-with-expertise Qualification to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'TypeWithExpertise']

## Example

```python
from touroptimizer_py_client.models.type_with_expertise_qualification import TypeWithExpertiseQualification

# TODO update the JSON string below
json = "{}"
# create an instance of TypeWithExpertiseQualification from a JSON string
type_with_expertise_qualification_instance = TypeWithExpertiseQualification.from_json(json)
# print the JSON string representation of the object
print TypeWithExpertiseQualification.to_json()

# convert the object into a dict
type_with_expertise_qualification_dict = type_with_expertise_qualification_instance.to_dict()
# create an instance of TypeWithExpertiseQualification from a dict
type_with_expertise_qualification_form_dict = type_with_expertise_qualification.from_dict(type_with_expertise_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


