# StayOutDefinition

Defines overnight-stay policies for this resource, including the maximum total number of stay-outs permitted, the maximum consecutive stay-outs in a row, and the minimum recovery period between stay-out sequences. Used in multi-day planning scenarios where resources may stay overnight near their last stop.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_total_stays_out** | **int** | The maximum total number of overnight stays the resource may have across all working-hour cycles. | 
**max_stays_out_in_row** | **int** | The maximum number of consecutive overnight stays in a row before the resource must return home or observe a recovery period. | 
**min_recovery** | **str** | The minimum recovery duration the resource must spend at its home location before another stay-out sequence is permitted. Expressed as an ISO 8601 duration (e.g. &#39;PT24H&#39; for one full day). | 

## Example

```python
from touroptimizer_py_client.models.stay_out_definition import StayOutDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StayOutDefinition from a JSON string
stay_out_definition_instance = StayOutDefinition.from_json(json)
# print the JSON string representation of the object
print(StayOutDefinition.to_json())

# convert the object into a dict
stay_out_definition_dict = stay_out_definition_instance.to_dict()
# create an instance of StayOutDefinition from a dict
stay_out_definition_from_dict = StayOutDefinition.from_dict(stay_out_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


