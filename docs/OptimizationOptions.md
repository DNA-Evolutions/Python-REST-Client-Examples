# OptimizationOptions

The list of optimizationOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **Dict[str, str]** | The properties of the Optimization run. For example, the number of iterations for the Optimization run or the weight for certain Optimization goals can be defined. | 

## Example

```python
from touroptimizer_py_client.models.optimization_options import OptimizationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationOptions from a JSON string
optimization_options_instance = OptimizationOptions.from_json(json)
# print the JSON string representation of the object
print OptimizationOptions.to_json()

# convert the object into a dict
optimization_options_dict = optimization_options_instance.to_dict()
# create an instance of OptimizationOptions from a dict
optimization_options_form_dict = optimization_options.from_dict(optimization_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


