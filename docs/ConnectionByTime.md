# ConnectionByTime

The connectionByTime defines an extension to the connection. For example, on Monday morning we need 2 hours to path a conneciton, whereas on Sunday morning we only need 1 hour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_definitions** | [**List[DateDef]**](DateDef.md) | The timeDefinitions describe at which times, what connection should be used. | 
**time_millis** | **List[int]** | The times to pass the connection in milliseconds for the underlying time defitions. | 
**distance_meters** | **List[float]** | The length of the connection in meters. | 

## Example

```python
from touroptimizer_py_client.models.connection_by_time import ConnectionByTime

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionByTime from a JSON string
connection_by_time_instance = ConnectionByTime.from_json(json)
# print the JSON string representation of the object
print ConnectionByTime.to_json()

# convert the object into a dict
connection_by_time_dict = connection_by_time_instance.to_dict()
# create an instance of ConnectionByTime from a dict
connection_by_time_form_dict = connection_by_time.from_dict(connection_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


