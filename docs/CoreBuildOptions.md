# CoreBuildOptions

Read-only metadata populated by the JOpt core library after an optimization run. Contains build properties such as the core library version, build timestamp, and Java runtime version. Useful for diagnostics, reproducibility audits, and support-ready bug reports. Do not set this field in the input — it is output-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_core_properties** | **Dict[str, str]** | The properties of the Optimization run. For example, the number of iterations for the Optimization run or the weight for certain Optimization goals can be defined. | 

## Example

```python
from touroptimizer_py_client.models.core_build_options import CoreBuildOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CoreBuildOptions from a JSON string
core_build_options_instance = CoreBuildOptions.from_json(json)
# print the JSON string representation of the object
print(CoreBuildOptions.to_json())

# convert the object into a dict
core_build_options_dict = core_build_options_instance.to_dict()
# create an instance of CoreBuildOptions from a dict
core_build_options_from_dict = CoreBuildOptions.from_dict(core_build_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


