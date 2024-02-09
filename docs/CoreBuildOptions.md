# CoreBuildOptions

The coreBuildOptions provided by the library

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_core_properties** | **Dict[str, str]** | The buildCoreProperties give information about the library and its version that was used for the optimization run. | 

## Example

```python
from touroptimizer_py_client.models.core_build_options import CoreBuildOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CoreBuildOptions from a JSON string
core_build_options_instance = CoreBuildOptions.from_json(json)
# print the JSON string representation of the object
print CoreBuildOptions.to_json()

# convert the object into a dict
core_build_options_dict = core_build_options_instance.to_dict()
# create an instance of CoreBuildOptions from a dict
core_build_options_form_dict = core_build_options.from_dict(core_build_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


