# RestOptimization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_status** | [**OptimizationStatus**](OptimizationStatus.md) |  | [optional] 
**id** | **str** | An id created by the system that can be used for unique identification | [optional] 
**created_time_stamp** | **int** | A timestamp when snapshot was created that will automatically filled out, if neccessary | [optional] 
**creator** | **str** | An id related to the creator that is filled out autmatically | [optional] 
**ident** | **str** | An optional title/ident for the run. If not provided, a generated ident will be used | [optional] 
**nodes** | [**List[Node]**](Node.md) | The list of nodes | 
**resources** | [**List[Resource]**](Resource.md) | The list of resoruces | 
**node_relations** | [**List[NodeRelation]**](NodeRelation.md) | The list of relations | [optional] 
**element_connections** | [**List[ElementConnection]**](ElementConnection.md) | The list of connections | [optional] 
**optimization_options** | [**OptimizationOptions**](OptimizationOptions.md) |  | [optional] 
**core_build_options** | [**CoreBuildOptions**](CoreBuildOptions.md) |  | [optional] 
**solution** | [**Solution**](Solution.md) |  | [optional] 
**extension** | [**JSONConfig**](JSONConfig.md) |  | [optional] 

## Example

```python
from touroptimizer_py_client.models.rest_optimization import RestOptimization

# TODO update the JSON string below
json = "{}"
# create an instance of RestOptimization from a JSON string
rest_optimization_instance = RestOptimization.from_json(json)
# print the JSON string representation of the object
print RestOptimization.to_json()

# convert the object into a dict
rest_optimization_dict = rest_optimization_instance.to_dict()
# create an instance of RestOptimization from a dict
rest_optimization_form_dict = rest_optimization.from_dict(rest_optimization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


