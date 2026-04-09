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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from touroptimizer_py_client.models.optimization_persistence_strategy_setting import OptimizationPersistenceStrategySetting
from touroptimizer_py_client.models.stream_persistence_strategy_setting import StreamPersistenceStrategySetting
from typing import Optional, Set
from typing_extensions import Self

class MongoOptimizationPersistenceSetting(BaseModel):
    """
    The mongoSettings
    """ # noqa: E501
    enable_persistence: StrictBool = Field(description="The enablePersistence", alias="enablePersistence")
    require_unique_ident_creator_combination: StrictBool = Field(description="The requireUniqueIdentCreatorCombination", alias="requireUniqueIdentCreatorCombination")
    secret: StrictStr = Field(description="The secret that encrypts the result. If empty, no encryption is assigned. Important: Metadata and stream information like progress is always saved as decrypted clear text. Attention: The secret is not saved by DNA evolutions. If you loose the secret, the file CAN NOT be restored.")
    expiry: Optional[StrictStr] = Field(default=None, description="The document will be automatically deleted after this duration. The default value is 48 hours.")
    optimization_persistence_strategy_setting: OptimizationPersistenceStrategySetting = Field(alias="optimizationPersistenceStrategySetting")
    stream_persistence_strategy_setting: StreamPersistenceStrategySetting = Field(alias="streamPersistenceStrategySetting")
    completion_webhook_url: Optional[StrictStr] = Field(default=None, description="Optional URL the server calls (POST) when the job completes or fails. The payload contains jobId, tenantId, status, and completedAt only — no optimization data. Leave empty to disable. URL validation is controlled by the server's webhook-validation policy: in strict mode (SaaS default) only public HTTPS URLs are accepted; in relaxed mode (on-premise) HTTP and private network addresses are also allowed; in none mode (local development) any URL is accepted. Loopback addresses (127.x, ::1) are always rejected. Validation is performed at submission time.", alias="completionWebhookUrl")
    completion_webhook_secret: Optional[StrictStr] = Field(default=None, description="Optional secret used to sign the webhook payload with HMAC-SHA256. When provided, the server includes an X-JOpt-Signature header on every delivery in the form 'sha256=<hex>'. The receiver should compute the same HMAC over the raw request body and compare it using a constant-time comparison before trusting the payload. Leave empty to send unsigned webhooks. Unsigned webhooks are acceptable in trusted internal networks but are not recommended when the webhook URL is reachable from untrusted clients.", alias="completionWebhookSecret")
    __properties: ClassVar[List[str]] = ["enablePersistence", "requireUniqueIdentCreatorCombination", "secret", "expiry", "optimizationPersistenceStrategySetting", "streamPersistenceStrategySetting", "completionWebhookUrl", "completionWebhookSecret"]

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
        """Create an instance of MongoOptimizationPersistenceSetting from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of optimization_persistence_strategy_setting
        if self.optimization_persistence_strategy_setting:
            _dict['optimizationPersistenceStrategySetting'] = self.optimization_persistence_strategy_setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stream_persistence_strategy_setting
        if self.stream_persistence_strategy_setting:
            _dict['streamPersistenceStrategySetting'] = self.stream_persistence_strategy_setting.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MongoOptimizationPersistenceSetting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enablePersistence": obj.get("enablePersistence"),
            "requireUniqueIdentCreatorCombination": obj.get("requireUniqueIdentCreatorCombination"),
            "secret": obj.get("secret"),
            "expiry": obj.get("expiry"),
            "optimizationPersistenceStrategySetting": OptimizationPersistenceStrategySetting.from_dict(obj["optimizationPersistenceStrategySetting"]) if obj.get("optimizationPersistenceStrategySetting") is not None else None,
            "streamPersistenceStrategySetting": StreamPersistenceStrategySetting.from_dict(obj["streamPersistenceStrategySetting"]) if obj.get("streamPersistenceStrategySetting") is not None else None,
            "completionWebhookUrl": obj.get("completionWebhookUrl"),
            "completionWebhookSecret": obj.get("completionWebhookSecret")
        })
        return _obj


