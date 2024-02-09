# INodeDepot

The NodeDepot type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ILoad]**](ILoad.md) |  | [optional] 
**depot_id** | **str** |  | [optional] 
**has_timed_loads** | **bool** |  | [optional] 
**has_flex_load** | **bool** |  | [optional] 
**type_name** | **str** |  | 

## Example

```python
from touroptimizer_py_client.models.i_node_depot import INodeDepot

# TODO update the JSON string below
json = "{}"
# create an instance of INodeDepot from a JSON string
i_node_depot_instance = INodeDepot.from_json(json)
# print the JSON string representation of the object
print INodeDepot.to_json()

# convert the object into a dict
i_node_depot_dict = i_node_depot_instance.to_dict()
# create an instance of INodeDepot from a dict
i_node_depot_form_dict = i_node_depot.from_dict(i_node_depot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


