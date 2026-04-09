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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from touroptimizer_py_client.models.i_node_depot import INodeDepot
from touroptimizer_py_client.models.position import Position
from touroptimizer_py_client.models.violation import Violation
from typing import Optional, Set
from typing_extensions import Self

class RouteElementDetail(BaseModel):
    """
    The full scheduling record for a single node within a route. Extends the minimal timing data with idle time, transit time and distance to the next element, early/late arrival flags, per-node violations, schedule status, white-space (slack) information, and pickup-and-delivery load exchange details. One RouteElementDetail is produced per visited node in each route of the solution.
    """ # noqa: E501
    element_id: StrictStr = Field(description="The elementId that the detail item belongs to.", alias="elementId")
    start_time: datetime = Field(description="The startTime defines the time when a vistior (Resource) starts serving a node.", alias="startTime")
    arrival_time: datetime = Field(description="The arrivalTime defines the time when a vistior (Resource) arrives at a node. It is possible that a Visitior needs to idle at the node until a node opens.", alias="arrivalTime")
    departure_time: datetime = Field(description="The departureTime defines the time a resource is leaving a node.", alias="departureTime")
    transition_time: StrictStr = Field(description="The transitionTime gives the time taken for the connection from the previous element to this element.", alias="transitionTime")
    effective_position: Optional[Position] = Field(default=None, alias="effectivePosition")
    idle_time: StrictStr = Field(description="The idleTime is the time the Visitor has to wait until a node can be served. By default idle time arrises at the node to be visited. For example, a the arrival time of a Visitor is at 7 in the morning but the node opens at 8. The Visitor has to wait for one hour at the node location until the node can be served.", alias="idleTime")
    zone_id: StrictStr = Field(description="The zoneId of detail", alias="zoneId")
    white_space_idle_time: Optional[StrictStr] = Field(default=None, description="The whiteSpaceIdleTime only occurs if the Visitor is using a different reduction time definition for normal nodes and PillarNodes. It is usually introduced to avoid a violation where Pillars are allowed to be served before workingTime and Nodes are not.", alias="whiteSpaceIdleTime")
    duration_time: StrictStr = Field(description="The durationTime defines how long a node is serverd by a Visitor.", alias="durationTime")
    transition_distance: StrictStr = Field(description="The transitionDistance gives the distance taken for the connection from the previous element to this element.", alias="transitionDistance")
    choosen_working_hours_index: Optional[StrictInt] = Field(default=None, description="Each visitor can have a list of workingHours. The choosenWorkingHoursIndex is the index of the Visitors workingHour in which the element is visited.", alias="choosenWorkingHoursIndex")
    chosen_opening_hours_index: Optional[StrictInt] = Field(default=None, description="Each node can have a list of openingHours. The chosenOpeningHoursIndex is the index of the node openingHour in which the node is visited.", alias="chosenOpeningHoursIndex")
    early_deviation: Optional[StrictStr] = Field(default=None, description="The earlyDeviation. The early deviation describes how long before the element opens the Visitor arrives. If the value is negative, the Vistor arrives after the element already opens.", alias="earlyDeviation")
    late_deviation: Optional[StrictStr] = Field(default=None, description="The lateDeviation. The late deviation describes how much lateness the Vistor has. For example, the element to be visited is open from 8-11 and the desired visit duration is 2 hours. The Visitor has to arrive latest by 9 to finish the Job until 11. If the Visitor arrives at 10 the late deviation will be one hour, as the Visitor needs till 12 to finish the Job. The late deviation can be also negative indicating not beeing late. For example if the Visitor reaches the element by 8 and finishes the Job by 10 and the element closes at 11 the late deviation will be -1 hour.", alias="lateDeviation")
    schedule_status: Optional[StrictStr] = Field(default=None, description="The scheduleStatus.", alias="scheduleStatus")
    visitor_id: Optional[StrictStr] = Field(default=None, description="The visitorId. The id of the Visitor serving the element.", alias="visitorId")
    load_change: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="LEGACY: The change of the load of the element caused by the Visitor. For example, when the element requested 2 items and the Visitor provided only 1 item the loadChange value would be 1.", alias="loadChange")
    cur_capacity: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="LEGACY: The curCapacity of the visitor after visiting the element.", alias="curCapacity")
    before_visit_node_depot: Optional[INodeDepot] = Field(default=None, alias="beforeVisitNodeDepot")
    after_visit_node_depot: Optional[INodeDepot] = Field(default=None, alias="afterVisitNodeDepot")
    node_violations: Optional[List[Violation]] = Field(default=None, description="The nodeViolations. The violations collected at the element/node. For example, lateViolation, early violation etc.", alias="nodeViolations")
    is_unlocated_idle_time: Optional[StrictBool] = Field(default=None, description="The isUnlocatedIdleTime changes the representation of the idle time in the solution. By default idle time is located at the node to be waited for. If true, the idle time becomes unlocated. For example, a Visitor can reach a node (that opens at 8) by 7 in the morning. If the idle time is unlocated, the arrival time  will be represented as 8 (instead of 7). ", alias="isUnlocatedIdleTime")
    __properties: ClassVar[List[str]] = ["elementId", "startTime", "arrivalTime", "departureTime", "transitionTime", "effectivePosition", "idleTime", "zoneId", "whiteSpaceIdleTime", "durationTime", "transitionDistance", "choosenWorkingHoursIndex", "chosenOpeningHoursIndex", "earlyDeviation", "lateDeviation", "scheduleStatus", "visitorId", "loadChange", "curCapacity", "beforeVisitNodeDepot", "afterVisitNodeDepot", "nodeViolations", "isUnlocatedIdleTime"]

    @field_validator('schedule_status')
    def schedule_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNKNOWN', 'EARLY', 'IDLE', 'INTIME', 'LATE']):
            raise ValueError("must be one of enum values ('UNKNOWN', 'EARLY', 'IDLE', 'INTIME', 'LATE')")
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
        """Create an instance of RouteElementDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of effective_position
        if self.effective_position:
            _dict['effectivePosition'] = self.effective_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of before_visit_node_depot
        if self.before_visit_node_depot:
            _dict['beforeVisitNodeDepot'] = self.before_visit_node_depot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of after_visit_node_depot
        if self.after_visit_node_depot:
            _dict['afterVisitNodeDepot'] = self.after_visit_node_depot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_violations (list)
        _items = []
        if self.node_violations:
            for _item_node_violations in self.node_violations:
                if _item_node_violations:
                    _items.append(_item_node_violations.to_dict())
            _dict['nodeViolations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteElementDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "elementId": obj.get("elementId"),
            "startTime": obj.get("startTime"),
            "arrivalTime": obj.get("arrivalTime"),
            "departureTime": obj.get("departureTime"),
            "transitionTime": obj.get("transitionTime"),
            "effectivePosition": Position.from_dict(obj["effectivePosition"]) if obj.get("effectivePosition") is not None else None,
            "idleTime": obj.get("idleTime"),
            "zoneId": obj.get("zoneId"),
            "whiteSpaceIdleTime": obj.get("whiteSpaceIdleTime"),
            "durationTime": obj.get("durationTime"),
            "transitionDistance": obj.get("transitionDistance"),
            "choosenWorkingHoursIndex": obj.get("choosenWorkingHoursIndex"),
            "chosenOpeningHoursIndex": obj.get("chosenOpeningHoursIndex"),
            "earlyDeviation": obj.get("earlyDeviation"),
            "lateDeviation": obj.get("lateDeviation"),
            "scheduleStatus": obj.get("scheduleStatus"),
            "visitorId": obj.get("visitorId"),
            "loadChange": obj.get("loadChange"),
            "curCapacity": obj.get("curCapacity"),
            "beforeVisitNodeDepot": INodeDepot.from_dict(obj["beforeVisitNodeDepot"]) if obj.get("beforeVisitNodeDepot") is not None else None,
            "afterVisitNodeDepot": INodeDepot.from_dict(obj["afterVisitNodeDepot"]) if obj.get("afterVisitNodeDepot") is not None else None,
            "nodeViolations": [Violation.from_dict(_item) for _item in obj["nodeViolations"]] if obj.get("nodeViolations") is not None else None,
            "isUnlocatedIdleTime": obj.get("isUnlocatedIdleTime")
        })
        return _obj


