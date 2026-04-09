# StayOutCycleDefinition

Defines the repeating cycle within which stay-out limits are evaluated. For example, a 7-day cycle starting on a specific date allows the optimizer to count stay-outs per week and enforce weekly limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_length** | **str** | The length of one stay-out evaluation cycle, expressed as an ISO 8601 duration (e.g. &#39;PT7D&#39; for one week). | 
**cycle_start** | **date** | The start date of the first stay-out evaluation cycle. Subsequent cycles begin at cycleStart + N * cycleLength. | 

## Example

```python
from touroptimizer_py_client.models.stay_out_cycle_definition import StayOutCycleDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StayOutCycleDefinition from a JSON string
stay_out_cycle_definition_instance = StayOutCycleDefinition.from_json(json)
# print the JSON string representation of the object
print(StayOutCycleDefinition.to_json())

# convert the object into a dict
stay_out_cycle_definition_dict = stay_out_cycle_definition_instance.to_dict()
# create an instance of StayOutCycleDefinition from a dict
stay_out_cycle_definition_from_dict = StayOutCycleDefinition.from_dict(stay_out_cycle_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


