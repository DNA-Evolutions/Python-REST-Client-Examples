# Violation

The routeViolations. Violations that occur on route level. For example, overtime, overdistance etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | If for example a constraint is triggering the violation, the underlying ident of the constraint class might be provided. | 
**desc** | **str** | The description of the violation. A human readable description of the violation | 
**offender** | **str** | The offender corresponding to the violation. That could be a node or route id. | [optional] 
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
print(Violation.to_json())

# convert the object into a dict
violation_dict = violation_instance.to_dict()
# create an instance of Violation from a dict
violation_from_dict = Violation.from_dict(violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


