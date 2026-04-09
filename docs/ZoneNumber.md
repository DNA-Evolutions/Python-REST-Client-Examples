# ZoneNumber

A numeric zone code assigned to nodes and resources for territory-based routing. Zone numbers define geographic partitions and are used with ZoneConnections to penalize or restrict zone crossings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_number** | **int** | The numeric zone identifier assigned to this element. Zone numbers are used to define geographic territories for resources and to penalize or restrict zone crossings between nodes via ZoneConnections. | 
**type_name** | **str** | The typeName of the object | [default to 'ZoneNumber']

## Example

```python
from touroptimizer_py_client.models.zone_number import ZoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneNumber from a JSON string
zone_number_instance = ZoneNumber.from_json(json)
# print the JSON string representation of the object
print(ZoneNumber.to_json())

# convert the object into a dict
zone_number_dict = zone_number_instance.to_dict()
# create an instance of ZoneNumber from a dict
zone_number_from_dict = ZoneNumber.from_dict(zone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


