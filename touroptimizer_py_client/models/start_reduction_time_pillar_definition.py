# coding: utf-8

"""
    DNA Evolutions - JOpt.TourOptimizer

    This is DNA's JOpt.TourOptimizer service. A RESTful Spring Boot application using springdoc-openapi and OpenAPI 3. JOpt.TourOpptimizer is a service that delivers route optimization and automatic scheduling features to be easily integrated into any third-party application. JOpt.TourOpptimizer encapsulates all necessary optimization functionality and provides a comprehensive REST API that offers a domain-specific optimization interface for the transportation industry. The service is stateless and does not come with graphical user interfaces, map depiction or any databases. These extensions and adjustments are supposed to be introduced by the consumer of the service while integrating it into his/her own application. The service will allow for many suitable adjustments and user-specific settings to adjust the behaviour and optimization goals (e.g. minimizing distance, maximizing resource utilization, etc.) through a comprehensive set of functions. This will enable you to gain control of the complete optimization processes.This service is based on JOpt (null)

    The version of the OpenAPI document: 1.2.6-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class StartReductionTimePillarDefinition(BaseModel):
    """
    The settings/defintion for the reduction time at the start of the route for pillar nodes. Please see startReductionTimeDefinition for details.
    """ # noqa: E501
    max_route_start_reduction_time_pillar: StrictStr = Field(description="The maximal Routes' Start Reduction Time for pillars nodes the Optimizer is allowed to use.", alias="maxRouteStartReductionTimePillar")
    is_reduction_time_only_used_for_driving_pillar: StrictBool = Field(description="The boolean isReductionTimeOnlyUsedForDriving defines if a Resource is allowed to use reduction time only for driving to the first node (here a pillar) but not for working on it.", alias="isReductionTimeOnlyUsedForDrivingPillar")
    __properties: ClassVar[List[str]] = ["maxRouteStartReductionTimePillar", "isReductionTimeOnlyUsedForDrivingPillar"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StartReductionTimePillarDefinition from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StartReductionTimePillarDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxRouteStartReductionTimePillar": obj.get("maxRouteStartReductionTimePillar"),
            "isReductionTimeOnlyUsedForDrivingPillar": obj.get("isReductionTimeOnlyUsedForDrivingPillar")
        })
        return _obj


