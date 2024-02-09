# TimeWindowNodeRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_time_deviation** | **str** | The minTimeDeviation defines the minimal time of the relation. | 
**max_time_deviation** | **str** | The maxTimeDeviation defines the minimal time of the relation. | 
**time_comparison_juncture** | [**TimeComparisonJuncture**](TimeComparisonJuncture.md) |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'TimeWindow']

## Example

```python
from touroptimizer_py_client.models.time_window_node_relation import TimeWindowNodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindowNodeRelation from a JSON string
time_window_node_relation_instance = TimeWindowNodeRelation.from_json(json)
# print the JSON string representation of the object
print TimeWindowNodeRelation.to_json()

# convert the object into a dict
time_window_node_relation_dict = time_window_node_relation_instance.to_dict()
# create an instance of TimeWindowNodeRelation from a dict
time_window_node_relation_form_dict = time_window_node_relation.from_dict(time_window_node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


