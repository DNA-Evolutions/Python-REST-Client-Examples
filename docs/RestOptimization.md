# RestOptimization

The REST-specific specialization of OptimizationConfig with JSONConfig as the extension type. This is the top-level request/response object for the TourOptimizer REST API. Inherits all fields from OptimizationConfig and adds JSON-specific extension support for license keys, persistence settings, creator settings, and timeout configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_status** | [**OptimizationStatus**](OptimizationStatus.md) |  | [optional] 
**id** | **str** | A system-generated unique identifier assigned by the persistence layer (e.g. MongoDB ObjectId). This field is read-only and will be populated automatically when the optimization snapshot is stored in the database. Clients may use this value together with the creator field to retrieve or reference a specific persisted snapshot. | [optional] 
**created_time_stamp** | **int** | An epoch-millisecond timestamp recording when this optimization snapshot was created. Populated automatically by the server at persistence time. Used for chronological ordering and expiry management Do not set this field in the input — it will be overwritten. | [optional] 
**creator** | **str** | A tenant-scoped identifier for the entity that submitted this optimization. Typically derived as a SHA-256 hash of the creator name supplied in the request&#39;s creatorSetting. Used as the primary scoping key for database queries — all persistence read operations require the creator to match, ensuring tenant isolation in multi-tenant deployments. Populated automatically by the server; do not set this field in the input. | [optional] 
**ident** | **str** | A user-defined, human-readable label for this optimization run. Useful for distinguishing runs in database queries and audit logs (e.g. &#39;Weekly-Route-Plan-CW42&#39; or &#39;NightShift-Berlin&#39;). If not provided, the server generates a default identifier based on a timestamp. Note: this field is stored as unencrypted metadata even when payload encryption is enabled — avoid embedding sensitive business information. | [optional] 
**nodes** | [**List[Node]**](Node.md) | The list of nodes (work items, customer locations, or events) to be scheduled and assigned to resources. Each node defines a geographic or event-based location, one or more opening-hour windows, a required visit duration, and optional constraints (skill requirements, resource bindings, priority, pickup-and-delivery loads). Every node id must be globally unique across all nodes and resources in this configuration. | 
**resources** | [**List[Resource]**](Resource.md) | The list of resources (vehicles, drivers, technicians, or other mobile agents) available to visit the defined nodes. Each resource specifies a home position, one or more working-hour windows, maximum working time and distance constraints, optional qualifications (skills), an optional alternate destination, and overnight-stay policies. Resource ids must be globally unique across all elements. | 
**node_relations** | [**List[NodeRelation]**](NodeRelation.md) | The list of inter-node relations that impose ordering or co-assignment constraints between nodes. Supported relation types include SAME_ROUTE (nodes must be on the same route), SAME_VISITOR (nodes must be served by the same resource), DIFFERENT_ROUTE (nodes must not share a route), and relative time-window relations that enforce temporal precedence (e.g. node A must be visited before node B within a defined time gap). | [optional] 
**element_connections** | [**List[ElementConnection]**](ElementConnection.md) | Pre-computed pairwise connections between elements (nodes and resources). Each connection specifies the travel distance and time between a source and a target element, optionally including time-dependent traffic profiles via connectionByTime. If connections are not provided, the optimizer falls back to a Haversine-based distance approximation or a configured backup connector. Providing accurate connections significantly improves solution quality. In persisted results, this list may be omitted to conserve storage (controlled via saveConnections). | [optional] 
**zone_connections** | [**List[ZoneConnection]**](ZoneConnection.md) | Zone connections define penalties or restrictions for crossing geographic zone boundaries (e.g. bridge tolls, tunnel crossings, or administrative borders). Each ZoneConnection specifies a pair of zone numbers and an associated crossing cost. When a route transitions between zones, the optimizer accumulates these costs, which discourages unnecessary zone crossings and promotes geographically cohesive routes. | [optional] 
**type_dictionaries** | [**TypeDictionaries**](TypeDictionaries.md) |  | [optional] 
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
print(RestOptimization.to_json())

# convert the object into a dict
rest_optimization_dict = rest_optimization_instance.to_dict()
# create an instance of RestOptimization from a dict
rest_optimization_from_dict = RestOptimization.from_dict(rest_optimization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


