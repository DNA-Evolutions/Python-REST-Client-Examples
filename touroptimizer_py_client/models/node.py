# coding: utf-8

"""
    DNA Evolutions - JOpt.TourOptimizer

    This is DNA's JOpt.TourOptimizer service. A RESTful Spring Boot application using springdoc-openapi and OpenAPI 3. JOpt.TourOptimizer is a service that delivers route optimization and automatic scheduling features to be easily integrated into any third-party application. JOpt.TourOptimizer encapsulates all necessary optimization functionality and provides a comprehensive REST API that offers a domain-specific optimization interface for the transportation industry. The service is stateless and does not come with graphical user interfaces, map depiction or any databases. These extensions and adjustments are supposed to be introduced by the consumer of the service while integrating it into his/her own application. The service will allow for many suitable adjustments and user-specific settings to adjust the behaviour and optimization goals (e.g. minimizing distance, maximizing resource utilization, etc.) through a comprehensive set of functions. This will enable you to gain control of the complete optimization processes.This service is based on JOpt (7.5.1-rc3-j17-SNAPSHOT)

    The version of the OpenAPI document: unknown
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from touroptimizer_py_client.models.constraint import Constraint
from touroptimizer_py_client.models.i_node_depot import INodeDepot
from touroptimizer_py_client.models.load_dimension import LoadDimension
from touroptimizer_py_client.models.node_color import NodeColor
from touroptimizer_py_client.models.node_type import NodeType
from touroptimizer_py_client.models.offered_node import OfferedNode
from touroptimizer_py_client.models.opening_hours import OpeningHours
from touroptimizer_py_client.models.qualification import Qualification
from typing import Optional, Set
from typing_extensions import Self

class Node(BaseModel):
    """
    The list of nodes
    """ # noqa: E501
    id: StrictStr = Field(description="The unique id of the node. It is not possible, to create mutliple elements (also Resources) with the same id.")
    extra_info: Optional[StrictStr] = Field(default=None, description="A custom extra info string that is attached to the Node.", alias="extraInfo")
    location_id: Optional[StrictStr] = Field(default=None, description="The location id can relate a node to the connection of another node. For example  the node 'MyFirstNode' and 'MySecondNode' have the same location. It is sufficient to provide the  connection data for 'MyFirstNode' and set the LocationId of 'MySecondNode' to be 'MyFirstNode'", alias="locationId")
    constraint_alias_id: Optional[StrictStr] = Field(default=None, description="The constraintAliasId. If set is used during constraint assessment instead of using the normal id.", alias="constraintAliasId")
    type: NodeType
    opening_hours: List[OpeningHours] = Field(description="The list of non-overlapping openingHours of the nodes.", alias="openingHours")
    visit_duration: StrictStr = Field(description="The visitDuration defines how long a visitor needs to stay at the node.", alias="visitDuration")
    constraints: Optional[List[Constraint]] = Field(default=None, description="The constraints of this node")
    offered_node: Optional[OfferedNode] = Field(default=None, alias="offeredNode")
    load_dimension: Optional[LoadDimension] = Field(default=None, alias="loadDimension")
    load: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The load")
    qualifications: Optional[List[Qualification]] = Field(default=None, description="The qualifications of the node.")
    lockdown_time: Optional[StrictInt] = Field(default=None, description="The lockdownTime", alias="lockdownTime")
    fix_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The fixCost defines an abstract cost that arrises when this node is visited.", alias="fixCost")
    priority: Optional[StrictInt] = Field(default=None, description="The priority of the node. A higher priority leads to a higher cost if a node shows violations. As the Optimizer tries to reduce cost, a higher priority results in lower chance  of seeing violations on this node. However, if all nodes of an Optimization have a priority, the effect vanishes.")
    priority_first: Optional[StrictInt] = Field(default=None, description="The priorityFirst defines if we want a node to be the first node in a route-solution.", alias="priorityFirst")
    priority_last: Optional[StrictInt] = Field(default=None, description="The priorityLast defines if we want a node to be the last node in a route-solution.", alias="priorityLast")
    node_color: Optional[NodeColor] = Field(default=None, alias="nodeColor")
    min_auto_filter_protected_executions: Optional[StrictInt] = Field(default=None, description="The minAutoFilterProtectedExecutions", alias="minAutoFilterProtectedExecutions")
    node_depot: Optional[INodeDepot] = Field(default=None, alias="nodeDepot")
    route_dependent_visit_duration: Optional[StrictBool] = Field(default=False, description="The routeDependentVisitDuration", alias="routeDependentVisitDuration")
    allow_move_to_reduce_flex_time: Optional[StrictBool] = Field(default=False, description="The allowMoveToReduceFlexTime", alias="allowMoveToReduceFlexTime")
    min_visit_duration: Optional[StrictStr] = Field(default=None, description="The minVisitDuration", alias="minVisitDuration")
    joint_visit_duration: Optional[StrictStr] = Field(default=None, description="The jointVisitDuration. If nodes are situated closely to each other (defined via property 'JOpt.JointVisitDuration.maxRadiusMeter') a joint visit duration can be defined. For example, 3 nodes have a visit duration of 20 minutes each. The  joint visit duration for ALL nodes is set to be 10 minutes. Further, they are close enough to each other, that the joint visit duration logic can be triggered. The optimizer finds a solution in which all three nodes are visted in direct succession. The first node (of the three) needs to be visted for the original visit duration of 20 minutes. The seconds and third nodes only needs to be visited for 10 minutes.", alias="jointVisitDuration")
    return_start_duration: Optional[StrictStr] = Field(default=None, description="The returnStartDuration", alias="returnStartDuration")
    is_optimizable: Optional[StrictBool] = Field(default=True, description="The boolean isOptimizable. Defines if a node is optimizable. This property will be auto-defined by the optimizer..", alias="isOptimizable")
    is_optional: Optional[StrictBool] = Field(default=False, description="The boolean isOptional. If a node is optional, the Optimizer can decide on its own, if the node is visited or not. Usually, this settings only makes sense in PND problems.", alias="isOptional")
    is_unassigned: Optional[StrictBool] = Field(default=False, description="The boolean isUnassigned. Defines if a node was unassigned by the Optimizer.", alias="isUnassigned")
    is_causing_idle_time_cost: Optional[StrictBool] = Field(default=True, description="The boolean isCausingIdleTimeCost. By default, waiting at a node to open is creating idle time cost. As the Optimizer tries to reduce cost, it will also try to reschedule nodes if idle time cost is generated. In some problem setups (especially problems of the kind: Low node count, high WorkingHours availability) it may be desired to keep the position of the nodes, even though idle time is created.", alias="isCausingIdleTimeCost")
    is_wait_on_early_arrival: Optional[StrictBool] = Field(default=True, description="The boolean isWaitOnEarlyArrival. In case a Resources reaches a node too early (before the start of the node's OpeningHours), the Resource can either start working direclty (false) or wait for the node to open (true, default).", alias="isWaitOnEarlyArrival")
    is_wait_on_early_arrival_first_node: Optional[StrictBool] = Field(default=False, description="The boolean isWaitOnEarlyArrivalFirstNode. In case a Resources reaches the FIRST node of a route too early (before the start of the node's OpeningHours),\"              + \" the Resource can either start working direclty (true) or wait for the FIRST node to open (false, default). This setting only takes action if isWaitOnEarlyArrival is set to true.", alias="isWaitOnEarlyArrivalFirstNode")
    is_opening_hours_includes_duration: Optional[StrictBool] = Field(default=True, description="The boolean isOpeningHoursIncludesDuration. By default a node's openingHour defines the time-window  in which a task has to be fulfilled, meaning a Visitor has to arrive, work, and leave within that time-window. If isOpeningHoursIncludesDuration is set to false, the time-window only counts as arrival-window for the Resource.", alias="isOpeningHoursIncludesDuration")
    is_work_node: Optional[StrictBool] = Field(default=True, description="The isWorkNode", alias="isWorkNode")
    is_stay_node: Optional[StrictBool] = Field(default=False, description="The boolean isStayNode defines if a node is capable to be a stay node. A stay node overrides the route termination element of a route, and the route start element of the next route and is  used in the context of 'overnight-stays'.", alias="isStayNode")
    __properties: ClassVar[List[str]] = ["id", "extraInfo", "locationId", "constraintAliasId", "type", "openingHours", "visitDuration", "constraints", "offeredNode", "loadDimension", "load", "qualifications", "lockdownTime", "fixCost", "priority", "priorityFirst", "priorityLast", "nodeColor", "minAutoFilterProtectedExecutions", "nodeDepot", "routeDependentVisitDuration", "allowMoveToReduceFlexTime", "minVisitDuration", "jointVisitDuration", "returnStartDuration", "isOptimizable", "isOptional", "isUnassigned", "isCausingIdleTimeCost", "isWaitOnEarlyArrival", "isWaitOnEarlyArrivalFirstNode", "isOpeningHoursIncludesDuration", "isWorkNode", "isStayNode"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Node from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in opening_hours (list)
        _items = []
        if self.opening_hours:
            for _item_opening_hours in self.opening_hours:
                if _item_opening_hours:
                    _items.append(_item_opening_hours.to_dict())
            _dict['openingHours'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item_constraints in self.constraints:
                if _item_constraints:
                    _items.append(_item_constraints.to_dict())
            _dict['constraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of offered_node
        if self.offered_node:
            _dict['offeredNode'] = self.offered_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of load_dimension
        if self.load_dimension:
            _dict['loadDimension'] = self.load_dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in qualifications (list)
        _items = []
        if self.qualifications:
            for _item_qualifications in self.qualifications:
                if _item_qualifications:
                    _items.append(_item_qualifications.to_dict())
            _dict['qualifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of node_color
        if self.node_color:
            _dict['nodeColor'] = self.node_color.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_depot
        if self.node_depot:
            _dict['nodeDepot'] = self.node_depot.to_dict()
        # set to None if route_dependent_visit_duration (nullable) is None
        # and model_fields_set contains the field
        if self.route_dependent_visit_duration is None and "route_dependent_visit_duration" in self.model_fields_set:
            _dict['routeDependentVisitDuration'] = None

        # set to None if allow_move_to_reduce_flex_time (nullable) is None
        # and model_fields_set contains the field
        if self.allow_move_to_reduce_flex_time is None and "allow_move_to_reduce_flex_time" in self.model_fields_set:
            _dict['allowMoveToReduceFlexTime'] = None

        # set to None if is_optimizable (nullable) is None
        # and model_fields_set contains the field
        if self.is_optimizable is None and "is_optimizable" in self.model_fields_set:
            _dict['isOptimizable'] = None

        # set to None if is_optional (nullable) is None
        # and model_fields_set contains the field
        if self.is_optional is None and "is_optional" in self.model_fields_set:
            _dict['isOptional'] = None

        # set to None if is_unassigned (nullable) is None
        # and model_fields_set contains the field
        if self.is_unassigned is None and "is_unassigned" in self.model_fields_set:
            _dict['isUnassigned'] = None

        # set to None if is_causing_idle_time_cost (nullable) is None
        # and model_fields_set contains the field
        if self.is_causing_idle_time_cost is None and "is_causing_idle_time_cost" in self.model_fields_set:
            _dict['isCausingIdleTimeCost'] = None

        # set to None if is_wait_on_early_arrival (nullable) is None
        # and model_fields_set contains the field
        if self.is_wait_on_early_arrival is None and "is_wait_on_early_arrival" in self.model_fields_set:
            _dict['isWaitOnEarlyArrival'] = None

        # set to None if is_wait_on_early_arrival_first_node (nullable) is None
        # and model_fields_set contains the field
        if self.is_wait_on_early_arrival_first_node is None and "is_wait_on_early_arrival_first_node" in self.model_fields_set:
            _dict['isWaitOnEarlyArrivalFirstNode'] = None

        # set to None if is_opening_hours_includes_duration (nullable) is None
        # and model_fields_set contains the field
        if self.is_opening_hours_includes_duration is None and "is_opening_hours_includes_duration" in self.model_fields_set:
            _dict['isOpeningHoursIncludesDuration'] = None

        # set to None if is_work_node (nullable) is None
        # and model_fields_set contains the field
        if self.is_work_node is None and "is_work_node" in self.model_fields_set:
            _dict['isWorkNode'] = None

        # set to None if is_stay_node (nullable) is None
        # and model_fields_set contains the field
        if self.is_stay_node is None and "is_stay_node" in self.model_fields_set:
            _dict['isStayNode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "extraInfo": obj.get("extraInfo"),
            "locationId": obj.get("locationId"),
            "constraintAliasId": obj.get("constraintAliasId"),
            "type": NodeType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "openingHours": [OpeningHours.from_dict(_item) for _item in obj["openingHours"]] if obj.get("openingHours") is not None else None,
            "visitDuration": obj.get("visitDuration"),
            "constraints": [Constraint.from_dict(_item) for _item in obj["constraints"]] if obj.get("constraints") is not None else None,
            "offeredNode": OfferedNode.from_dict(obj["offeredNode"]) if obj.get("offeredNode") is not None else None,
            "loadDimension": LoadDimension.from_dict(obj["loadDimension"]) if obj.get("loadDimension") is not None else None,
            "load": obj.get("load"),
            "qualifications": [Qualification.from_dict(_item) for _item in obj["qualifications"]] if obj.get("qualifications") is not None else None,
            "lockdownTime": obj.get("lockdownTime"),
            "fixCost": obj.get("fixCost"),
            "priority": obj.get("priority"),
            "priorityFirst": obj.get("priorityFirst"),
            "priorityLast": obj.get("priorityLast"),
            "nodeColor": NodeColor.from_dict(obj["nodeColor"]) if obj.get("nodeColor") is not None else None,
            "minAutoFilterProtectedExecutions": obj.get("minAutoFilterProtectedExecutions"),
            "nodeDepot": INodeDepot.from_dict(obj["nodeDepot"]) if obj.get("nodeDepot") is not None else None,
            "routeDependentVisitDuration": obj.get("routeDependentVisitDuration") if obj.get("routeDependentVisitDuration") is not None else False,
            "allowMoveToReduceFlexTime": obj.get("allowMoveToReduceFlexTime") if obj.get("allowMoveToReduceFlexTime") is not None else False,
            "minVisitDuration": obj.get("minVisitDuration"),
            "jointVisitDuration": obj.get("jointVisitDuration"),
            "returnStartDuration": obj.get("returnStartDuration"),
            "isOptimizable": obj.get("isOptimizable") if obj.get("isOptimizable") is not None else True,
            "isOptional": obj.get("isOptional") if obj.get("isOptional") is not None else False,
            "isUnassigned": obj.get("isUnassigned") if obj.get("isUnassigned") is not None else False,
            "isCausingIdleTimeCost": obj.get("isCausingIdleTimeCost") if obj.get("isCausingIdleTimeCost") is not None else True,
            "isWaitOnEarlyArrival": obj.get("isWaitOnEarlyArrival") if obj.get("isWaitOnEarlyArrival") is not None else True,
            "isWaitOnEarlyArrivalFirstNode": obj.get("isWaitOnEarlyArrivalFirstNode") if obj.get("isWaitOnEarlyArrivalFirstNode") is not None else False,
            "isOpeningHoursIncludesDuration": obj.get("isOpeningHoursIncludesDuration") if obj.get("isOpeningHoursIncludesDuration") is not None else True,
            "isWorkNode": obj.get("isWorkNode") if obj.get("isWorkNode") is not None else True,
            "isStayNode": obj.get("isStayNode") if obj.get("isStayNode") is not None else False
        })
        return _obj


