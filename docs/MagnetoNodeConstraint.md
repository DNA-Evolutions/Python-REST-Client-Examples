# MagnetoNodeConstraint

A node-to-node soft constraint that creates magnetic attraction or repulsion between nodes. In attraction mode, the optimizer prefers placing the listed nodes on the same route. In repulsion mode, it prefers separating them. Supports ordering preferences (front/back of route).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_magnet_ids** | **List[str]** | A list of user-provided node-magntet-ids. Attraction Mode: A node holding this constraints attracts nodes (defined via ids) to share the same route. Repulsive mode: A node holding this constraints repels nodes (defined via ids). | 
**order** | **str** | The desired order. For example, if desired node order is front, the node carrying the constraint is ideally in front of the other nodes defined in nodeMagnetIds. | 
**type_name** | **str** | The typeName of the object | [default to 'MagnetoNode']
**is_attracting_magnet** | **bool** | True: Attracting nodes. False: Repel nodes. | 

## Example

```python
from touroptimizer_py_client.models.magneto_node_constraint import MagnetoNodeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of MagnetoNodeConstraint from a JSON string
magneto_node_constraint_instance = MagnetoNodeConstraint.from_json(json)
# print the JSON string representation of the object
print(MagnetoNodeConstraint.to_json())

# convert the object into a dict
magneto_node_constraint_dict = magneto_node_constraint_instance.to_dict()
# create an instance of MagnetoNodeConstraint from a dict
magneto_node_constraint_from_dict = MagnetoNodeConstraint.from_dict(magneto_node_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


