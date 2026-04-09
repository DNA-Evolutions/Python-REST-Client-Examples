# IntegerMultiConstraintHelperItem

The mirroring configuration that maps this constraint across working-hour boundaries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pairs** | [**List[StringIntegerPair]**](StringIntegerPair.md) | A list of key-value pairs mapping element identifiers to integer values. Used internally to mirror multi-route constraint configurations across working hours. | 

## Example

```python
from touroptimizer_py_client.models.integer_multi_constraint_helper_item import IntegerMultiConstraintHelperItem

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerMultiConstraintHelperItem from a JSON string
integer_multi_constraint_helper_item_instance = IntegerMultiConstraintHelperItem.from_json(json)
# print the JSON string representation of the object
print(IntegerMultiConstraintHelperItem.to_json())

# convert the object into a dict
integer_multi_constraint_helper_item_dict = integer_multi_constraint_helper_item_instance.to_dict()
# create an instance of IntegerMultiConstraintHelperItem from a dict
integer_multi_constraint_helper_item_from_dict = IntegerMultiConstraintHelperItem.from_dict(integer_multi_constraint_helper_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


