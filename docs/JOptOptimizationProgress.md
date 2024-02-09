# JOptOptimizationProgress

JOptOptimizationProgress model for the documentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The obejct id. Will be filled out by the optimizer, if necessary | [optional] 
**creator** | **str** | An id related to the creator that is filled out autmatically | [optional] 
**ident** | **str** | The ident of the currently running optimization | 
**caller_id** | **str** | The id of the currently running optimization algorithm | 
**cur_progress** | **float** | The progress in percentage of the currently running optimization algorithm | 
**cur_cost** | **float** | The current cost of the currently running optimization algorithm | 
**stage** | **int** | The stage of the optimization. The first running algorithm will get the stage 0. | 
**desc** | **str** | The progress as human readable description | 
**expire_at** | **datetime** | Optional value that will be used for database cleanup purposes. | [optional] 

## Example

```python
from touroptimizer_py_client.models.j_opt_optimization_progress import JOptOptimizationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of JOptOptimizationProgress from a JSON string
j_opt_optimization_progress_instance = JOptOptimizationProgress.from_json(json)
# print the JSON string representation of the object
print JOptOptimizationProgress.to_json()

# convert the object into a dict
j_opt_optimization_progress_dict = j_opt_optimization_progress_instance.to_dict()
# create an instance of JOptOptimizationProgress from a dict
j_opt_optimization_progress_form_dict = j_opt_optimization_progress.from_dict(j_opt_optimization_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


