# Solution

The solution. Either provided by the library or by the user and used as starting solution for the optimization run

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
print Solution.to_json()

# convert the object into a dict
solution_dict = solution_instance.to_dict()
# create an instance of Solution from a dict
solution_form_dict = solution.from_dict(solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


