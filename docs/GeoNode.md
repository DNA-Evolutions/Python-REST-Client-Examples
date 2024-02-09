# GeoNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**Position**](Position.md) |  | 
**pillar_node** | [**GeoPillarNode**](GeoPillarNode.md) |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'Geo']

## Example

```python
from touroptimizer_py_client.models.geo_node import GeoNode

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNode from a JSON string
geo_node_instance = GeoNode.from_json(json)
# print the JSON string representation of the object
print GeoNode.to_json()

# convert the object into a dict
geo_node_dict = geo_node_instance.to_dict()
# create an instance of GeoNode from a dict
geo_node_form_dict = geo_node.from_dict(geo_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


