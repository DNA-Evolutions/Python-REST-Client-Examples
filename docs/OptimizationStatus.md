# OptimizationStatus

The status of the optimization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_description** | **str** | A human-readable description of the optimization outcome (e.g. &#39;SUCCESS_WITH_SOLUTION&#39;, &#39;Optimization execution failed due to timeout&#39;). Provides more context than the status tag alone. | 
**error** | **str** | An error code or message describing the failure cause. Set to &#39;NO_ERROR&#39; on successful runs. On failure, contains the exception message or a structured error identifier for programmatic handling. | 
**status** | **str** | The machine-readable status tag indicating the optimization outcome. UNKNOWN: status not yet determined. ERROR: the run failed. SUCCESS_WITH_SOLUTION: completed with a valid solution. SUCCESS_WITHOUT_SOLUTION: completed but no feasible assignment was found. | 

## Example

```python
from touroptimizer_py_client.models.optimization_status import OptimizationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationStatus from a JSON string
optimization_status_instance = OptimizationStatus.from_json(json)
# print the JSON string representation of the object
print(OptimizationStatus.to_json())

# convert the object into a dict
optimization_status_dict = optimization_status_instance.to_dict()
# create an instance of OptimizationStatus from a dict
optimization_status_from_dict = OptimizationStatus.from_dict(optimization_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


