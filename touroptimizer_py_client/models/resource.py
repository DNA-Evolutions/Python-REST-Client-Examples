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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from touroptimizer_py_client.models.constraint import Constraint
from touroptimizer_py_client.models.i_resource_depot import IResourceDepot
from touroptimizer_py_client.models.position import Position
from touroptimizer_py_client.models.qualification import Qualification
from touroptimizer_py_client.models.resource_type import ResourceType
from touroptimizer_py_client.models.start_reduction_time_definition import StartReductionTimeDefinition
from touroptimizer_py_client.models.start_reduction_time_include_definition import StartReductionTimeIncludeDefinition
from touroptimizer_py_client.models.start_reduction_time_pillar_definition import StartReductionTimePillarDefinition
from touroptimizer_py_client.models.stay_out_cycle_definition import StayOutCycleDefinition
from touroptimizer_py_client.models.stay_out_definition import StayOutDefinition
from touroptimizer_py_client.models.working_hours import WorkingHours
from typing import Optional, Set
from typing_extensions import Self

class Resource(BaseModel):
    """
    A mobile agent (vehicle, driver, technician) available to visit nodes. Defines a home position, one or more working-hour windows with time/distance constraints, optional qualifications (skills), an optional resource depot for pickup-and-delivery, connection efficiency factors, overnight-stay policies, and route configuration (open/closed, alternate destination, return-to-start).
    """ # noqa: E501
    id: StrictStr = Field(description="The unique id of the Resource. It is not possible, to create mutliple elements (also Nodes) with the same id.")
    extra_info: Optional[StrictStr] = Field(default=None, description="A custom extra info string that is attached to the Resource.", alias="extraInfo")
    location_id: Optional[StrictStr] = Field(default=None, description="The location id can relate a Resouce to the connection of another resource. See also locationId of Node.", alias="locationId")
    constraint_alias_id: Optional[StrictStr] = Field(default=None, description="The constraintAliasId. If set is used during constraint assessment instead of using the normal id.", alias="constraintAliasId")
    type: ResourceType
    position: Position
    working_hours: List[WorkingHours] = Field(description="The list of non-overlapping workingHours.", alias="workingHours")
    max_time: StrictStr = Field(description="The maxTime. The maximal time a Resource should work within the WorkingHour. This value is NOT logically coupled to the workingHours. For example, a working hour is defined from 8 in the morning till  5 in the afternoon and the maxTime is defined as 4 hours. In this situation an overime violation will be already  generated  when the Resource works from 8 till 1 (one hour of overtime). As JOpt supports flexible start times, the Resource might work from 12-4 (4 hours => not violation). The workingHour itself should be seen as a frame that is used primarily for matching WokingHours of Resources and OpeningHours of nodes. If no flexTime is used, the Resource will always start working at the beginning of its current working hours.", alias="maxTime")
    max_distance: StrictStr = Field(description="The maxDistance. The maximal distance a Resource is allowed to drive within a certain working hours.", alias="maxDistance")
    destination_position: Optional[Position] = Field(default=None, alias="destinationPosition")
    stay_out_definition: Optional[StayOutDefinition] = Field(default=None, alias="stayOutDefinition")
    stay_out_cycle_definition: Optional[StayOutCycleDefinition] = Field(default=None, alias="stayOutCycleDefinition")
    stay_out_policy_time: Optional[StrictStr] = Field(default=None, description="The maximum additional working time a resource is allowed to accumulate during an overnight-stay route beyond its normal working-hour boundaries. Acts as a buffer for late arrivals at stay nodes.", alias="stayOutPolicyTime")
    stay_out_policy_distance: Optional[StrictStr] = Field(default=None, description="The maximum additional driving distance a resource is allowed to accumulate during an overnight-stay route beyond its normal per-working-hour distance limit. Prevents the resource from driving excessively far to reach a stay node.", alias="stayOutPolicyDistance")
    capacity: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The multi-dimensional capacity vector of the resource (e.g. weight in kg, volume in m³, number of pallets). Each element represents the maximum capacity for one dimension. Used in pickup-and-delivery (PND) scenarios to enforce load constraints. The index positions must align with the load dimensions defined on the nodes.")
    initial_load: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The initial load the resource carries at the start of each route, per capacity dimension. For delivery scenarios, this represents the pre-loaded goods at the depot. For pickup scenarios, this is typically zero. Must have the same dimensionality as the capacity vector.", alias="initialLoad")
    min_degrated_capacity: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The minimum degraded capacity per dimension. As the resource visits more stops, its effective capacity may degrade (e.g. due to fatigue, compartment loss, or reorganization overhead). This vector defines the floor below which the capacity cannot degrade, regardless of the number of stops visited.", alias="minDegratedCapacity")
    capacity_deg_per_stop: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The capacity degradation per stop, per dimension. After each node visit, the resource's effective capacity is reduced by this amount (down to the minDegratedCapacity floor). Models real-world effects such as compartment unavailability after partial unloading or diminishing usable space.", alias="capacityDegPerStop")
    start_reduction_time_definition: Optional[StartReductionTimeDefinition] = Field(default=None, alias="startReductionTimeDefinition")
    start_reduction_time_pillar_definition: Optional[StartReductionTimePillarDefinition] = Field(default=None, alias="startReductionTimePillarDefinition")
    start_reduction_time_include_definition: Optional[StartReductionTimeIncludeDefinition] = Field(default=None, alias="startReductionTimeIncludeDefinition")
    flex_time: Optional[StrictStr] = Field(default=None, description="The local flexible time. In some cases a Resource should start working later compared to what is defined in the working hours. This way idle time can be reduced. The local flex time is the maximum a Resource is allowed to start working later, depending on the Optimization maybe flex time is not or only partially used.", alias="flexTime")
    post_flex_time: Optional[StrictStr] = Field(default=None, description="The maximum duration by which the resource is allowed to end its working day earlier than the working-hour boundary. Reduces unnecessary idle time at the end of a route. See also postFlexTimeOnlyOnOvertime to restrict usage to overtime-reduction scenarios.", alias="postFlexTime")
    post_flex_time_only_on_overtime: Optional[StrictBool] = Field(default=False, description="The post flextime is only applied to reduce overtime.", alias="postFlexTimeOnlyOnOvertime")
    max_pillar_after_hours_time: Optional[StrictStr] = Field(default=None, description="The maximum duration a pillar node may be served after the resource's official working-hours end. Applies globally across all working hours of this resource. For per-working-hour overrides, use maxLocalPillarAfterHoursTime on the individual WorkingHours object.", alias="maxPillarAfterHoursTime")
    max_drive_time_first_node: Optional[StrictStr] = Field(default=None, description="The maximum driving time allowed from the resource's start position to the first node of a route. Prevents the optimizer from assigning a distant first stop that would consume excessive travel time before productive work begins.", alias="maxDriveTimeFirstNode")
    max_drive_distance_first_node: Optional[StrictStr] = Field(default=None, description="The maximum driving distance allowed from the resource's start position to the first node of a route. Complements maxDriveTimeFirstNode to enforce both time- and distance-based proximity constraints.", alias="maxDriveDistanceFirstNode")
    max_drive_time_last_node: Optional[StrictStr] = Field(default=None, description="The maximum driving time allowed from the last visited node to the route termination element (typically the resource's home position or alternate destination). Prevents the optimizer from placing a final stop that would require an excessively long return journey.", alias="maxDriveTimeLastNode")
    max_drive_distance_last_node: Optional[StrictStr] = Field(default=None, description="The maximum driving distance allowed from the last visited node to the route termination element. Complements maxDriveTimeLastNode to enforce both time- and distance-based return constraints.", alias="maxDriveDistanceLastNode")
    kilometer_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The kilometerCost defines how much arbitrary cost arises per kilometer driven.", alias="kilometerCost")
    hour_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The hourCost defines how much arbitrary cost arises per hour scheduled (idling, working, driving).", alias="hourCost")
    production_hour_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The productionHourCost defines how much arbitrary cost arises per hour working.", alias="productionHourCost")
    fix_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The fixCost defines an abstract cost that arrises when this node is visited.", alias="fixCost")
    pre_work_driving_time: Optional[StrictStr] = Field(default=None, description="DEPRECATED. Use startReductionTimeDefinition instead. Legacy field that defined how long before the official working-hour start the resource was allowed to drive.", alias="preWorkDrivingTime")
    skill_efficiency_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="DEPRECATED. Use the visitDurationEfficiency mechanism on individual nodes and ResourceVisitDurationEfficiency instead. Legacy factor that scaled visit durations for this resource.", alias="skillEfficiencyFactor")
    acceptable_overtime: Optional[StrictStr] = Field(default=None, description="The acceptableOvertime. By default if nodes are constantly leading to overtime for a resource, at some point they might get unassigned (if AutoFilter is activated). The acceptable overtime assigns a margin to avoid filtering nodes if they lead to overtime below this margin. By defaul the property  'JoptAutoFilterWorkingHoursExceedMargin' can be used to globally define this value.", alias="acceptableOvertime")
    strict_overtime: Optional[StrictStr] = Field(default=None, description="The strictOvertime. By default if nodes are constantly leading to overtime for a resource, at some point they might get unassigned (if AutoFilter is activated). The strictOvertime overtime assigns a margin to avoid filtering nodes if they lead to overtime below this margin. By defaul the property  'JoptAutoFilterWorkingHoursStrictExceedMargin' can be used to globally define this value. In contrast to acceptable  overtime, the strict overtime is used during the last fitlering step of the AutoFilter (if strict mode is enabled).", alias="strictOvertime")
    acceptable_overdistance: Optional[StrictStr] = Field(default=None, description="The acceptableOverdistance. Like acceptableOvertime for distance.", alias="acceptableOverdistance")
    strict_overdistance: Optional[StrictStr] = Field(default=None, description="The strictOverdistance. Like strictOvertime for distance.", alias="strictOverdistance")
    average_speed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The averageSpeed of the Resource. By default this value is set to be 22[m/s] (79.2[km/h]). This value is mainly used, in case no external node connections are provided.", alias="averageSpeed")
    qualifications: Optional[List[Qualification]] = Field(default=None, description="The qualifications of the Resource.")
    constraints: Optional[List[Constraint]] = Field(default=None, description="The constraints  of the Resource")
    connection_time_efficiency_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=1.0, description="The connectionTimeEfficiencyFactor. The default time for passing a connection is devided by this factor. For example, if a connections needs 30 minutes to be passed by default, a Resource with a connectionTimeEfficiencyFactor of 1.5 only needs 20 minutes. By default this factor is one.", alias="connectionTimeEfficiencyFactor")
    co2emission_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The co2emissionFactor.", alias="co2emissionFactor")
    resource_depot: Optional[IResourceDepot] = Field(default=None, alias="resourceDepot")
    overall_visit_duration_efficiency: Optional[Union[StrictFloat, StrictInt]] = Field(default=1.0, description="The overallVisitDurationEfficiency. The base duration a Resource spends at a node is devided by this factor. For example, if a node has 30 minutes of visit duration assigned, a Resource with a overallVisitDurationEfficiency of 1.5 only needs 20 minutes. By default this factor is one.", alias="overallVisitDurationEfficiency")
    is_reduction_time_included_in_total_working_time: Optional[StrictBool] = Field(default=False, description="DEPRECATED. Use StartReductionTimeIncludeDefinition instead. Legacy flag that controlled whether reduction time was counted toward the resource's total working time.", alias="isReductionTimeIncludedInTotalWorkingTime")
    is_reduction_time_only_used_for_driving: Optional[StrictBool] = Field(default=False, description="DEPRECATED. Use startReductionTimeDefinition instead. Legacy flag that restricted reduction time to driving only (no working at the first node before the shift starts).", alias="isReductionTimeOnlyUsedForDriving")
    is_service_hub: Optional[StrictBool] = Field(default=False, description="A resource is hub mode gets visited by nodes.", alias="isServiceHub")
    __properties: ClassVar[List[str]] = ["id", "extraInfo", "locationId", "constraintAliasId", "type", "position", "workingHours", "maxTime", "maxDistance", "destinationPosition", "stayOutDefinition", "stayOutCycleDefinition", "stayOutPolicyTime", "stayOutPolicyDistance", "capacity", "initialLoad", "minDegratedCapacity", "capacityDegPerStop", "startReductionTimeDefinition", "startReductionTimePillarDefinition", "startReductionTimeIncludeDefinition", "flexTime", "postFlexTime", "postFlexTimeOnlyOnOvertime", "maxPillarAfterHoursTime", "maxDriveTimeFirstNode", "maxDriveDistanceFirstNode", "maxDriveTimeLastNode", "maxDriveDistanceLastNode", "kilometerCost", "hourCost", "productionHourCost", "fixCost", "preWorkDrivingTime", "skillEfficiencyFactor", "acceptableOvertime", "strictOvertime", "acceptableOverdistance", "strictOverdistance", "averageSpeed", "qualifications", "constraints", "connectionTimeEfficiencyFactor", "co2emissionFactor", "resourceDepot", "overallVisitDurationEfficiency", "isReductionTimeIncludedInTotalWorkingTime", "isReductionTimeOnlyUsedForDriving", "isServiceHub"]

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
        """Create an instance of Resource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in working_hours (list)
        _items = []
        if self.working_hours:
            for _item_working_hours in self.working_hours:
                if _item_working_hours:
                    _items.append(_item_working_hours.to_dict())
            _dict['workingHours'] = _items
        # override the default output from pydantic by calling `to_dict()` of destination_position
        if self.destination_position:
            _dict['destinationPosition'] = self.destination_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stay_out_definition
        if self.stay_out_definition:
            _dict['stayOutDefinition'] = self.stay_out_definition.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in qualifications (list)
        _items = []
        if self.qualifications:
            for _item_qualifications in self.qualifications:
                if _item_qualifications:
                    _items.append(_item_qualifications.to_dict())
            _dict['qualifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item_constraints in self.constraints:
                if _item_constraints:
                    _items.append(_item_constraints.to_dict())
            _dict['constraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of resource_depot
        if self.resource_depot:
            _dict['resourceDepot'] = self.resource_depot.to_dict()
        # set to None if post_flex_time_only_on_overtime (nullable) is None
        # and model_fields_set contains the field
        if self.post_flex_time_only_on_overtime is None and "post_flex_time_only_on_overtime" in self.model_fields_set:
            _dict['postFlexTimeOnlyOnOvertime'] = None

        # set to None if is_reduction_time_included_in_total_working_time (nullable) is None
        # and model_fields_set contains the field
        if self.is_reduction_time_included_in_total_working_time is None and "is_reduction_time_included_in_total_working_time" in self.model_fields_set:
            _dict['isReductionTimeIncludedInTotalWorkingTime'] = None

        # set to None if is_reduction_time_only_used_for_driving (nullable) is None
        # and model_fields_set contains the field
        if self.is_reduction_time_only_used_for_driving is None and "is_reduction_time_only_used_for_driving" in self.model_fields_set:
            _dict['isReductionTimeOnlyUsedForDriving'] = None

        # set to None if is_service_hub (nullable) is None
        # and model_fields_set contains the field
        if self.is_service_hub is None and "is_service_hub" in self.model_fields_set:
            _dict['isServiceHub'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Resource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "extraInfo": obj.get("extraInfo"),
            "locationId": obj.get("locationId"),
            "constraintAliasId": obj.get("constraintAliasId"),
            "type": ResourceType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "position": Position.from_dict(obj["position"]) if obj.get("position") is not None else None,
            "workingHours": [WorkingHours.from_dict(_item) for _item in obj["workingHours"]] if obj.get("workingHours") is not None else None,
            "maxTime": obj.get("maxTime"),
            "maxDistance": obj.get("maxDistance"),
            "destinationPosition": Position.from_dict(obj["destinationPosition"]) if obj.get("destinationPosition") is not None else None,
            "stayOutDefinition": StayOutDefinition.from_dict(obj["stayOutDefinition"]) if obj.get("stayOutDefinition") is not None else None,
            "stayOutCycleDefinition": StayOutCycleDefinition.from_dict(obj["stayOutCycleDefinition"]) if obj.get("stayOutCycleDefinition") is not None else None,
            "stayOutPolicyTime": obj.get("stayOutPolicyTime"),
            "stayOutPolicyDistance": obj.get("stayOutPolicyDistance"),
            "capacity": obj.get("capacity"),
            "initialLoad": obj.get("initialLoad"),
            "minDegratedCapacity": obj.get("minDegratedCapacity"),
            "capacityDegPerStop": obj.get("capacityDegPerStop"),
            "startReductionTimeDefinition": StartReductionTimeDefinition.from_dict(obj["startReductionTimeDefinition"]) if obj.get("startReductionTimeDefinition") is not None else None,
            "startReductionTimePillarDefinition": StartReductionTimePillarDefinition.from_dict(obj["startReductionTimePillarDefinition"]) if obj.get("startReductionTimePillarDefinition") is not None else None,
            "startReductionTimeIncludeDefinition": StartReductionTimeIncludeDefinition.from_dict(obj["startReductionTimeIncludeDefinition"]) if obj.get("startReductionTimeIncludeDefinition") is not None else None,
            "flexTime": obj.get("flexTime"),
            "postFlexTime": obj.get("postFlexTime"),
            "postFlexTimeOnlyOnOvertime": obj.get("postFlexTimeOnlyOnOvertime") if obj.get("postFlexTimeOnlyOnOvertime") is not None else False,
            "maxPillarAfterHoursTime": obj.get("maxPillarAfterHoursTime"),
            "maxDriveTimeFirstNode": obj.get("maxDriveTimeFirstNode"),
            "maxDriveDistanceFirstNode": obj.get("maxDriveDistanceFirstNode"),
            "maxDriveTimeLastNode": obj.get("maxDriveTimeLastNode"),
            "maxDriveDistanceLastNode": obj.get("maxDriveDistanceLastNode"),
            "kilometerCost": obj.get("kilometerCost"),
            "hourCost": obj.get("hourCost"),
            "productionHourCost": obj.get("productionHourCost"),
            "fixCost": obj.get("fixCost"),
            "preWorkDrivingTime": obj.get("preWorkDrivingTime"),
            "skillEfficiencyFactor": obj.get("skillEfficiencyFactor"),
            "acceptableOvertime": obj.get("acceptableOvertime"),
            "strictOvertime": obj.get("strictOvertime"),
            "acceptableOverdistance": obj.get("acceptableOverdistance"),
            "strictOverdistance": obj.get("strictOverdistance"),
            "averageSpeed": obj.get("averageSpeed"),
            "qualifications": [Qualification.from_dict(_item) for _item in obj["qualifications"]] if obj.get("qualifications") is not None else None,
            "constraints": [Constraint.from_dict(_item) for _item in obj["constraints"]] if obj.get("constraints") is not None else None,
            "connectionTimeEfficiencyFactor": obj.get("connectionTimeEfficiencyFactor") if obj.get("connectionTimeEfficiencyFactor") is not None else 1.0,
            "co2emissionFactor": obj.get("co2emissionFactor"),
            "resourceDepot": IResourceDepot.from_dict(obj["resourceDepot"]) if obj.get("resourceDepot") is not None else None,
            "overallVisitDurationEfficiency": obj.get("overallVisitDurationEfficiency") if obj.get("overallVisitDurationEfficiency") is not None else 1.0,
            "isReductionTimeIncludedInTotalWorkingTime": obj.get("isReductionTimeIncludedInTotalWorkingTime") if obj.get("isReductionTimeIncludedInTotalWorkingTime") is not None else False,
            "isReductionTimeOnlyUsedForDriving": obj.get("isReductionTimeOnlyUsedForDriving") if obj.get("isReductionTimeOnlyUsedForDriving") is not None else False,
            "isServiceHub": obj.get("isServiceHub") if obj.get("isServiceHub") is not None else False
        })
        return _obj


