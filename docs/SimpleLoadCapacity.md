# SimpleLoadCapacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_capacity_id** | **str** |  | [optional] 
**max_capacity_value** | **int** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'SimpleLoadCapacity']

## Example

```python
from touroptimizer_py_client.models.simple_load_capacity import SimpleLoadCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleLoadCapacity from a JSON string
simple_load_capacity_instance = SimpleLoadCapacity.from_json(json)
# print the JSON string representation of the object
print SimpleLoadCapacity.to_json()

# convert the object into a dict
simple_load_capacity_dict = simple_load_capacity_instance.to_dict()
# create an instance of SimpleLoadCapacity from a dict
simple_load_capacity_form_dict = simple_load_capacity.from_dict(simple_load_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


