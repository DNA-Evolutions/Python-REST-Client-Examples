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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DatabaseInfoSearch(BaseModel):
    """
    DatabaseInfoSearch model for a databse search
    """ # noqa: E501
    creator: Optional[StrictStr] = Field(default=None, description="A related creator.")
    ident: Optional[StrictStr] = Field(default=None, description="The ident of the optimization to serach for. Leave blank if not required")
    limit: Optional[StrictInt] = Field(default=None, description="The max number of results. Results are sorted by creation. Newest first by default")
    sort_direction: Optional[StrictStr] = Field(default=None, description="The sort direction of the createdDate. By default descending (DESC) newest first. For oldest first, use ASC (ascending)", alias="sortDirection")
    created_date_start: Optional[datetime] = Field(default=None, description="The snapshot was created AFTER this time. Leave blank if not required.", alias="createdDateStart")
    created_date_end: Optional[datetime] = Field(default=None, description="The snapshot was created BEFORE this time. Leave blank if not required.", alias="createdDateEnd")
    time_out: Optional[StrictStr] = Field(default=None, description="The timeOut for the request. By default one minute", alias="timeOut")
    __properties: ClassVar[List[str]] = ["creator", "ident", "limit", "sortDirection", "createdDateStart", "createdDateEnd", "timeOut"]

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
        """Create an instance of DatabaseInfoSearch from a JSON string"""
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
        """Create an instance of DatabaseInfoSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "creator": obj.get("creator"),
            "ident": obj.get("ident"),
            "limit": obj.get("limit"),
            "sortDirection": obj.get("sortDirection"),
            "createdDateStart": obj.get("createdDateStart"),
            "createdDateEnd": obj.get("createdDateEnd"),
            "timeOut": obj.get("timeOut")
        })
        return _obj


