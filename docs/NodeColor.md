# NodeColor

The nodeColor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_code** | **int** | The colorCode | 
**color_id** | **str** | The colorId | 
**count_value** | **int** | The countValue | [optional] 

## Example

```python
from touroptimizer_py_client.models.node_color import NodeColor

# TODO update the JSON string below
json = "{}"
# create an instance of NodeColor from a JSON string
node_color_instance = NodeColor.from_json(json)
# print the JSON string representation of the object
print NodeColor.to_json()

# convert the object into a dict
node_color_dict = node_color_instance.to_dict()
# create an instance of NodeColor from a dict
node_color_form_dict = node_color.from_dict(node_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


