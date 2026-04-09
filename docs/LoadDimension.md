# LoadDimension

The load dimension descriptor for pickup-and-delivery (PND) scenarios. Defines how loads are interpreted at this node — for example, whether goods are picked up from or delivered to this location, and how the load interacts with the resource's capacity vector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unload_all_dimension** | **int** | The number of load dimensions that participate in the unload-all operation. For example, if the resource carries goods across 3 dimensions (weight, volume, pallets) and unloadAllDimension is set to 2, only the first 2 dimensions are emptied at this node. | 
**total_load_dimension** | **int** | The total number of load dimensions defined for this node. Must match the dimensionality of the resource&#39;s capacity vector and the node&#39;s load vector. | 
**unload_all** | **bool** | If true, the resource unloads all remaining cargo at this node before continuing. Typically used at depot-return nodes or redistribution hubs in PND scenarios. | [optional] 

## Example

```python
from touroptimizer_py_client.models.load_dimension import LoadDimension

# TODO update the JSON string below
json = "{}"
# create an instance of LoadDimension from a JSON string
load_dimension_instance = LoadDimension.from_json(json)
# print the JSON string representation of the object
print(LoadDimension.to_json())

# convert the object into a dict
load_dimension_dict = load_dimension_instance.to_dict()
# create an instance of LoadDimension from a dict
load_dimension_from_dict = LoadDimension.from_dict(load_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


