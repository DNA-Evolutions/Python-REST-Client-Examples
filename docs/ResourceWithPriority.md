# ResourceWithPriority

The list of resources that should NOT visit a certain node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resourceId that will be part of a constraint. For example, Jack is a preffered Resource of a node. If multiple resources are preferred, the Optimizer tries to schedule the Resource with the highest priority. | 
**priority** | **int** | The priority | 

## Example

```python
from touroptimizer_py_client.models.resource_with_priority import ResourceWithPriority

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceWithPriority from a JSON string
resource_with_priority_instance = ResourceWithPriority.from_json(json)
# print the JSON string representation of the object
print ResourceWithPriority.to_json()

# convert the object into a dict
resource_with_priority_dict = resource_with_priority_instance.to_dict()
# create an instance of ResourceWithPriority from a dict
resource_with_priority_form_dict = resource_with_priority.from_dict(resource_with_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


