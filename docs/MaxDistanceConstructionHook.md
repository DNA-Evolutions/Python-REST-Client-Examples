# MaxDistanceConstructionHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The typeName of the object | [default to 'MaxDistanceConstructionHook']
**prioritize_node_connector_on_fallback_speed** | **bool** | In case the route to be used to calculate the average speed is empty, we need to calculate a fallback speed. By default we take the average speed provided by the resource. However, we can also extract a few connections from node connector that belong to the visiting resource of the route and calculated an average speed. | 
**only_apply_once** | **bool** | If only applied once, the hook is autmatically set to be inactive after one execution. | 
**invocation_position** | **str** | When is the hook incorporated? | 
**driven_time** | **str** | The offset for driven time. This time will be transformed into a distance (utilizing average resource speed) that is substracted from the defined maxdistance. | 
**driven_distance** | **str** | The offset for driven distance. This value is substracted from the defined maxdistance. | 
**is_active** | **bool** | Is the hook active? | 

## Example

```python
from touroptimizer_py_client.models.max_distance_construction_hook import MaxDistanceConstructionHook

# TODO update the JSON string below
json = "{}"
# create an instance of MaxDistanceConstructionHook from a JSON string
max_distance_construction_hook_instance = MaxDistanceConstructionHook.from_json(json)
# print the JSON string representation of the object
print(MaxDistanceConstructionHook.to_json())

# convert the object into a dict
max_distance_construction_hook_dict = max_distance_construction_hook_instance.to_dict()
# create an instance of MaxDistanceConstructionHook from a dict
max_distance_construction_hook_from_dict = MaxDistanceConstructionHook.from_dict(max_distance_construction_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


