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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from touroptimizer_py_client.models.core_build_options import CoreBuildOptions
from touroptimizer_py_client.models.element_connection import ElementConnection
from touroptimizer_py_client.models.json_config import JSONConfig
from touroptimizer_py_client.models.node import Node
from touroptimizer_py_client.models.node_relation import NodeRelation
from touroptimizer_py_client.models.optimization_options import OptimizationOptions
from touroptimizer_py_client.models.optimization_status import OptimizationStatus
from touroptimizer_py_client.models.resource import Resource
from touroptimizer_py_client.models.solution import Solution
from touroptimizer_py_client.models.type_dictionaries import TypeDictionaries
from touroptimizer_py_client.models.zone_connection import ZoneConnection
from typing import Optional, Set
from typing_extensions import Self

class RestOptimization(BaseModel):
    """
    The REST-specific specialization of OptimizationConfig with JSONConfig as the extension type. This is the top-level request/response object for the TourOptimizer REST API. Inherits all fields from OptimizationConfig and adds JSON-specific extension support for license keys, persistence settings, creator settings, and timeout configuration.
    """ # noqa: E501
    optimization_status: Optional[OptimizationStatus] = Field(default=None, alias="optimizationStatus")
    id: Optional[StrictStr] = Field(default=None, description="A system-generated unique identifier assigned by the persistence layer (e.g. MongoDB ObjectId). This field is read-only and will be populated automatically when the optimization snapshot is stored in the database. Clients may use this value together with the creator field to retrieve or reference a specific persisted snapshot.")
    created_time_stamp: Optional[StrictInt] = Field(default=None, description="An epoch-millisecond timestamp recording when this optimization snapshot was created. Populated automatically by the server at persistence time. Used for chronological ordering and expiry management Do not set this field in the input — it will be overwritten.", alias="createdTimeStamp")
    creator: Optional[StrictStr] = Field(default=None, description="A tenant-scoped identifier for the entity that submitted this optimization. Typically derived as a SHA-256 hash of the creator name supplied in the request's creatorSetting. Used as the primary scoping key for database queries — all persistence read operations require the creator to match, ensuring tenant isolation in multi-tenant deployments. Populated automatically by the server; do not set this field in the input.")
    ident: Optional[StrictStr] = Field(default=None, description="A user-defined, human-readable label for this optimization run. Useful for distinguishing runs in database queries and audit logs (e.g. 'Weekly-Route-Plan-CW42' or 'NightShift-Berlin'). If not provided, the server generates a default identifier based on a timestamp. Note: this field is stored as unencrypted metadata even when payload encryption is enabled — avoid embedding sensitive business information.")
    nodes: List[Node] = Field(description="The list of nodes (work items, customer locations, or events) to be scheduled and assigned to resources. Each node defines a geographic or event-based location, one or more opening-hour windows, a required visit duration, and optional constraints (skill requirements, resource bindings, priority, pickup-and-delivery loads). Every node id must be globally unique across all nodes and resources in this configuration.")
    resources: List[Resource] = Field(description="The list of resources (vehicles, drivers, technicians, or other mobile agents) available to visit the defined nodes. Each resource specifies a home position, one or more working-hour windows, maximum working time and distance constraints, optional qualifications (skills), an optional alternate destination, and overnight-stay policies. Resource ids must be globally unique across all elements.")
    node_relations: Optional[List[NodeRelation]] = Field(default=None, description="The list of inter-node relations that impose ordering or co-assignment constraints between nodes. Supported relation types include SAME_ROUTE (nodes must be on the same route), SAME_VISITOR (nodes must be served by the same resource), DIFFERENT_ROUTE (nodes must not share a route), and relative time-window relations that enforce temporal precedence (e.g. node A must be visited before node B within a defined time gap).", alias="nodeRelations")
    element_connections: Optional[List[ElementConnection]] = Field(default=None, description="Pre-computed pairwise connections between elements (nodes and resources). Each connection specifies the travel distance and time between a source and a target element, optionally including time-dependent traffic profiles via connectionByTime. If connections are not provided, the optimizer falls back to a Haversine-based distance approximation or a configured backup connector. Providing accurate connections significantly improves solution quality. In persisted results, this list may be omitted to conserve storage (controlled via saveConnections).", alias="elementConnections")
    zone_connections: Optional[List[ZoneConnection]] = Field(default=None, description="Zone connections define penalties or restrictions for crossing geographic zone boundaries (e.g. bridge tolls, tunnel crossings, or administrative borders). Each ZoneConnection specifies a pair of zone numbers and an associated crossing cost. When a route transitions between zones, the optimizer accumulates these costs, which discourages unnecessary zone crossings and promotes geographically cohesive routes.", alias="zoneConnections")
    type_dictionaries: Optional[TypeDictionaries] = Field(default=None, alias="typeDictionaries")
    optimization_options: Optional[OptimizationOptions] = Field(default=None, alias="optimizationOptions")
    core_build_options: Optional[CoreBuildOptions] = Field(default=None, alias="coreBuildOptions")
    solution: Optional[Solution] = None
    extension: Optional[JSONConfig] = None
    __properties: ClassVar[List[str]] = ["optimizationStatus", "id", "createdTimeStamp", "creator", "ident", "nodes", "resources", "nodeRelations", "elementConnections", "zoneConnections", "typeDictionaries", "optimizationOptions", "coreBuildOptions", "solution", "extension"]

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
        """Create an instance of RestOptimization from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of optimization_status
        if self.optimization_status:
            _dict['optimizationStatus'] = self.optimization_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item_nodes in self.nodes:
                if _item_nodes:
                    _items.append(_item_nodes.to_dict())
            _dict['nodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in node_relations (list)
        _items = []
        if self.node_relations:
            for _item_node_relations in self.node_relations:
                if _item_node_relations:
                    _items.append(_item_node_relations.to_dict())
            _dict['nodeRelations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in element_connections (list)
        _items = []
        if self.element_connections:
            for _item_element_connections in self.element_connections:
                if _item_element_connections:
                    _items.append(_item_element_connections.to_dict())
            _dict['elementConnections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zone_connections (list)
        _items = []
        if self.zone_connections:
            for _item_zone_connections in self.zone_connections:
                if _item_zone_connections:
                    _items.append(_item_zone_connections.to_dict())
            _dict['zoneConnections'] = _items
        # override the default output from pydantic by calling `to_dict()` of type_dictionaries
        if self.type_dictionaries:
            _dict['typeDictionaries'] = self.type_dictionaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of optimization_options
        if self.optimization_options:
            _dict['optimizationOptions'] = self.optimization_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of core_build_options
        if self.core_build_options:
            _dict['coreBuildOptions'] = self.core_build_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of solution
        if self.solution:
            _dict['solution'] = self.solution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extension
        if self.extension:
            _dict['extension'] = self.extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestOptimization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "optimizationStatus": OptimizationStatus.from_dict(obj["optimizationStatus"]) if obj.get("optimizationStatus") is not None else None,
            "id": obj.get("id"),
            "createdTimeStamp": obj.get("createdTimeStamp"),
            "creator": obj.get("creator"),
            "ident": obj.get("ident"),
            "nodes": [Node.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "resources": [Resource.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None,
            "nodeRelations": [NodeRelation.from_dict(_item) for _item in obj["nodeRelations"]] if obj.get("nodeRelations") is not None else None,
            "elementConnections": [ElementConnection.from_dict(_item) for _item in obj["elementConnections"]] if obj.get("elementConnections") is not None else None,
            "zoneConnections": [ZoneConnection.from_dict(_item) for _item in obj["zoneConnections"]] if obj.get("zoneConnections") is not None else None,
            "typeDictionaries": TypeDictionaries.from_dict(obj["typeDictionaries"]) if obj.get("typeDictionaries") is not None else None,
            "optimizationOptions": OptimizationOptions.from_dict(obj["optimizationOptions"]) if obj.get("optimizationOptions") is not None else None,
            "coreBuildOptions": CoreBuildOptions.from_dict(obj["coreBuildOptions"]) if obj.get("coreBuildOptions") is not None else None,
            "solution": Solution.from_dict(obj["solution"]) if obj.get("solution") is not None else None,
            "extension": JSONConfig.from_dict(obj["extension"]) if obj.get("extension") is not None else None
        })
        return _obj


