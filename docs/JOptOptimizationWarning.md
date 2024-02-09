# JOptOptimizationWarning

JOptOptimizationWarning model for the documentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | An id related to the creator that is filled out autmatically | [optional] 
**ident** | **str** | The ident of the currently running optimization | 
**message** | **str** | The info message | 
**code** | **int** | The info message code | 
**desc** | **str** | The description of the info | 
**expire_at** | **datetime** | Optional value that will be used for database cleanup purposes. | [optional] 

## Example

```python
from touroptimizer_py_client.models.j_opt_optimization_warning import JOptOptimizationWarning

# TODO update the JSON string below
json = "{}"
# create an instance of JOptOptimizationWarning from a JSON string
j_opt_optimization_warning_instance = JOptOptimizationWarning.from_json(json)
# print the JSON string representation of the object
print JOptOptimizationWarning.to_json()

# convert the object into a dict
j_opt_optimization_warning_dict = j_opt_optimization_warning_instance.to_dict()
# create an instance of JOptOptimizationWarning from a dict
j_opt_optimization_warning_form_dict = j_opt_optimization_warning.from_dict(j_opt_optimization_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


