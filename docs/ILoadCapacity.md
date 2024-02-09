# ILoadCapacity

The LoadCapacity type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_pickup_time** | **int** |  | [optional] 
**current_load** | **float** |  | [optional] 
**maximal_individual_load_capacity** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.i_load_capacity import ILoadCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of ILoadCapacity from a JSON string
i_load_capacity_instance = ILoadCapacity.from_json(json)
# print the JSON string representation of the object
print ILoadCapacity.to_json()

# convert the object into a dict
i_load_capacity_dict = i_load_capacity_instance.to_dict()
# create an instance of ILoadCapacity from a dict
i_load_capacity_form_dict = i_load_capacity.from_dict(i_load_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


