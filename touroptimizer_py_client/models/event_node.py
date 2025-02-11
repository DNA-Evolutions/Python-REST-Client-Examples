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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from touroptimizer_py_client.models.node_type import NodeType
from touroptimizer_py_client.models.pillar_type import PillarType
from typing import Optional, Set
from typing_extensions import Self

class EventNode(NodeType):
    """
    EventNode
    """ # noqa: E501
    pillar_node: Optional[PillarType] = Field(default=None, alias="pillarNode")
    type_name: StrictStr = Field(description="The typeName of the object", alias="typeName")
    is_partial_exchange_idle_for_driving_time: Optional[StrictBool] = Field(default=True, description="An EventNode is allowed to be visited BEWTWEEN two Nodes and does not need to be positioned at a node.", alias="isPartialExchangeIdleForDrivingTime")
    __properties: ClassVar[List[str]] = ["typeName", "pillarNode", "isPartialExchangeIdleForDrivingTime"]

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
        """Create an instance of EventNode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pillar_node
        if self.pillar_node:
            _dict['pillarNode'] = self.pillar_node.to_dict()
        # set to None if is_partial_exchange_idle_for_driving_time (nullable) is None
        # and model_fields_set contains the field
        if self.is_partial_exchange_idle_for_driving_time is None and "is_partial_exchange_idle_for_driving_time" in self.model_fields_set:
            _dict['isPartialExchangeIdleForDrivingTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "typeName": obj.get("typeName") if obj.get("typeName") is not None else 'Event',
            "pillarNode": PillarType.from_dict(obj["pillarNode"]) if obj.get("pillarNode") is not None else None,
            "isPartialExchangeIdleForDrivingTime": obj.get("isPartialExchangeIdleForDrivingTime") if obj.get("isPartialExchangeIdleForDrivingTime") is not None else True
        })
        return _obj


