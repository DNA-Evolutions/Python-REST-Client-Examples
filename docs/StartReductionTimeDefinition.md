# StartReductionTimeDefinition

The settings/defintion for the reduction time at the start of the route for non-pillar nodes. A reduction times allows the Resource to start working/driving before the actual official workingHours start. For example, a customer node opens at 8 in the morning and the resource needs 25 minutes to drive to the node. The official workingHour of the Resource start at 8 as well. By giving a maximal reduction time of, for example, one hour and only allow the reduction time to be used for driving, the Resource will start 25 minutes to earlier to reach the node by 8.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_route_start_reduction_time** | **str** | The maximal Routes&#39; Start Reduction Time for nodes the Optimizer is allowed to use. | 
**is_reduction_time_only_used_for_driving** | **bool** | The boolean isReductionTimeOnlyUsedForDriving defines if a Resource is allowed to use reduction time only for driving to the first node but not for working on it. | 

## Example

```python
from touroptimizer_py_client.models.start_reduction_time_definition import StartReductionTimeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StartReductionTimeDefinition from a JSON string
start_reduction_time_definition_instance = StartReductionTimeDefinition.from_json(json)
# print the JSON string representation of the object
print StartReductionTimeDefinition.to_json()

# convert the object into a dict
start_reduction_time_definition_dict = start_reduction_time_definition_instance.to_dict()
# create an instance of StartReductionTimeDefinition from a dict
start_reduction_time_definition_form_dict = start_reduction_time_definition.from_dict(start_reduction_time_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


