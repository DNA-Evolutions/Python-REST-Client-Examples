# JobAcceptedResponse

JobAcceptedResponse for a submitted job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique job id token. This should be treated as secret but is not the only security barrier. | 
**creator_hash** | **str** | Thr related creatorHash force-hashed by sha256(). In the optimization result the creator is only hashed, if the magic prefix &#39;hash:&#39; followed by the creator is used. | [optional] 
**ident** | **str** | The ident of the optimization to serach for. Leave blank if not required | [optional] 
**submitted_at** | **int** | The time as millis when job was committed. | [optional] 
**status** | **str** | The status. | [optional] 

## Example

```python
from touroptimizer_py_client.models.job_accepted_response import JobAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobAcceptedResponse from a JSON string
job_accepted_response_instance = JobAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(JobAcceptedResponse.to_json())

# convert the object into a dict
job_accepted_response_dict = job_accepted_response_instance.to_dict()
# create an instance of JobAcceptedResponse from a dict
job_accepted_response_from_dict = JobAcceptedResponse.from_dict(job_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


