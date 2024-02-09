# StartReductionTimePillarDefinition

The settings/defintion for the reduction time at the start of the route for pillar nodes. Please see startReductionTimeDefinition for details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_route_start_reduction_time_pillar** | **str** | The maximal Routes&#39; Start Reduction Time for pillars nodes the Optimizer is allowed to use. | 
**is_reduction_time_only_used_for_driving_pillar** | **bool** | The boolean isReductionTimeOnlyUsedForDriving defines if a Resource is allowed to use reduction time only for driving to the first node (here a pillar) but not for working on it. | 

## Example

```python
from touroptimizer_py_client.models.start_reduction_time_pillar_definition import StartReductionTimePillarDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StartReductionTimePillarDefinition from a JSON string
start_reduction_time_pillar_definition_instance = StartReductionTimePillarDefinition.from_json(json)
# print the JSON string representation of the object
print StartReductionTimePillarDefinition.to_json()

# convert the object into a dict
start_reduction_time_pillar_definition_dict = start_reduction_time_pillar_definition_instance.to_dict()
# create an instance of StartReductionTimePillarDefinition from a dict
start_reduction_time_pillar_definition_form_dict = start_reduction_time_pillar_definition.from_dict(start_reduction_time_pillar_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


