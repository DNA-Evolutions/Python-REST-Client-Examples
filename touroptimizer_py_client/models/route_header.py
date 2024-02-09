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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from touroptimizer_py_client.models.violation import Violation
from typing import Optional, Set
from typing_extensions import Self

class RouteHeader(BaseModel):
    """
    The header of the solution per route is summarizing important data like number of elements in the route , total time needed for the route etc.
    """ # noqa: E501
    cost: Union[StrictFloat, StrictInt] = Field(description="The abstract cost value of the route.")
    time: StrictStr = Field(description="The time that is needed for the route.")
    idle_time: StrictStr = Field(description="The accumlated idleTime of the route.", alias="idleTime")
    prod_time: StrictStr = Field(description="The productive time of the route. Productive time is working-time spend at a node.", alias="prodTime")
    tran_time: StrictStr = Field(description="The tranTime. The summed transit time of the route.", alias="tranTime")
    termi_time: StrictStr = Field(description="The termiTime. The time taken from the last element to the termination element of the route.", alias="termiTime")
    distance: StrictStr = Field(description="The distance. The summed transit distance of the route.")
    termi_distance: StrictStr = Field(description="The termiDistance. The distance taken from the last element to the termination element of the route.", alias="termiDistance")
    route_violations: List[Violation] = Field(description="The routeViolations. Violations that occur on route level. For example, overtime, overdistance etc.", alias="routeViolations")
    is_closed: StrictBool = Field(description="The isClosed boolean describes if a Resource has to visit the termination element of the Route. By default, the start element and the termination element of a Route is the Resource itself. In case of a closed route, by default, the Resource returns to its original starting location.", alias="isClosed")
    is_alternate_destination: StrictBool = Field(description="The isAlternateDestination boolean. Descibes of the Resource has an alternate destination. The Resource has to end it's Route at the alternate destination there but  will start from the original route start again the next working hour.", alias="isAlternateDestination")
    __properties: ClassVar[List[str]] = ["cost", "time", "idleTime", "prodTime", "tranTime", "termiTime", "distance", "termiDistance", "routeViolations", "isClosed", "isAlternateDestination"]

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
        """Create an instance of RouteHeader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in route_violations (list)
        _items = []
        if self.route_violations:
            for _item in self.route_violations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['routeViolations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cost": obj.get("cost"),
            "time": obj.get("time"),
            "idleTime": obj.get("idleTime"),
            "prodTime": obj.get("prodTime"),
            "tranTime": obj.get("tranTime"),
            "termiTime": obj.get("termiTime"),
            "distance": obj.get("distance"),
            "termiDistance": obj.get("termiDistance"),
            "routeViolations": [Violation.from_dict(_item) for _item in obj["routeViolations"]] if obj.get("routeViolations") is not None else None,
            "isClosed": obj.get("isClosed"),
            "isAlternateDestination": obj.get("isAlternateDestination")
        })
        return _obj


