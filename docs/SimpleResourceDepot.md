# SimpleResourceDepot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximal_unit_matched_capacity** | **float** | The maximal unit matched total capacity of the depot. | 
**capacity_unit_map** | **Dict[str, float]** | The capacityUnitMap of the depot. | [optional] 
**per_kilometer_cost_factor_map** | **Dict[str, int]** | The perKilometerCostFactorMap of the depot. | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'SimpleResourceDepot']
**empty_at_end_of_route_factor_map** | **Dict[str, int]** | The emptyAtEndOfRouteFactorMap of the depot. | [optional] 

## Example

```python
from touroptimizer_py_client.models.simple_resource_depot import SimpleResourceDepot

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleResourceDepot from a JSON string
simple_resource_depot_instance = SimpleResourceDepot.from_json(json)
# print the JSON string representation of the object
print SimpleResourceDepot.to_json()

# convert the object into a dict
simple_resource_depot_dict = simple_resource_depot_instance.to_dict()
# create an instance of SimpleResourceDepot from a dict
simple_resource_depot_form_dict = simple_resource_depot.from_dict(simple_resource_depot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


