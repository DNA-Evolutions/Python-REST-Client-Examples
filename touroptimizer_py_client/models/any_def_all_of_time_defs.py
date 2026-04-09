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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from touroptimizer_py_client.models.day import Day
from touroptimizer_py_client.models.day_month import DayMonth
from touroptimizer_py_client.models.day_month_year import DayMonthYear
from touroptimizer_py_client.models.range_day import RangeDay
from touroptimizer_py_client.models.range_day_month import RangeDayMonth
from touroptimizer_py_client.models.range_day_month_year import RangeDayMonthYear
from touroptimizer_py_client.models.range_week_day import RangeWeekDay
from touroptimizer_py_client.models.week_day import WeekDay
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ANYDEFALLOFTIMEDEFS_ONE_OF_SCHEMAS = ["AnyDef", "Day", "DayMonth", "DayMonthYear", "RangeDay", "RangeDayMonth", "RangeDayMonthYear", "RangeWeekDay", "WeekDay"]

class AnyDefAllOfTimeDefs(BaseModel):
    """
    AnyDefAllOfTimeDefs
    """
    # data type: AnyDef
    oneof_schema_1_validator: Optional[AnyDef] = None
    # data type: Day
    oneof_schema_2_validator: Optional[Day] = None
    # data type: DayMonth
    oneof_schema_3_validator: Optional[DayMonth] = None
    # data type: DayMonthYear
    oneof_schema_4_validator: Optional[DayMonthYear] = None
    # data type: RangeDay
    oneof_schema_5_validator: Optional[RangeDay] = None
    # data type: RangeDayMonth
    oneof_schema_6_validator: Optional[RangeDayMonth] = None
    # data type: RangeDayMonthYear
    oneof_schema_7_validator: Optional[RangeDayMonthYear] = None
    # data type: RangeWeekDay
    oneof_schema_8_validator: Optional[RangeWeekDay] = None
    # data type: WeekDay
    oneof_schema_9_validator: Optional[WeekDay] = None
    actual_instance: Optional[Union[AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay]] = None
    one_of_schemas: Set[str] = { "AnyDef", "Day", "DayMonth", "DayMonthYear", "RangeDay", "RangeDayMonth", "RangeDayMonthYear", "RangeWeekDay", "WeekDay" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = AnyDefAllOfTimeDefs.model_construct()
        error_messages = []
        match = 0
        # validate data type: AnyDef
        if not isinstance(v, AnyDef):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AnyDef`")
        else:
            match += 1
        # validate data type: Day
        if not isinstance(v, Day):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Day`")
        else:
            match += 1
        # validate data type: DayMonth
        if not isinstance(v, DayMonth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DayMonth`")
        else:
            match += 1
        # validate data type: DayMonthYear
        if not isinstance(v, DayMonthYear):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DayMonthYear`")
        else:
            match += 1
        # validate data type: RangeDay
        if not isinstance(v, RangeDay):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeDay`")
        else:
            match += 1
        # validate data type: RangeDayMonth
        if not isinstance(v, RangeDayMonth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeDayMonth`")
        else:
            match += 1
        # validate data type: RangeDayMonthYear
        if not isinstance(v, RangeDayMonthYear):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeDayMonthYear`")
        else:
            match += 1
        # validate data type: RangeWeekDay
        if not isinstance(v, RangeWeekDay):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeWeekDay`")
        else:
            match += 1
        # validate data type: WeekDay
        if not isinstance(v, WeekDay):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WeekDay`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AnyDefAllOfTimeDefs with oneOf schemas: AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AnyDefAllOfTimeDefs with oneOf schemas: AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("typeName")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `typeName` in the input.")

        # check if data type is `AnyDef`
        if _data_type == "Any":
            instance.actual_instance = AnyDef.from_json(json_str)
            return instance

        # check if data type is `Day`
        if _data_type == "Day":
            instance.actual_instance = Day.from_json(json_str)
            return instance

        # check if data type is `DayMonth`
        if _data_type == "DayMonth":
            instance.actual_instance = DayMonth.from_json(json_str)
            return instance

        # check if data type is `DayMonthYear`
        if _data_type == "DayMonthYear":
            instance.actual_instance = DayMonthYear.from_json(json_str)
            return instance

        # check if data type is `RangeDay`
        if _data_type == "Range.Day":
            instance.actual_instance = RangeDay.from_json(json_str)
            return instance

        # check if data type is `RangeDayMonth`
        if _data_type == "Range.DayMonth":
            instance.actual_instance = RangeDayMonth.from_json(json_str)
            return instance

        # check if data type is `RangeDayMonthYear`
        if _data_type == "Range.DayMonthYear":
            instance.actual_instance = RangeDayMonthYear.from_json(json_str)
            return instance

        # check if data type is `RangeWeekDay`
        if _data_type == "Range.WeekDay":
            instance.actual_instance = RangeWeekDay.from_json(json_str)
            return instance

        # check if data type is `WeekDay`
        if _data_type == "WeekDay":
            instance.actual_instance = WeekDay.from_json(json_str)
            return instance

        # deserialize data into AnyDef
        try:
            instance.actual_instance = AnyDef.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Day
        try:
            instance.actual_instance = Day.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DayMonth
        try:
            instance.actual_instance = DayMonth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DayMonthYear
        try:
            instance.actual_instance = DayMonthYear.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RangeDay
        try:
            instance.actual_instance = RangeDay.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RangeDayMonth
        try:
            instance.actual_instance = RangeDayMonth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RangeDayMonthYear
        try:
            instance.actual_instance = RangeDayMonthYear.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RangeWeekDay
        try:
            instance.actual_instance = RangeWeekDay.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WeekDay
        try:
            instance.actual_instance = WeekDay.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AnyDefAllOfTimeDefs with oneOf schemas: AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AnyDefAllOfTimeDefs with oneOf schemas: AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AnyDef, Day, DayMonth, DayMonthYear, RangeDay, RangeDayMonth, RangeDayMonthYear, RangeWeekDay, WeekDay]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

from touroptimizer_py_client.models.any_def import AnyDef
# TODO: Rewrite to not use raise_errors
AnyDefAllOfTimeDefs.model_rebuild(raise_errors=False)

