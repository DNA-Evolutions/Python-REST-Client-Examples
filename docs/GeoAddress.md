# GeoAddress

A structured geographic address used for geocoding. Contains fields for street, house number, postal code, city, country, region, and other GeoJSON-compatible address components. When provided on a Position, the geocoder resolves it to latitude/longitude coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | An optional identifier linking this address to a shared location entry. | [optional] 
**housenumber** | **str** | The house number of the address. | [optional] 
**streetname** | **str** | The street name of the address (without house number). | [optional] 
**city** | **str** | The city or locality name. | [optional] 
**county** | **str** | The county or administrative district. | [optional] 
**state** | **str** | The state or region name. | [optional] 
**statecode** | **str** | The state or region code (abbreviated form, e.g. &#39;NSW&#39;, &#39;BY&#39;). | [optional] 
**country** | **str** | The country name (e.g. &#39;Germany&#39;, &#39;Australia&#39;). | [optional] 
**macrocountry** | **str** | The macro-country or metropolitan region (e.g. &#39;Berlin&#39;, &#39;Sydney&#39;). | [optional] 
**countrycode** | **str** | The country code (ISO CODE) | [optional] 
**postalcode** | **str** | The postal or ZIP code. | [optional] 
**layer** | **str** | The geocoding layer (e.g. &#39;address&#39;, &#39;venue&#39;, &#39;street&#39;) indicating the granularity of the match. | [optional] 
**source** | **str** | The geocoding data source (e.g. &#39;openstreetmap&#39;, &#39;geonames&#39;) that provided this address. | [optional] 
**accuracy** | **str** | The accuracy level of the geocoding result (e.g. &#39;point&#39;, &#39;centroid&#39;, &#39;interpolated&#39;). | [optional] 
**confidence** | **float** | This is a general score computed to calculate how likely result is what was asked for. It&#39;s meant to be a combination of all the information available to Pelias. It&#39;s not super sophisticated, and results may not be sorted in confidence-score order. In that case results returned first should be trusted more. Confidence scores are floating point numbers ranging from &#39;0.0&#39; to &#39;1.0&#39;. | [optional] 
**label** | **str** | A fully formatted address label combining all available components (e.g. &#39;495 Old South Head Road, Rose Bay, NSW, Australia&#39;). | [optional] 

## Example

```python
from touroptimizer_py_client.models.geo_address import GeoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of GeoAddress from a JSON string
geo_address_instance = GeoAddress.from_json(json)
# print the JSON string representation of the object
print(GeoAddress.to_json())

# convert the object into a dict
geo_address_dict = geo_address_instance.to_dict()
# create an instance of GeoAddress from a dict
geo_address_from_dict = GeoAddress.from_dict(geo_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


