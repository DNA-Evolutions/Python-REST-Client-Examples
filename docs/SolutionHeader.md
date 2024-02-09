# SolutionHeader

The header of the whole solution. Summarizing important data like total number of routes, total time needed for ALL routes etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_routes** | **int** | The numRoutes. The number of routes. | 
**num_scheduled_routes** | **int** | The numScheduledRoutes. The number of routes that have non-zero time. | 
**tot_elements** | **int** | The total number of Elements inlucidng Nodes and Resoures | 
**unassigned_element_ids** | **List[str]** | The unassignedElementIds, The ids of the elements that were unassigned during the Optimization run. Either by the AutoFilter or at start up due to conflicting hard-constraints. | 
**tot_cost** | **float** | The total cost is the abstract value that is used as figure of merit during the Optimization run. | 
**tot_time** | **str** | The total time needed for all routes. | 
**tot_idle_time** | **str** | The total IdleTime accumulated over all routes. | 
**tot_prod_time** | **str** | The total Productive Time accumulated over all routes | 
**tot_tran_time** | **str** | The total transit Time accumulated over all routes | 
**tot_termi_time** | **str** | The total termination Time accumulated over all routes | 
**tot_distance** | **str** | The total distance accumulated over all routes | 
**tot_termi_distance** | **str** | The total termiantion distance accumulated over all routes | 
**job_violations** | [**List[Violation]**](Violation.md) | The jobViolations. The violation that occured on Job level. This does NOT contain individual node violations like lateness etc. Moreover,  it contains violations like relation-constraints between nodes. For example, node &#39;A&#39; needs to be visited before node &#39;B&#39; is violated. | 

## Example

```python
from touroptimizer_py_client.models.solution_header import SolutionHeader

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionHeader from a JSON string
solution_header_instance = SolutionHeader.from_json(json)
# print the JSON string representation of the object
print SolutionHeader.to_json()

# convert the object into a dict
solution_header_dict = solution_header_instance.to_dict()
# create an instance of SolutionHeader from a dict
solution_header_form_dict = solution_header.from_dict(solution_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


