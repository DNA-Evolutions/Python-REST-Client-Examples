# HeuristicOptimizationAlgorithmConfig

An ordered list of heuristic algorithm configurations that are executed sequentially after construction. Each entry defines an algorithm (e.g. Genetic Algorithm, Simulated Annealing) and its parameters (iteration count, repetitions). The optimizer runs each phase in order to progressively improve the solution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The algorithm | 
**simulated_annealing_override_num_iterations_value** | **int** | The simulatedAnnealingOverrideNumIterationsValue | [optional] 
**has_auto_filter** | **bool** | The hasAutoFilter | [optional] 

## Example

```python
from touroptimizer_py_client.models.heuristic_optimization_algorithm_config import HeuristicOptimizationAlgorithmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeuristicOptimizationAlgorithmConfig from a JSON string
heuristic_optimization_algorithm_config_instance = HeuristicOptimizationAlgorithmConfig.from_json(json)
# print the JSON string representation of the object
print(HeuristicOptimizationAlgorithmConfig.to_json())

# convert the object into a dict
heuristic_optimization_algorithm_config_dict = heuristic_optimization_algorithm_config_instance.to_dict()
# create an instance of HeuristicOptimizationAlgorithmConfig from a dict
heuristic_optimization_algorithm_config_from_dict = HeuristicOptimizationAlgorithmConfig.from_dict(heuristic_optimization_algorithm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


