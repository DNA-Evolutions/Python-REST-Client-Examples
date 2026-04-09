# coding: utf-8

"""
    DNA Evolutions - JOpt.TourOptimizer

    # JOpt.TourOptimizer REST API  ![DNA Evolutions Logo](https://www.dna-evolutions.com/images/dna_logo.png)  JOpt.TourOptimizer is DNA Evolutions' route optimization and scheduling engine for transportation, field service, and resource planning scenarios.  This API is a **reactive Spring WebFlux REST service** with an **OpenAPI 3** contract, designed for integration into third-party systems and for generating typed client SDKs directly from the schema.  ---  ## Endpoint groups  ### Job endpoints (`job`)  The primary integration model for all deployments with a connected database.  Submit an optimization job with `POST /api/v1/jobs` and receive an HTTP 202 response containing a unique `jobId`. Use that jobId to poll for status, progress, warnings, errors, and the final result at any time — no open connection required.  | Endpoint | Description | Availability | |---|---|---| | `POST /api/v1/jobs` | Submit an async optimization job | All deployments | | `GET /api/v1/jobs/{jobId}/status` | Poll job status | All deployments | | `GET /api/v1/jobs/{jobId}/result` | Retrieve full optimization result | All deployments | | `GET /api/v1/jobs/{jobId}/solution` | Retrieve solution payload only | All deployments | | `GET /api/v1/jobs/{jobId}/progress` | Retrieve progress snapshots | All deployments | | `GET /api/v1/jobs/{jobId}/warnings` | Retrieve warning messages | All deployments | | `GET /api/v1/jobs/{jobId}/errors` | Retrieve error messages | All deployments | | `GET /api/v1/jobs/{jobId}/export` | Download result as ZIP archive | All deployments | | `POST /api/v1/jobs/{jobId}/stop` | Send graceful stop signal to a running job | All deployments | | `DELETE /api/v1/jobs/{jobId}` | Delete all persisted data for a job | All deployments | | `POST /api/v1/jobs/search` | Search jobs by metadata criteria | On-premise (free-search enabled) | | `POST /api/v1/jobs/import` | Import a pre-computed result directly | On-premise (import enabled) |  All job endpoints require the `X-Tenant-Id` header, injected by the API gateway. The `jobId` returned at submission is the only token needed for all subsequent reads.  ### Synchronous run endpoints (`optimization`)  Available on on-premise installations with synchronous mode enabled. The client holds the HTTP connection open and receives the result directly in the response body.  | Endpoint | Description | |---|---| | `POST /api/v1/runs` | Start a run, return runId immediately (HTTP 202) | | `GET /api/v1/runs/{runId}/result` | Block until run completes, return full result | | `GET /api/v1/runs/{runId}/solution` | Block until run completes, return solution only | | `DELETE /api/v1/runs/{runId}` | Stop the run gracefully | | `GET /api/v1/runs/{runId}/started` | One-shot signal when the run has started |  ### Event stream endpoints (`stream`)  Server-Sent Event streams for monitoring a running synchronous optimization in near real time. Subscribe to one or more streams while a `POST /api/v1/runs` call is in progress.  | Endpoint | Event type | |---|---| | `GET /api/v1/runs/{runId}/stream/progress` | Progress percentage and timing | | `GET /api/v1/runs/{runId}/stream/status` | Lifecycle status transitions | | `GET /api/v1/runs/{runId}/stream/warnings` | Non-fatal solver warnings | | `GET /api/v1/runs/{runId}/stream/errors` | Solver error events |  ### Health endpoint (`health`)  | Endpoint | Description | |---|---| | `GET /api/v1/health` | Service liveness and readiness |  ---  ## Deployment modes and feature flags  Endpoints that require specific conditions are activated via Spring `@Conditional` annotations and application properties. Endpoints not active in a given deployment are absent from the service entirely and do not appear in the runtime spec.  | Condition | Property / annotation | Effect | |---|---|---| | Database connected | `DatabaseEnabledCondition` | Activates all `job` endpoints | | Sync mode | `SynchControllersEnabledCondition` | Activates `optimization` and `stream` endpoints | | Free search | `DatabaseFreeSearchEnabledCondition` | Activates `POST /api/v1/jobs/search` | | Import | `DatabaseJobImportEnabledCondition` | Activates `POST /api/v1/jobs/import` |  ---  ## Tenant isolation  Every job endpoint is scoped by `X-Tenant-Id`, injected by the API gateway. Persisted documents are tagged with both `jobId` and `tenantId`. A request with a valid `jobId` but a mismatched `tenantId` returns no data. The `jobId` is a UUID v4 (122 bits of randomness) and is not a security credential — security is enforced by the verified `tenantId` from the gateway header.  ---  ## Encryption at rest  Results can be stored encrypted in two modes:  - **CLIENT mode**: key derived from a caller-provided passphrase via PBKDF2.   Pass the same secret in `X-Encryption-Secret` when reading back. - **KMS mode**: server-generated data encryption key (DEK) wrapped by an   external key management service (Azure Key Vault, AWS KMS). Decryption is   transparent to the caller.  The `encrypted` and `sec` fields in `DatabaseInfoSearchResult` indicate which mode was used for each stored result.  ---  ## Client generation  The OpenAPI schema can be used to generate typed clients for any language. The `operationId` values follow `{verb}{Resource}` lowerCamelCase convention (`createJob`, `getJobResult`, `listJobs`, etc.) for predictable generated method names.  ---  This service is based on **JOpt Core (unknown)**. 

    The version of the OpenAPI document: 1.3.5-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from touroptimizer_py_client.models.position import Position
from touroptimizer_py_client.models.route_element_detail import RouteElementDetail
from touroptimizer_py_client.models.route_header import RouteHeader
from touroptimizer_py_client.models.route_trip import RouteTrip
from typing import Optional, Set
from typing_extensions import Self

class Route(BaseModel):
    """
    A single route within the optimization solution. Assigns a resource to a sequence of nodes with full scheduling details. Contains the route header (KPIs), start/end elements and positions, lists of optimizable, non-optimizable, optional, and pillar element ids, per-element scheduling details, and route-level flags.
    """ # noqa: E501
    header: Optional[RouteHeader] = None
    id: StrictInt = Field(description="The id is an optimizer provided number identifiying a route.")
    resource_id: StrictStr = Field(description="The resourceId of the Visitor owning this route.", alias="resourceId")
    route_trip: Optional[RouteTrip] = Field(default=None, alias="routeTrip")
    start_time: datetime = Field(description="The startTime of the route. This is usually the start of the workingHours of the Resource. However, when using flextime/reduction-time the starttime can be different from the working hours start.", alias="startTime")
    start_element_id: StrictStr = Field(description="The startElementId, is the element from where the route starts. By default, it is the Resource itself.", alias="startElementId")
    start_position: Optional[Position] = Field(default=None, alias="startPosition")
    end_element_id: StrictStr = Field(description="The endElementId, is the element where the route stops. By default, it is the Resource itself.", alias="endElementId")
    end_position: Optional[Position] = Field(default=None, alias="endPosition")
    optimizable_element_ids: List[StrictStr] = Field(description="The optimizableElementIds. The list of optimizable elements that are part of the route.", alias="optimizableElementIds")
    non_optimizable_element_ids: List[StrictStr] = Field(description="The nonOptimizableElementIds. The list of non-optimizable elements that are part of the route.", alias="nonOptimizableElementIds")
    optional_optimizable_element_ids: List[StrictStr] = Field(description="The optionalOptimizableElementIds. The list of optional elements that are part of the route.", alias="optionalOptimizableElementIds")
    pillar_element_ids: List[StrictStr] = Field(description="The pillarElementIds. The list of pillar elements that are part of the route.", alias="pillarElementIds")
    element_details: List[RouteElementDetail] = Field(description="The elementDetails. The list of details describing the route schedule.", alias="elementDetails")
    pillar_latest_effective_arrival_offset_map: Optional[Dict[str, StrictInt]] = Field(default=None, description="The pillarLatestEffectiveArrivalOffsetMap. A map of additional time offsets for pillar elements. Each pillar has a latest possible arrival. As a route can consist of multiple pillars, the latest arrival at a certain pillar is also a function of  subsequent pillars. This latest arrival may shifted to a later time spot to allow shifitig a pillar around a normal node, even the normal node would fit before the pillar.", alias="pillarLatestEffectiveArrivalOffsetMap")
    flags: Optional[List[StrictStr]] = Field(default=None, description="The flags. A list of flags indicating statii like which source finalized a route.")
    additional_route_start_offset: Optional[StrictInt] = Field(default=None, description="The additionalRouteStartOffset", alias="additionalRouteStartOffset")
    is_locked_down: Optional[StrictBool] = Field(default=None, description="The isLockedDown. Describes if a route was undergoing lockdown.", alias="isLockedDown")
    is_inactive: Optional[StrictBool] = Field(default=None, description="The isInactive boolean describes if a route is deactivated.", alias="isInactive")
    is_finalized: Optional[StrictBool] = Field(default=None, description="The isFinalized. Describes if a route was undergoing finalization.", alias="isFinalized")
    __properties: ClassVar[List[str]] = ["header", "id", "resourceId", "routeTrip", "startTime", "startElementId", "startPosition", "endElementId", "endPosition", "optimizableElementIds", "nonOptimizableElementIds", "optionalOptimizableElementIds", "pillarElementIds", "elementDetails", "pillarLatestEffectiveArrivalOffsetMap", "flags", "additionalRouteStartOffset", "isLockedDown", "isInactive", "isFinalized"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['FINALIZED_PILLARFORCEARRANGER', 'INACTIVE_PILLARFORCEARRANGER', 'FINALIZED_ROUTE_FINALIZER', 'INACTIVE_ROUTE_FINALIZER']):
                raise ValueError("each list item must be one of ('FINALIZED_PILLARFORCEARRANGER', 'INACTIVE_PILLARFORCEARRANGER', 'FINALIZED_ROUTE_FINALIZER', 'INACTIVE_ROUTE_FINALIZER')")
        return value

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
        """Create an instance of Route from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of header
        if self.header:
            _dict['header'] = self.header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of route_trip
        if self.route_trip:
            _dict['routeTrip'] = self.route_trip.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_position
        if self.start_position:
            _dict['startPosition'] = self.start_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_position
        if self.end_position:
            _dict['endPosition'] = self.end_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in element_details (list)
        _items = []
        if self.element_details:
            for _item_element_details in self.element_details:
                if _item_element_details:
                    _items.append(_item_element_details.to_dict())
            _dict['elementDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Route from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "header": RouteHeader.from_dict(obj["header"]) if obj.get("header") is not None else None,
            "id": obj.get("id"),
            "resourceId": obj.get("resourceId"),
            "routeTrip": RouteTrip.from_dict(obj["routeTrip"]) if obj.get("routeTrip") is not None else None,
            "startTime": obj.get("startTime"),
            "startElementId": obj.get("startElementId"),
            "startPosition": Position.from_dict(obj["startPosition"]) if obj.get("startPosition") is not None else None,
            "endElementId": obj.get("endElementId"),
            "endPosition": Position.from_dict(obj["endPosition"]) if obj.get("endPosition") is not None else None,
            "optimizableElementIds": obj.get("optimizableElementIds"),
            "nonOptimizableElementIds": obj.get("nonOptimizableElementIds"),
            "optionalOptimizableElementIds": obj.get("optionalOptimizableElementIds"),
            "pillarElementIds": obj.get("pillarElementIds"),
            "elementDetails": [RouteElementDetail.from_dict(_item) for _item in obj["elementDetails"]] if obj.get("elementDetails") is not None else None,
            "pillarLatestEffectiveArrivalOffsetMap": obj.get("pillarLatestEffectiveArrivalOffsetMap"),
            "flags": obj.get("flags"),
            "additionalRouteStartOffset": obj.get("additionalRouteStartOffset"),
            "isLockedDown": obj.get("isLockedDown"),
            "isInactive": obj.get("isInactive"),
            "isFinalized": obj.get("isFinalized")
        })
        return _obj


