# BitTypeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_names** | **List[str]** | A list of user-provided type-integer numbers. A Contraint type name must match to a Qualification type name to result in a violation free solution. | 
**type_name** | **str** | The typeName of the object | [default to 'BitType']

## Example

```python
from touroptimizer_py_client.models.bit_type_constraint import BitTypeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BitTypeConstraint from a JSON string
bit_type_constraint_instance = BitTypeConstraint.from_json(json)
# print the JSON string representation of the object
print(BitTypeConstraint.to_json())

# convert the object into a dict
bit_type_constraint_dict = bit_type_constraint_instance.to_dict()
# create an instance of BitTypeConstraint from a dict
bit_type_constraint_from_dict = BitTypeConstraint.from_dict(bit_type_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


