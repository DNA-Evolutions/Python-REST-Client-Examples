# BitTypeQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_names** | **List[str]** | A list of user-provided type-names. A Contraint type name must match to a Qualification type number (integer) to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'BitType']

## Example

```python
from touroptimizer_py_client.models.bit_type_qualification import BitTypeQualification

# TODO update the JSON string below
json = "{}"
# create an instance of BitTypeQualification from a JSON string
bit_type_qualification_instance = BitTypeQualification.from_json(json)
# print the JSON string representation of the object
print(BitTypeQualification.to_json())

# convert the object into a dict
bit_type_qualification_dict = bit_type_qualification_instance.to_dict()
# create an instance of BitTypeQualification from a dict
bit_type_qualification_from_dict = BitTypeQualification.from_dict(bit_type_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


