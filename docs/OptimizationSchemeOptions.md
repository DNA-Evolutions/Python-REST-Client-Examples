# OptimizationSchemeOptions

The OptimizationSchemeOptions describes the desired algos to run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**construction_optimization_algorithm_config** | [**ConstructionOptimizationAlgorithmConfig**](ConstructionOptimizationAlgorithmConfig.md) |  | 
**heuristic_optimization_algorithm_configs** | [**List[HeuristicOptimizationAlgorithmConfig]**](HeuristicOptimizationAlgorithmConfig.md) | The heuristicOptimizationAlgorithmConfigs | 

## Example

```python
from touroptimizer_py_client.models.optimization_scheme_options import OptimizationSchemeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationSchemeOptions from a JSON string
optimization_scheme_options_instance = OptimizationSchemeOptions.from_json(json)
# print the JSON string representation of the object
print(OptimizationSchemeOptions.to_json())

# convert the object into a dict
optimization_scheme_options_dict = optimization_scheme_options_instance.to_dict()
# create an instance of OptimizationSchemeOptions from a dict
optimization_scheme_options_from_dict = OptimizationSchemeOptions.from_dict(optimization_scheme_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


