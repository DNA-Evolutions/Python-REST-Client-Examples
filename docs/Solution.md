# Solution

The optimization solution. In a result snapshot, this contains the computed route assignments, scheduling details per node, violation reports, and summary headers (cost, distance, time). When provided as input (warm start), the optimizer uses this solution as its initial starting point and attempts to improve upon it. This enables incremental re-optimization, manual plan adjustments, and 'continue where we left off' workflows. If omitted in the input, the optimizer constructs a solution from scratch using its construction heuristic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_status** | [**OptimizationStatus**](OptimizationStatus.md) |  | [optional] 
**id** | **str** | An id created by the system that can be used for unique identification | [optional] 
**created_time_stamp** | **int** | A timestamp the Snapshot was created that will automatically filled out, if neccessary | [optional] 
**creator** | **str** | An id related to the creator that is filled out autmatically | [optional] 
**ident** | **str** | An optional title/ident inhertited from the OptimizationCondig. | [optional] 
**header** | [**SolutionHeader**](SolutionHeader.md) |  | [optional] 
**routes** | [**List[Route]**](Route.md) | The routes of the solution. | 

## Example

```python
from touroptimizer_py_client.models.solution import Solution

# TODO update the JSON string below
json = "{}"
# create an instance of Solution from a JSON string
solution_instance = Solution.from_json(json)
# print the JSON string representation of the object
print(Solution.to_json())

# convert the object into a dict
solution_dict = solution_instance.to_dict()
# create an instance of Solution from a dict
solution_from_dict = Solution.from_dict(solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


