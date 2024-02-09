# EncodedPolyline

The encoded polyline describing a connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoded_polyline** | **str** | An encoded polyline (see e.g.: https://developers.google.com/maps/documentation/utilities/polylinealgorithm). | 
**precision** | **float** | The precision of the encoded polyline. | 

## Example

```python
from touroptimizer_py_client.models.encoded_polyline import EncodedPolyline

# TODO update the JSON string below
json = "{}"
# create an instance of EncodedPolyline from a JSON string
encoded_polyline_instance = EncodedPolyline.from_json(json)
# print the JSON string representation of the object
print EncodedPolyline.to_json()

# convert the object into a dict
encoded_polyline_dict = encoded_polyline_instance.to_dict()
# create an instance of EncodedPolyline from a dict
encoded_polyline_form_dict = encoded_polyline.from_dict(encoded_polyline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


