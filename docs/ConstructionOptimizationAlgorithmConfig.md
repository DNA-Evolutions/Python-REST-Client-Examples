# ConstructionOptimizationAlgorithmConfig

The configuration for the construction algorithm phase. Defines which construction heuristic to use (e.g. nearest-neighbor, cheapest-insertion) and its parameters. This phase builds the initial solution before the heuristic improvement phases begin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The algorithm | 

## Example

```python
from touroptimizer_py_client.models.construction_optimization_algorithm_config import ConstructionOptimizationAlgorithmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructionOptimizationAlgorithmConfig from a JSON string
construction_optimization_algorithm_config_instance = ConstructionOptimizationAlgorithmConfig.from_json(json)
# print the JSON string representation of the object
print(ConstructionOptimizationAlgorithmConfig.to_json())

# convert the object into a dict
construction_optimization_algorithm_config_dict = construction_optimization_algorithm_config_instance.to_dict()
# create an instance of ConstructionOptimizationAlgorithmConfig from a dict
construction_optimization_algorithm_config_from_dict = ConstructionOptimizationAlgorithmConfig.from_dict(construction_optimization_algorithm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


