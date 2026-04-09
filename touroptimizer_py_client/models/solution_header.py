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


