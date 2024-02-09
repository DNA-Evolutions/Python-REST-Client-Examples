# TimeComparisonJuncture

The timeComparisonJuncture of the relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_master_node_working_start** | **bool** | Defines if the master nodes start is used as comparison point (true). If false, the end of the master node will be used. | 
**is_related_node_working_start** | **bool** | Defines if the related nodes start is used as comparison point (true). If false, the end of the related node will be used. | 

## Example

```python
from touroptimizer_py_client.models.time_comparison_juncture import TimeComparisonJuncture

# TODO update the JSON string below
json = "{}"
# create an instance of TimeComparisonJuncture from a JSON string
time_comparison_juncture_instance = TimeComparisonJuncture.from_json(json)
# print the JSON string representation of the object
print TimeComparisonJuncture.to_json()

# convert the object into a dict
time_comparison_juncture_dict = time_comparison_juncture_instance.to_dict()
# create an instance of TimeComparisonJuncture from a dict
time_comparison_juncture_form_dict = time_comparison_juncture.from_dict(time_comparison_juncture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


