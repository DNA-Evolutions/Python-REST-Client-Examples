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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GeoAddress(BaseModel):
    """
    The geographical address of the Position in case geo-coding will be applied.
    """ # noqa: E501
    location_id: Optional[StrictStr] = Field(default=None, description="The locationId", alias="locationId")
    housenumber: Optional[StrictStr] = Field(default=None, description="The housenumber")
    streetname: Optional[StrictStr] = Field(default=None, description="The streetname")
    city: Optional[StrictStr] = Field(default=None, description="The city")
    county: Optional[StrictStr] = Field(default=None, description="The county")
    state: Optional[StrictStr] = Field(default=None, description="The state")
    statecode: Optional[StrictStr] = Field(default=None, description="The statecode")
    country: Optional[StrictStr] = Field(default=None, description="The country")
    macrocountry: Optional[StrictStr] = Field(default=None, description="The macrocountry")
    countrycode: Optional[StrictStr] = Field(default=None, description="The country code (ISO CODE)")
    postalcode: Optional[StrictStr] = Field(default=None, description="The postalcode")
    layer: Optional[StrictStr] = Field(default=None, description="The layer")
    source: Optional[StrictStr] = Field(default=None, description="The source the data was extracted from")
    accuracy: Optional[StrictStr] = Field(default=None, description="The accuracy")
    confidence: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This is a general score computed to calculate how likely result is what was asked for. It's meant to be a combination of all the information available to Pelias. It's not super sophisticated, and results may not be sorted in confidence-score order. In that case results returned first should be trusted more. Confidence scores are floating point numbers ranging from '0.0' to '1.0'.")
    label: Optional[StrictStr] = Field(default=None, description="The label")
    __properties: ClassVar[List[str]] = ["locationId", "housenumber", "streetname", "city", "county", "state", "statecode", "country", "macrocountry", "countrycode", "postalcode", "layer", "source", "accuracy", "confidence", "label"]

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
        """Create an instance of GeoAddress from a JSON string"""
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
        """Create an instance of GeoAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "locationId": obj.get("locationId"),
            "housenumber": obj.get("housenumber"),
            "streetname": obj.get("streetname"),
            "city": obj.get("city"),
            "county": obj.get("county"),
            "state": obj.get("state"),
            "statecode": obj.get("statecode"),
            "country": obj.get("country"),
            "macrocountry": obj.get("macrocountry"),
            "countrycode": obj.get("countrycode"),
            "postalcode": obj.get("postalcode"),
            "layer": obj.get("layer"),
            "source": obj.get("source"),
            "accuracy": obj.get("accuracy"),
            "confidence": obj.get("confidence"),
            "label": obj.get("label")
        })
        return _obj


