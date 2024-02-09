# OptimizationStatus

The status of the optimization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_description** | **str** | The description of status of the optimization | 
**error** | **str** | An  error code/desciption | 
**status** | **str** | The status of the optimization | 

## Example

```python
from touroptimizer_py_client.models.optimization_status import OptimizationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationStatus from a JSON string
optimization_status_instance = OptimizationStatus.from_json(json)
# print the JSON string representation of the object
print OptimizationStatus.to_json()

# convert the object into a dict
optimization_status_dict = optimization_status_instance.to_dict()
# create an instance of OptimizationStatus from a dict
optimization_status_form_dict = optimization_status.from_dict(optimization_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


