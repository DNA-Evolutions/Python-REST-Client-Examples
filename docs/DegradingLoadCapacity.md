# DegradingLoadCapacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_capacity_id** | **str** |  | [optional] 
**max_capacity_value** | **int** |  | [optional] 
**capacity_degradation_per_stop** | **float** |  | [optional] 
**minimal_tota_degradated_capacity** | **float** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'DegradingLoadCapacity']

## Example

```python
from touroptimizer_py_client.models.degrading_load_capacity import DegradingLoadCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of DegradingLoadCapacity from a JSON string
degrading_load_capacity_instance = DegradingLoadCapacity.from_json(json)
# print the JSON string representation of the object
print DegradingLoadCapacity.to_json()

# convert the object into a dict
degrading_load_capacity_dict = degrading_load_capacity_instance.to_dict()
# create an instance of DegradingLoadCapacity from a dict
degrading_load_capacity_form_dict = degrading_load_capacity.from_dict(degrading_load_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


