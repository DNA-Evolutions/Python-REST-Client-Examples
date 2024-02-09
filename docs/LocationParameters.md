# LocationParameters

Location parameters that can support geographical routing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layers** | **str** | The layers in which the location can be detected. Use &#39;auto&#39; for automatically selecting the best (highest confidence) layer. | [optional] 
**size** | **int** | The number of layers the location can be related to. Further, in case of a query the number of results that might be found/desired. | [optional] 
**radius** | **float** | The number of meters about this input location within which edges (roads between intersections) will be considered as candidates for said location. When correlating this location to the route network, try to only return results within this distance (meters) from this location. If there are no candidates within this distance it will return the closest candidate within reason. If this value is larger than the configured service limit it will be clamped to that limit. The default is 20 meters. | [optional] 
**sources** | **str** | If you use the sources parameter, you can choose which of these data sources to include in your search. So if you&#39;re only interested in finding an address in data from OpenAddresses, for example, you can build a query specifying that data source &#39;oa&#39;. (OpenAddresses&#x3D;&#39;oa&#39;, OpenstreetMap &#x3D; &#39;osm&#39;, Who&#39;s on First &#x3D;&#39;wof&#39;,GeoNames&#x3D;&#39;gn&#39; ). If, for example, OpenAddresses and OpenstreetMap is desired use &#39;osm,oa&#39;. Default is &#39;all&#39;  | [optional] 

## Example

```python
from touroptimizer_py_client.models.location_parameters import LocationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of LocationParameters from a JSON string
location_parameters_instance = LocationParameters.from_json(json)
# print the JSON string representation of the object
print LocationParameters.to_json()

# convert the object into a dict
location_parameters_dict = location_parameters_instance.to_dict()
# create an instance of LocationParameters from a dict
location_parameters_form_dict = location_parameters.from_dict(location_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


