# PillarType

A pillar (anchored/captured) node that is locked to a specific resource and cannot be reassigned during optimization. Subtypes include geo-pillar nodes (with latitude/longitude) and event-pillar nodes (non-geographical tasks).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.pillar_type import PillarType

# TODO update the JSON string below
json = "{}"
# create an instance of PillarType from a JSON string
pillar_type_instance = PillarType.from_json(json)
# print the JSON string representation of the object
print(PillarType.to_json())

# convert the object into a dict
pillar_type_dict = pillar_type_instance.to_dict()
# create an instance of PillarType from a dict
pillar_type_from_dict = PillarType.from_dict(pillar_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


