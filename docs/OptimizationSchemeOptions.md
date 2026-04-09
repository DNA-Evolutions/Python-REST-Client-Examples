# OptimizationSchemeOptions

Defines the algorithm pipeline for an optimization run. Specifies exactly which construction heuristic builds the initial solution and which heuristic improvement phases (e.g. Genetic Algorithm, Simulated Annealing) are executed in sequence afterward. Each phase carries its own parameter set (iteration count, repetitions). If omitted from OptimizationOptions, the optimizer uses its built-in default pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**construction_optimization_algorithm_config** | [**ConstructionOptimizationAlgorithmConfig**](ConstructionOptimizationAlgorithmConfig.md) |  | 
**heuristic_optimization_algorithm_configs** | [**List[HeuristicOptimizationAlgorithmConfig]**](HeuristicOptimizationAlgorithmConfig.md) | An ordered list of heuristic algorithm configurations that are executed sequentially after construction. Each entry defines an algorithm (e.g. Genetic Algorithm, Simulated Annealing) and its parameters (iteration count, repetitions). The optimizer runs each phase in order to progressively improve the solution. | 

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


