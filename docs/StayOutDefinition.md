# StayOutDefinition

The stayOutDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_total_stays_out** | **int** | The maxTotalStaysOut | 
**max_stays_out_in_row** | **int** | The maxStaysOutInRow | 
**min_recovery** | **str** | The minRecovery | 

## Example

```python
from touroptimizer_py_client.models.stay_out_definition import StayOutDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StayOutDefinition from a JSON string
stay_out_definition_instance = StayOutDefinition.from_json(json)
# print the JSON string representation of the object
print StayOutDefinition.to_json()

# convert the object into a dict
stay_out_definition_dict = stay_out_definition_instance.to_dict()
# create an instance of StayOutDefinition from a dict
stay_out_definition_form_dict = stay_out_definition.from_dict(stay_out_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


