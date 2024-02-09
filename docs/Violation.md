# Violation

The routeViolations. Violations that occur on route level. For example, overtime, overdistance etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value is a violation specfic value. For example, if the violation is of subAttribute &#39;LATE&#39;, the value contains the late violation value in minutes. | 
**desc** | **str** | The description of the violation. A human readable description of the violation | 
**category** | **str** | The category of the violation. The main category of the violation. | 
**attribute** | **str** | The attribute is further defining the type of the violation. For example, late and early violation belong to the attribute &#39;TIMECONSTRAINT&#39;. | 
**sub_attribute** | **str** | The subAttribute defines what kind of violation we are dealing with. | 
**code** | **int** | The code is the unique code for each Violation type. | 

## Example

```python
from touroptimizer_py_client.models.violation import Violation

# TODO update the JSON string below
json = "{}"
# create an instance of Violation from a JSON string
violation_instance = Violation.from_json(json)
# print the JSON string representation of the object
print Violation.to_json()

# convert the object into a dict
violation_dict = violation_instance.to_dict()
# create an instance of Violation from a dict
violation_form_dict = violation.from_dict(violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


