# IResourceDepot

A resource-level depot that defines the initial goods/capacity a resource carries at route start. Holds a collection of load capacities and manages load exchange when visiting node depots during pickup-and-delivery scenarios.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ILoadCapacity]**](ILoadCapacity.md) |  | [optional] 
**maximal_total_capacity** | **float** |  | [optional] 
**depot_id** | **str** |  | [optional] 
**capacity_unit_map** | **Dict[str, float]** |  | [optional] 
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.i_resource_depot import IResourceDepot

# TODO update the JSON string below
json = "{}"
# create an instance of IResourceDepot from a JSON string
i_resource_depot_instance = IResourceDepot.from_json(json)
# print the JSON string representation of the object
print(IResourceDepot.to_json())

# convert the object into a dict
i_resource_depot_dict = i_resource_depot_instance.to_dict()
# create an instance of IResourceDepot from a dict
i_resource_depot_from_dict = IResourceDepot.from_dict(i_resource_depot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


