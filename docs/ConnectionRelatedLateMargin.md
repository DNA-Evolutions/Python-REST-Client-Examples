# ConnectionRelatedLateMargin

The connectionRelatedLateMargin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_element_connection_realted_late_margin** | **bool** | The isDoElementShiftConnectionRealtedLateMargin | [optional] 
**apply_partial_connection_related_late_margin** | **bool** | The applyPartialConnectionRelatedLateMargin | [optional] 
**max_margin** | **str** | The maxMargin | 
**margin_factor** | **float** | The marginFactor between 0 (inclusive) and 1 (inclusive) | 

## Example

```python
from touroptimizer_py_client.models.connection_related_late_margin import ConnectionRelatedLateMargin

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRelatedLateMargin from a JSON string
connection_related_late_margin_instance = ConnectionRelatedLateMargin.from_json(json)
# print the JSON string representation of the object
print ConnectionRelatedLateMargin.to_json()

# convert the object into a dict
connection_related_late_margin_dict = connection_related_late_margin_instance.to_dict()
# create an instance of ConnectionRelatedLateMargin from a dict
connection_related_late_margin_form_dict = connection_related_late_margin.from_dict(connection_related_late_margin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


