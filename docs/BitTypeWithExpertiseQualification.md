# BitTypeWithExpertiseQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dict_type_names** | **List[str]** | A list of user-provided dict type-names. Those values will be mapped. | [optional] 
**dict_mapping** | [**Dict[str, TypeLevelOffering]**](TypeLevelOffering.md) | The mapping of a certain type. or multiple types | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'BitTypeWithExpertise']

## Example

```python
from touroptimizer_py_client.models.bit_type_with_expertise_qualification import BitTypeWithExpertiseQualification

# TODO update the JSON string below
json = "{}"
# create an instance of BitTypeWithExpertiseQualification from a JSON string
bit_type_with_expertise_qualification_instance = BitTypeWithExpertiseQualification.from_json(json)
# print the JSON string representation of the object
print(BitTypeWithExpertiseQualification.to_json())

# convert the object into a dict
bit_type_with_expertise_qualification_dict = bit_type_with_expertise_qualification_instance.to_dict()
# create an instance of BitTypeWithExpertiseQualification from a dict
bit_type_with_expertise_qualification_from_dict = BitTypeWithExpertiseQualification.from_dict(bit_type_with_expertise_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


