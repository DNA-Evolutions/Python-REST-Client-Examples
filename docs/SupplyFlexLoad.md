# SupplyFlexLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_id** | **str** |  | [optional] 
**is_request** | **bool** |  | [optional] 
**is_fuzzy_visit** | **bool** |  | [optional] 
**type_name** | **str** | The typeName of the object | [default to 'SupplyFlexLoad']

## Example

```python
from touroptimizer_py_client.models.supply_flex_load import SupplyFlexLoad

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyFlexLoad from a JSON string
supply_flex_load_instance = SupplyFlexLoad.from_json(json)
# print the JSON string representation of the object
print SupplyFlexLoad.to_json()

# convert the object into a dict
supply_flex_load_dict = supply_flex_load_instance.to_dict()
# create an instance of SupplyFlexLoad from a dict
supply_flex_load_form_dict = supply_flex_load.from_dict(supply_flex_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


