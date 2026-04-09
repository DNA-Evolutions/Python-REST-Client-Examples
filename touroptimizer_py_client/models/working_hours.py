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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from touroptimizer_py_client.models.constraint import Constraint
from touroptimizer_py_client.models.construction_hook import ConstructionHook
from touroptimizer_py_client.models.node_color_capacity import NodeColorCapacity
from touroptimizer_py_client.models.qualification import Qualification
from touroptimizer_py_client.models.reduced_node_edge_connector_item import ReducedNodeEdgeConnectorItem
from touroptimizer_py_client.models.start_reduction_time_definition import StartReductionTimeDefinition
from touroptimizer_py_client.models.start_reduction_time_include_definition import StartReductionTimeIncludeDefinition
from touroptimizer_py_client.models.start_reduction_time_pillar_definition import StartReductionTimePillarDefinition
from touroptimizer_py_client.models.stay_out_cycle_definition import StayOutCycleDefinition
from typing import Optional, Set
from typing_extensions import Self

class WorkingHours(BaseModel):
    """
    A time window during which a resource is available for work. Defined by a begin and end instant with a time zone. Supports maximum working time and distance constraints, overtime/overdistance allowances, start-reduction-time (flex-time) policies, stay-out (overnight) definitions, node color capacities, and optional qualifications and depot configurations per working-hour window.
    """ # noqa: E501
    begin: datetime = Field(description="The begin of the Working hours.")
    end: datetime = Field(description="The end of the Working hours.")
    zone_id: StrictStr = Field(description="The zoneId of the Working hours.", alias="zoneId")
    max_time: Optional[StrictStr] = Field(default=None, description="The maximal time a Resource should work within the WorkingHour.", alias="maxTime")
    max_distance: Optional[StrictStr] = Field(default=None, description="The maximla distance a resource should cover within the WorkingHour.", alias="maxDistance")
    stay_out_cycle_definition: Optional[StayOutCycleDefinition] = Field(default=None, alias="stayOutCycleDefinition")
    start_reduction_time_definition: Optional[StartReductionTimeDefinition] = Field(default=None, alias="startReductionTimeDefinition")
    start_reduction_time_pillar_definition: Optional[StartReductionTimePillarDefinition] = Field(default=None, alias="startReductionTimePillarDefinition")
    start_reduction_time_include_definition: Optional[StartReductionTimeIncludeDefinition] = Field(default=None, alias="startReductionTimeIncludeDefinition")
    local_flex_time: Optional[StrictStr] = Field(default=None, description="The local flexible time. In some cases a Resource should start working later compared to what is defined in the working hours. This way idle time can be reduced. The local flex time is the maximum a Resource is allowed to start working later, depending on the Optimization maybe flex time is not or only partially used.", alias="localFlexTime")
    local_post_flex_time: Optional[StrictStr] = Field(default=None, description="The maximum duration by which the resource is allowed to end work earlier than the working-hour boundary. Acts as a flexible end-of-shift buffer — if the last node finishes ahead of schedule, the resource may clock off early by up to this amount, reducing unnecessary idle time at the end of the route. See also localPostFlexTimeOnlyOnOvertime to restrict this behavior to overtime-reduction scenarios only.", alias="localPostFlexTime")
    local_post_flex_time_only_on_overtime: Optional[StrictBool] = Field(default=False, description="The post flextime is only applied to reduce overtime.", alias="localPostFlexTimeOnlyOnOvertime")
    max_local_pillar_after_hours_time: Optional[StrictStr] = Field(default=None, description="The maximum duration a pillar node is allowed to be served after the official working-hours end for this specific working-hour window. Enables late-shift mandatory stops (e.g. end-of-day depot return) that extend slightly beyond the defined working-hour boundary.", alias="maxLocalPillarAfterHoursTime")
    node_color_capacities: Optional[List[NodeColorCapacity]] = Field(default=None, description="Per-color capacity limits for routes produced from this working hour. Controls the composition of the route by limiting how many nodes of a given color category may appear (e.g. at most 40% hazardous-goods stops). Overrides any resource-level color capacity when set at the working-hour level.", alias="nodeColorCapacities")
    working_hours_constraints: Optional[List[Constraint]] = Field(default=None, description="The constraints for this working hour.", alias="workingHoursConstraints")
    multi_working_hours_constraints: Optional[List[Constraint]] = Field(default=None, description="Constraints that span across multiple working hours of the same resource. Unlike workingHoursConstraints (which apply to a single working-hour window), these constraints enforce policies across the full planning horizon — for example, limiting the total number of a certain node type visited across all days.", alias="multiWorkingHoursConstraints")
    construction_hooks: Optional[List[ConstructionHook]] = Field(default=None, description="The hooks for this working hour.", alias="constructionHooks")
    qualifications: Optional[List[Qualification]] = Field(default=None, description="The qualification of the Resource for this working hour. For example, the Resource is allowed to visit a node needing a skill (defined via a constraint) and the Resource is providing this skill.")
    route_start_time_hook: Optional[StrictStr] = Field(default=None, description="An optional time offset applied to the route start. Shifts the effective departure time from the resource's home location, for example to account for vehicle preparation, warm-up, or loading time before the first stop.", alias="routeStartTimeHook")
    hook_element_connections: Optional[List[ReducedNodeEdgeConnectorItem]] = Field(default=None, description="Pre-computed connections used exclusively during the construction hook phase. These connections override the default element connections for hook-related routing decisions, allowing special distance/time calculations during construction (e.g. depot-to-first-stop distances that differ from normal driving).", alias="hookElementConnections")
    is_local_service_hub: Optional[StrictBool] = Field(default=False, description="If true, this resource operates in service-hub mode during this working hour: instead of the resource traveling to visit nodes, nodes are conceptually 'brought to' the resource's location. Useful for modeling stationary service points, reception desks, or warehouse processing stations.", alias="isLocalServiceHub")
    is_closed_route: Optional[StrictBool] = Field(default=True, description="The isClosedRoute boolean describes if a Resource has to visit the termination element of the Route. By default, the start element and the termination element of a Route is the Resource itself. In case of a closed route, by default, the Resource returns to its original starting location.", alias="isClosedRoute")
    is_available_for_stay: Optional[StrictBool] = Field(default=False, description="The boolean isAvailableForStay defines if this working hour is allowed to end at an overnight stay.", alias="isAvailableForStay")
    __properties: ClassVar[List[str]] = ["begin", "end", "zoneId", "maxTime", "maxDistance", "stayOutCycleDefinition", "startReductionTimeDefinition", "startReductionTimePillarDefinition", "startReductionTimeIncludeDefinition", "localFlexTime", "localPostFlexTime", "localPostFlexTimeOnlyOnOvertime", "maxLocalPillarAfterHoursTime", "nodeColorCapacities", "workingHoursConstraints", "multiWorkingHoursConstraints", "constructionHooks", "qualifications", "routeStartTimeHook", "hookElementConnections", "isLocalServiceHub", "isClosedRoute", "isAvailableForStay"]

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
        """Create an instance of WorkingHours from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stay_out_cycle_definition
        if self.stay_out_cycle_definition:
            _dict['stayOutCycleDefinition'] = self.stay_out_cycle_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_reduction_time_definition
        if self.start_reduction_time_definition:
            _dict['startReductionTimeDefinition'] = self.start_reduction_time_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_reduction_time_pillar_definition
        if self.start_reduction_time_pillar_definition:
            _dict['startReductionTimePillarDefinition'] = self.start_reduction_time_pillar_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_reduction_time_include_definition
        if self.start_reduction_time_include_definition:
            _dict['startReductionTimeIncludeDefinition'] = self.start_reduction_time_include_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_color_capacities (list)
        _items = []
        if self.node_color_capacities:
            for _item_node_color_capacities in self.node_color_capacities:
                if _item_node_color_capacities:
                    _items.append(_item_node_color_capacities.to_dict())
            _dict['nodeColorCapacities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in working_hours_constraints (list)
        _items = []
        if self.working_hours_constraints:
            for _item_working_hours_constraints in self.working_hours_constraints:
                if _item_working_hours_constraints:
                    _items.append(_item_working_hours_constraints.to_dict())
            _dict['workingHoursConstraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in multi_working_hours_constraints (list)
        _items = []
        if self.multi_working_hours_constraints:
            for _item_multi_working_hours_constraints in self.multi_working_hours_constraints:
                if _item_multi_working_hours_constraints:
                    _items.append(_item_multi_working_hours_constraints.to_dict())
            _dict['multiWorkingHoursConstraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in construction_hooks (list)
        _items = []
        if self.construction_hooks:
            for _item_construction_hooks in self.construction_hooks:
                if _item_construction_hooks:
                    _items.append(_item_construction_hooks.to_dict())
            _dict['constructionHooks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in qualifications (list)
        _items = []
        if self.qualifications:
            for _item_qualifications in self.qualifications:
                if _item_qualifications:
                    _items.append(_item_qualifications.to_dict())
            _dict['qualifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hook_element_connections (list)
        _items = []
        if self.hook_element_connections:
            for _item_hook_element_connections in self.hook_element_connections:
                if _item_hook_element_connections:
                    _items.append(_item_hook_element_connections.to_dict())
            _dict['hookElementConnections'] = _items
        # set to None if local_post_flex_time_only_on_overtime (nullable) is None
        # and model_fields_set contains the field
        if self.local_post_flex_time_only_on_overtime is None and "local_post_flex_time_only_on_overtime" in self.model_fields_set:
            _dict['localPostFlexTimeOnlyOnOvertime'] = None

        # set to None if is_local_service_hub (nullable) is None
        # and model_fields_set contains the field
        if self.is_local_service_hub is None and "is_local_service_hub" in self.model_fields_set:
            _dict['isLocalServiceHub'] = None

        # set to None if is_closed_route (nullable) is None
        # and model_fields_set contains the field
        if self.is_closed_route is None and "is_closed_route" in self.model_fields_set:
            _dict['isClosedRoute'] = None

        # set to None if is_available_for_stay (nullable) is None
        # and model_fields_set contains the field
        if self.is_available_for_stay is None and "is_available_for_stay" in self.model_fields_set:
            _dict['isAvailableForStay'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkingHours from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "begin": obj.get("begin"),
            "end": obj.get("end"),
            "zoneId": obj.get("zoneId"),
            "maxTime": obj.get("maxTime"),
            "maxDistance": obj.get("maxDistance"),
            "stayOutCycleDefinition": StayOutCycleDefinition.from_dict(obj["stayOutCycleDefinition"]) if obj.get("stayOutCycleDefinition") is not None else None,
            "startReductionTimeDefinition": StartReductionTimeDefinition.from_dict(obj["startReductionTimeDefinition"]) if obj.get("startReductionTimeDefinition") is not None else None,
            "startReductionTimePillarDefinition": StartReductionTimePillarDefinition.from_dict(obj["startReductionTimePillarDefinition"]) if obj.get("startReductionTimePillarDefinition") is not None else None,
            "startReductionTimeIncludeDefinition": StartReductionTimeIncludeDefinition.from_dict(obj["startReductionTimeIncludeDefinition"]) if obj.get("startReductionTimeIncludeDefinition") is not None else None,
            "localFlexTime": obj.get("localFlexTime"),
            "localPostFlexTime": obj.get("localPostFlexTime"),
            "localPostFlexTimeOnlyOnOvertime": obj.get("localPostFlexTimeOnlyOnOvertime") if obj.get("localPostFlexTimeOnlyOnOvertime") is not None else False,
            "maxLocalPillarAfterHoursTime": obj.get("maxLocalPillarAfterHoursTime"),
            "nodeColorCapacities": [NodeColorCapacity.from_dict(_item) for _item in obj["nodeColorCapacities"]] if obj.get("nodeColorCapacities") is not None else None,
            "workingHoursConstraints": [Constraint.from_dict(_item) for _item in obj["workingHoursConstraints"]] if obj.get("workingHoursConstraints") is not None else None,
            "multiWorkingHoursConstraints": [Constraint.from_dict(_item) for _item in obj["multiWorkingHoursConstraints"]] if obj.get("multiWorkingHoursConstraints") is not None else None,
            "constructionHooks": [ConstructionHook.from_dict(_item) for _item in obj["constructionHooks"]] if obj.get("constructionHooks") is not None else None,
            "qualifications": [Qualification.from_dict(_item) for _item in obj["qualifications"]] if obj.get("qualifications") is not None else None,
            "routeStartTimeHook": obj.get("routeStartTimeHook"),
            "hookElementConnections": [ReducedNodeEdgeConnectorItem.from_dict(_item) for _item in obj["hookElementConnections"]] if obj.get("hookElementConnections") is not None else None,
            "isLocalServiceHub": obj.get("isLocalServiceHub") if obj.get("isLocalServiceHub") is not None else False,
            "isClosedRoute": obj.get("isClosedRoute") if obj.get("isClosedRoute") is not None else True,
            "isAvailableForStay": obj.get("isAvailableForStay") if obj.get("isAvailableForStay") is not None else False
        })
        return _obj


