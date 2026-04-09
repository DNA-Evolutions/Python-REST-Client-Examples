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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from touroptimizer_py_client.models.absolute_node_color_multi_route_constraint import AbsoluteNodeColorMultiRouteConstraint
    from touroptimizer_py_client.models.binding_resource_constraint import BindingResourceConstraint
    from touroptimizer_py_client.models.bit_type_constraint import BitTypeConstraint
    from touroptimizer_py_client.models.bit_type_with_expertise_constraint import BitTypeWithExpertiseConstraint
    from touroptimizer_py_client.models.connected_constraint import ConnectedConstraint
    from touroptimizer_py_client.models.excluding_resource_constraint import ExcludingResourceConstraint
    from touroptimizer_py_client.models.magneto_node_constraint import MagnetoNodeConstraint
    from touroptimizer_py_client.models.node_color_multi_route_constraint import NodeColorMultiRouteConstraint
    from touroptimizer_py_client.models.resource_location_constraint import ResourceLocationConstraint
    from touroptimizer_py_client.models.type_constraint import TypeConstraint
    from touroptimizer_py_client.models.type_with_expertise_constraint import TypeWithExpertiseConstraint
    from touroptimizer_py_client.models.uk_post_code_constraint import UKPostCodeConstraint
    from touroptimizer_py_client.models.zone_number_constraint import ZoneNumberConstraint

class ConstraintType(BaseModel):
    """
    A node-level constraint that restricts which resources may visit a node, or penalizes undesirable assignments. Subtypes include binding/excluding resource constraints, type-based skill matching (with optional expertise levels and cost models), zone number and UK post code territory constraints, magneto (node-to-node attraction/repulsion) constraints, and multi-route node color constraints.
    """ # noqa: E501
    type_name: StrictStr = Field(alias="typeName")
    __properties: ClassVar[List[str]] = ["typeName"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'AbsoluteNodeColorMultiRouteConstraint': 'AbsoluteNodeColorMultiRouteConstraint','BindingResource': 'BindingResourceConstraint','BitType': 'BitTypeConstraint','BitTypeWithExpertise': 'BitTypeWithExpertiseConstraint','ConnectedConstraint': 'ConnectedConstraint','ExcludingResource': 'ExcludingResourceConstraint','MagnetoNode': 'MagnetoNodeConstraint','NodeColorMultiRouteConstraint': 'NodeColorMultiRouteConstraint','ResourceLocationConstraint': 'ResourceLocationConstraint','Type': 'TypeConstraint','TypeWithExpertise': 'TypeWithExpertiseConstraint','UKPostCodeConstraint': 'UKPostCodeConstraint','ZoneNumberConstraint': 'ZoneNumberConstraint'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AbsoluteNodeColorMultiRouteConstraint, BindingResourceConstraint, BitTypeConstraint, BitTypeWithExpertiseConstraint, ConnectedConstraint, ExcludingResourceConstraint, MagnetoNodeConstraint, NodeColorMultiRouteConstraint, ResourceLocationConstraint, TypeConstraint, TypeWithExpertiseConstraint, UKPostCodeConstraint, ZoneNumberConstraint]]:
        """Create an instance of ConstraintType from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AbsoluteNodeColorMultiRouteConstraint, BindingResourceConstraint, BitTypeConstraint, BitTypeWithExpertiseConstraint, ConnectedConstraint, ExcludingResourceConstraint, MagnetoNodeConstraint, NodeColorMultiRouteConstraint, ResourceLocationConstraint, TypeConstraint, TypeWithExpertiseConstraint, UKPostCodeConstraint, ZoneNumberConstraint]]:
        """Create an instance of ConstraintType from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AbsoluteNodeColorMultiRouteConstraint':
            return import_module("touroptimizer_py_client.models.absolute_node_color_multi_route_constraint").AbsoluteNodeColorMultiRouteConstraint.from_dict(obj)
        if object_type ==  'BindingResourceConstraint':
            return import_module("touroptimizer_py_client.models.binding_resource_constraint").BindingResourceConstraint.from_dict(obj)
        if object_type ==  'BitTypeConstraint':
            return import_module("touroptimizer_py_client.models.bit_type_constraint").BitTypeConstraint.from_dict(obj)
        if object_type ==  'BitTypeWithExpertiseConstraint':
            return import_module("touroptimizer_py_client.models.bit_type_with_expertise_constraint").BitTypeWithExpertiseConstraint.from_dict(obj)
        if object_type ==  'ConnectedConstraint':
            return import_module("touroptimizer_py_client.models.connected_constraint").ConnectedConstraint.from_dict(obj)
        if object_type ==  'ExcludingResourceConstraint':
            return import_module("touroptimizer_py_client.models.excluding_resource_constraint").ExcludingResourceConstraint.from_dict(obj)
        if object_type ==  'MagnetoNodeConstraint':
            return import_module("touroptimizer_py_client.models.magneto_node_constraint").MagnetoNodeConstraint.from_dict(obj)
        if object_type ==  'NodeColorMultiRouteConstraint':
            return import_module("touroptimizer_py_client.models.node_color_multi_route_constraint").NodeColorMultiRouteConstraint.from_dict(obj)
        if object_type ==  'ResourceLocationConstraint':
            return import_module("touroptimizer_py_client.models.resource_location_constraint").ResourceLocationConstraint.from_dict(obj)
        if object_type ==  'TypeConstraint':
            return import_module("touroptimizer_py_client.models.type_constraint").TypeConstraint.from_dict(obj)
        if object_type ==  'TypeWithExpertiseConstraint':
            return import_module("touroptimizer_py_client.models.type_with_expertise_constraint").TypeWithExpertiseConstraint.from_dict(obj)
        if object_type ==  'UKPostCodeConstraint':
            return import_module("touroptimizer_py_client.models.uk_post_code_constraint").UKPostCodeConstraint.from_dict(obj)
        if object_type ==  'ZoneNumberConstraint':
            return import_module("touroptimizer_py_client.models.zone_number_constraint").ZoneNumberConstraint.from_dict(obj)

        raise ValueError("ConstraintType failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


