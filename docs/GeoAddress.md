# GeoAddress

The geographical address of the Position in case geo-coding will be applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | The locationId | [optional] 
**housenumber** | **str** | The housenumber | [optional] 
**streetname** | **str** | The streetname | [optional] 
**city** | **str** | The city | [optional] 
**county** | **str** | The county | [optional] 
**state** | **str** | The state | [optional] 
**statecode** | **str** | The statecode | [optional] 
**country** | **str** | The country | [optional] 
**macrocountry** | **str** | The macrocountry | [optional] 
**countrycode** | **str** | The country code (ISO CODE) | [optional] 
**postalcode** | **str** | The postalcode | [optional] 
**layer** | **str** | The layer | [optional] 
**source** | **str** | The source the data was extracted from | [optional] 
**accuracy** | **str** | The accuracy | [optional] 
**confidence** | **float** | This is a general score computed to calculate how likely result is what was asked for. It&#39;s meant to be a combination of all the information available to Pelias. It&#39;s not super sophisticated, and results may not be sorted in confidence-score order. In that case results returned first should be trusted more. Confidence scores are floating point numbers ranging from &#39;0.0&#39; to &#39;1.0&#39;. | [optional] 
**label** | **str** | The label | [optional] 

## Example

```python
from touroptimizer_py_client.models.geo_address import GeoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of GeoAddress from a JSON string
geo_address_instance = GeoAddress.from_json(json)
# print the JSON string representation of the object
print GeoAddress.to_json()

# convert the object into a dict
geo_address_dict = geo_address_instance.to_dict()
# create an instance of GeoAddress from a dict
geo_address_form_dict = geo_address.from_dict(geo_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


