# RunAcceptedResponse

Confirmation that a synchronous optimization run has been accepted and started. Use the runId to retrieve the result, subscribe to event streams, or stop the run early.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Unique identifier for this run. Use with GET /api/v1/runs/{runId}/result to retrieve the result and GET /api/v1/runs/{runId}/stream/* for live events. | [optional] 
**submitted_at** | **int** | Epoch-millisecond timestamp when the run was accepted. | [optional] 
**ident** | **str** | User-defined label echoed back from the input ident field. | [optional] 

## Example

```python
from touroptimizer_py_client.models.run_accepted_response import RunAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunAcceptedResponse from a JSON string
run_accepted_response_instance = RunAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(RunAcceptedResponse.to_json())

# convert the object into a dict
run_accepted_response_dict = run_accepted_response_instance.to_dict()
# create an instance of RunAcceptedResponse from a dict
run_accepted_response_from_dict = RunAcceptedResponse.from_dict(run_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


