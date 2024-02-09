# Node

The list of nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the node. It is not possible, to create mutliple elements (also Resources) with the same id. | 
**extra_info** | **str** | A custom extra info string that is attached to the Node. | [optional] 
**location_id** | **str** | The location id can relate a node to the connection of another node. For example  the node &#39;MyFirstNode&#39; and &#39;MySecondNode&#39; have the same location. It is sufficient to provide the  connection data for &#39;MyFirstNode&#39; and set the LocationId of &#39;MySecondNode&#39; to be &#39;MyFirstNode&#39; | [optional] 
**constraint_alias_id** | **str** | The constraintAliasId. If set is used during constraint assessment instead of using the normal id. | [optional] 
**type** | [**NodeType**](NodeType.md) |  | 
**opening_hours** | [**List[OpeningHours]**](OpeningHours.md) | The list of non-overlapping openingHours of the nodes. | 
**visit_duration** | **str** | The visitDuration defines how long a visitor needs to stay at the node. | 
**constraints** | [**List[Constraint]**](Constraint.md) | The constraints of this node | [optional] 
**offered_node** | [**OfferedNode**](OfferedNode.md) |  | [optional] 
**load_dimension** | [**LoadDimension**](LoadDimension.md) |  | [optional] 
**load** | **List[float]** | The load | [optional] 
**qualifications** | [**List[Qualification]**](Qualification.md) | The qualifications of the node. | [optional] 
**lockdown_time** | **int** | The lockdownTime | [optional] 
**fix_cost** | **float** | The fixCost defines an abstract cost that arrises when this node is visited. | [optional] 
**priority** | **int** | The priority of the node. A higher priority leads to a higher cost if a node shows violations. As the Optimizer tries to reduce cost, a higher priority results in lower chance  of seeing violations on this node. However, if all nodes of an Optimization have a priority, the effect vanishes. | [optional] 
**priority_first** | **int** | The priorityFirst defines if we want a node to be the first node in a route-solution. | [optional] 
**priority_last** | **int** | The priorityLast defines if we want a node to be the last node in a route-solution. | [optional] 
**node_color** | [**NodeColor**](NodeColor.md) |  | [optional] 
**min_auto_filter_protected_executions** | **int** | The minAutoFilterProtectedExecutions | [optional] 
**node_depot** | [**INodeDepot**](INodeDepot.md) |  | [optional] 
**route_dependent_visit_duration** | **bool** | The routeDependentVisitDuration | [optional] [default to False]
**allow_move_to_reduce_flex_time** | **bool** | The allowMoveToReduceFlexTime | [optional] [default to False]
**min_visit_duration** | **str** | The minVisitDuration | [optional] 
**joint_visit_duration** | **str** | The jointVisitDuration. If nodes are situated closely to each other (defined via property &#39;JOpt.JointVisitDuration.maxRadiusMeter&#39;) a joint visit duration can be defined. For example, 3 nodes have a visit duration of 20 minutes each. The  joint visit duration for ALL nodes is set to be 10 minutes. Further, they are close enough to each other, that the joint visit duration logic can be triggered. The optimizer finds a solution in which all three nodes are visted in direct succession. The first node (of the three) needs to be visted for the original visit duration of 20 minutes. The seconds and third nodes only needs to be visited for 10 minutes. | [optional] 
**return_start_duration** | **str** | The returnStartDuration | [optional] 
**is_optimizable** | **bool** | The boolean isOptimizable. Defines if a node is optimizable. This property will be auto-defined by the optimizer.. | [optional] [default to True]
**is_optional** | **bool** | The boolean isOptional. If a node is optional, the Optimizer can decide on its own, if the node is visited or not. Usually, this settings only makes sense in PND problems. | [optional] [default to False]
**is_unassigned** | **bool** | The boolean isUnassigned. Defines if a node was unassigned by the Optimizer. | [optional] [default to False]
**is_stay_node** | **bool** | The boolean isStayNode defines if a node is capable to be a stay node. A stay node overrides the route termination element of a route, and the route start element of the next route and is  used in the context of &#39;overnight-stays&#39;. | [optional] [default to False]
**is_work_node** | **bool** | The isWorkNode | [optional] [default to True]
**is_wait_on_early_arrival** | **bool** | The boolean isWaitOnEarlyArrival. In case a Resources reaches a node too early (before the start of the node&#39;s OpeningHours), the Resource can either start working direclty (false) or wait for the node to open (true, default). | [optional] [default to True]
**is_opening_hours_includes_duration** | **bool** | The boolean isOpeningHoursIncludesDuration. By default a node&#39;s openingHour defines the time-window  in which a task has to be fulfilled, meaning a Visitor has to arrive, work, and leave within that time-window. If isOpeningHoursIncludesDuration is set to false, the time-window only counts as arrival-window for the Resource. | [optional] [default to True]
**is_causing_idle_time_cost** | **bool** | The boolean isCausingIdleTimeCost. By default, waiting at a node to open is creating idle time cost. As the Optimizer tries to reduce cost, it will also try to reschedule nodes if idle time cost is generated. In some problem setups (especially problems of the kind: Low node count, high WorkingHours availability) it may be desired to keep the position of the nodes, even though idle time is created. | [optional] [default to True]
**is_wait_on_early_arrival_first_node** | **bool** | The boolean isWaitOnEarlyArrivalFirstNode. In case a Resources reaches the FIRST node of a route too early (before the start of the node&#39;s OpeningHours),\&quot;              + \&quot; the Resource can either start working direclty (true) or wait for the FIRST node to open (false, default). This setting only takes action if isWaitOnEarlyArrival is set to true. | [optional] [default to False]

## Example

```python
from touroptimizer_py_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print Node.to_json()

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_form_dict = node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


