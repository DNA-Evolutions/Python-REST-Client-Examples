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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from touroptimizer_py_client.models.violation import Violation
from typing import Optional, Set
from typing_extensions import Self

class SolutionHeader(BaseModel):
    """
    The header of the whole solution. Summarizing important data like total number of routes, total time needed for ALL routes etc.
    """ # noqa: E501
    num_routes: StrictInt = Field(description="The numRoutes. The number of routes.", alias="numRoutes")
    num_scheduled_routes: StrictInt = Field(description="The numScheduledRoutes. The number of routes that have non-zero time.", alias="numScheduledRoutes")
    tot_elements: StrictInt = Field(description="The total number of Elements inlucidng Nodes and Resoures", alias="totElements")
    unassigned_element_ids: List[StrictStr] = Field(description="The unassignedElementIds, The ids of the elements that were unassigned during the Optimization run. Either by the AutoFilter or at start up due to conflicting hard-constraints.", alias="unassignedElementIds")
    tot_cost: Union[StrictFloat, StrictInt] = Field(description="The total cost is the abstract value that is used as figure of merit during the Optimization run.", alias="totCost")
    tot_time: StrictStr = Field(description="The total time needed for all routes.", alias="totTime")
    tot_idle_time: StrictStr = Field(description="The total IdleTime accumulated over all routes.", alias="totIdleTime")
    tot_prod_time: StrictStr = Field(description="The total Productive Time accumulated over all routes", alias="totProdTime")
    tot_tran_time: StrictStr = Field(description="The total transit Time accumulated over all routes", alias="totTranTime")
    tot_termi_time: StrictStr = Field(description="The total termination Time accumulated over all routes", alias="totTermiTime")
    tot_distance: StrictStr = Field(description="The total distance accumulated over all routes", alias="totDistance")
    tot_termi_distance: StrictStr = Field(description="The total termiantion distance accumulated over all routes", alias="totTermiDistance")
    job_violations: List[Violation] = Field(description="The jobViolations. The violation that occured on Job level. This does NOT contain individual node violations like lateness etc. Moreover,  it contains violations like relation-constraints between nodes. For example, node 'A' needs to be visited before node 'B' is violated.", alias="jobViolations")
    __properties: ClassVar[List[str]] = ["numRoutes", "numScheduledRoutes", "totElements", "unassignedElementIds", "totCost", "totTime", "totIdleTime", "totProdTime", "totTranTime", "totTermiTime", "totDistance", "totTermiDistance", "jobViolations"]

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
        """Create an instance of SolutionHeader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in job_violations (list)
        _items = []
        if self.job_violations:
            for _item_job_violations in self.job_violations:
                if _item_job_violations:
                    _items.append(_item_job_violations.to_dict())
            _dict['jobViolations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SolutionHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numRoutes": obj.get("numRoutes"),
            "numScheduledRoutes": obj.get("numScheduledRoutes"),
            "totElements": obj.get("totElements"),
            "unassignedElementIds": obj.get("unassignedElementIds"),
            "totCost": obj.get("totCost"),
            "totTime": obj.get("totTime"),
            "totIdleTime": obj.get("totIdleTime"),
            "totProdTime": obj.get("totProdTime"),
            "totTranTime": obj.get("totTranTime"),
            "totTermiTime": obj.get("totTermiTime"),
            "totDistance": obj.get("totDistance"),
            "totTermiDistance": obj.get("totTermiDistance"),
            "jobViolations": [Violation.from_dict(_item) for _item in obj["jobViolations"]] if obj.get("jobViolations") is not None else None
        })
        return _obj


