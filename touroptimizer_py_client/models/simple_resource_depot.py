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

from pydantic import ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from touroptimizer_py_client.models.i_load_capacity import ILoadCapacity
from touroptimizer_py_client.models.i_resource_depot import IResourceDepot
from typing import Optional, Set
from typing_extensions import Self

class SimpleResourceDepot(IResourceDepot):
    """
    SimpleResourceDepot
    """ # noqa: E501
    maximal_unit_matched_capacity: Union[StrictFloat, StrictInt] = Field(description="The maximal unit matched total capacity of the depot.", alias="maximalUnitMatchedCapacity")
    capacity_unit_map: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The capacityUnitMap of the depot.", alias="capacityUnitMap")
    per_kilometer_cost_factor_map: Optional[Dict[str, StrictInt]] = Field(default=None, description="The perKilometerCostFactorMap of the depot.", alias="perKilometerCostFactorMap")
    type_name: StrictStr = Field(description="The typeName of the object", alias="typeName")
    empty_at_end_of_route_factor_map: Optional[Dict[str, StrictInt]] = Field(default=None, description="The emptyAtEndOfRouteFactorMap of the depot.", alias="emptyAtEndOfRouteFactorMap")
    __properties: ClassVar[List[str]] = ["items", "maximalTotalCapacity", "depotId", "capacityUnitMap", "typeName", "maximalUnitMatchedCapacity", "perKilometerCostFactorMap", "emptyAtEndOfRouteFactorMap"]

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
        """Create an instance of SimpleResourceDepot from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimpleResourceDepot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [ILoadCapacity.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "maximalTotalCapacity": obj.get("maximalTotalCapacity"),
            "depotId": obj.get("depotId"),
            "capacityUnitMap": obj.get("capacityUnitMap"),
            "typeName": obj.get("typeName") if obj.get("typeName") is not None else 'SimpleResourceDepot',
            "maximalUnitMatchedCapacity": obj.get("maximalUnitMatchedCapacity"),
            "perKilometerCostFactorMap": obj.get("perKilometerCostFactorMap"),
            "emptyAtEndOfRouteFactorMap": obj.get("emptyAtEndOfRouteFactorMap")
        })
        return _obj


