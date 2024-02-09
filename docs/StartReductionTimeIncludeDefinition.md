# StartReductionTimeIncludeDefinition

The settings/defintion for how to handle working time in the context of reduction time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_reduction_time_included_in_working_time** | **bool** | The boolean isReductionTimeIncludedInWorkingTime. If reduction time is used it can be either counted as part of the working time or not. | 

## Example

```python
from touroptimizer_py_client.models.start_reduction_time_include_definition import StartReductionTimeIncludeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StartReductionTimeIncludeDefinition from a JSON string
start_reduction_time_include_definition_instance = StartReductionTimeIncludeDefinition.from_json(json)
# print the JSON string representation of the object
print StartReductionTimeIncludeDefinition.to_json()

# convert the object into a dict
start_reduction_time_include_definition_dict = start_reduction_time_include_definition_instance.to_dict()
# create an instance of StartReductionTimeIncludeDefinition from a dict
start_reduction_time_include_definition_form_dict = start_reduction_time_include_definition.from_dict(start_reduction_time_include_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


