# BitTypeWithExpertiseConstraint

A bitset-based skill constraint with expertise levels on nodes. Each required type maps to a TypeLevelRequirement specifying the minimum expertise level. Supports cost models that penalize over- or under-qualified assignments. Matched against BitTypeWithExpertiseQualification on resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dict_type_names** | **List[str]** | A list of user-provided dict type-names. Those values will be mapped. | [optional] 
**dict_mapping** | [**Dict[str, TypeLevelRequirement]**](TypeLevelRequirement.md) | The mapping of a certain type. or multiple types | [optional] 
**info_cost_model** | **str** | The cost model for matching the expertise. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'BitTypeWithExpertise']
**is_hard_level** | **bool** | Defines if a level of a cosntraint is soft contrained or hard constraint. A hard constraint is fullfilled by the architectural design of the Optimzer. Therefore a hard constraint violation cannot occure. However, not all constraints can be hard-constraint- | 

## Example

```python
from touroptimizer_py_client.models.bit_type_with_expertise_constraint import BitTypeWithExpertiseConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BitTypeWithExpertiseConstraint from a JSON string
bit_type_with_expertise_constraint_instance = BitTypeWithExpertiseConstraint.from_json(json)
# print the JSON string representation of the object
print(BitTypeWithExpertiseConstraint.to_json())

# convert the object into a dict
bit_type_with_expertise_constraint_dict = bit_type_with_expertise_constraint_instance.to_dict()
# create an instance of BitTypeWithExpertiseConstraint from a dict
bit_type_with_expertise_constraint_from_dict = BitTypeWithExpertiseConstraint.from_dict(bit_type_with_expertise_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


