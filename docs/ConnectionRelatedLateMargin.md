# ConnectionRelatedLateMargin

Configures a distance- or time-proportional late-arrival tolerance for a pillar node. If the inbound connection is long, the optimizer grants a proportional margin before counting lateness as a violation. Useful for fixed appointments where minor lateness is acceptable when traveling from distant locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_element_connection_realted_late_margin** | **bool** | If true, the optimizer shifts the element&#39;s effective time window by the computed late margin, rather than simply absorbing the lateness as a soft violation. Produces a cleaner schedule representation. | [optional] 
**apply_partial_connection_related_late_margin** | **bool** | If true, partial late margins are applied proportionally based on the actual connection time relative to the maximum margin. If false, the full margin is applied as a binary threshold. | [optional] 
**max_margin** | **str** | The maximum late-arrival margin that can be granted, regardless of how long the inbound connection is. Caps the proportional margin to prevent excessively permissive lateness tolerance. | 
**margin_factor** | **float** | A factor between 0.0 and 1.0 that determines what proportion of the inbound connection time is granted as late-arrival margin. For example, a factor of 0.2 on a 50-minute connection yields a 10-minute margin (capped by maxMargin). | 

## Example

```python
from touroptimizer_py_client.models.connection_related_late_margin import ConnectionRelatedLateMargin

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRelatedLateMargin from a JSON string
connection_related_late_margin_instance = ConnectionRelatedLateMargin.from_json(json)
# print the JSON string representation of the object
print(ConnectionRelatedLateMargin.to_json())

# convert the object into a dict
connection_related_late_margin_dict = connection_related_late_margin_instance.to_dict()
# create an instance of ConnectionRelatedLateMargin from a dict
connection_related_late_margin_from_dict = ConnectionRelatedLateMargin.from_dict(connection_related_late_margin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


