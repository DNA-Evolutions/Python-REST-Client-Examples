# StayOutCycleDefinition

The stayOutCycleDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_lenght** | **str** | The cycleLenght | 
**cycle_start** | **date** | The cycleStart | 

## Example

```python
from touroptimizer_py_client.models.stay_out_cycle_definition import StayOutCycleDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StayOutCycleDefinition from a JSON string
stay_out_cycle_definition_instance = StayOutCycleDefinition.from_json(json)
# print the JSON string representation of the object
print StayOutCycleDefinition.to_json()

# convert the object into a dict
stay_out_cycle_definition_dict = stay_out_cycle_definition_instance.to_dict()
# create an instance of StayOutCycleDefinition from a dict
stay_out_cycle_definition_form_dict = stay_out_cycle_definition.from_dict(stay_out_cycle_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


