# coding: utf-8

# flake8: noqa
"""
    DNA Evolutions - JOpt.TourOptimizer

    # JOpt.TourOptimizer REST API  ![DNA Evolutions Logo](https://www.dna-evolutions.com/images/dna_logo.png)  JOpt.TourOptimizer is DNA Evolutions' route optimization and scheduling engine for transportation, field service, and resource planning scenarios.  This API is a **reactive Spring WebFlux REST service** with an **OpenAPI 3** contract, designed for integration into third-party systems and for generating typed client SDKs directly from the schema.  ---  ## Endpoint groups  ### Job endpoints (`job`)  The primary integration model for all deployments with a connected database.  Submit an optimization job with `POST /api/v1/jobs` and receive an HTTP 202 response containing a unique `jobId`. Use that jobId to poll for status, progress, warnings, errors, and the final result at any time — no open connection required.  | Endpoint | Description | Availability | |---|---|---| | `POST /api/v1/jobs` | Submit an async optimization job | All deployments | | `GET /api/v1/jobs/{jobId}/status` | Poll job status | All deployments | | `GET /api/v1/jobs/{jobId}/result` | Retrieve full optimization result | All deployments | | `GET /api/v1/jobs/{jobId}/solution` | Retrieve solution payload only | All deployments | | `GET /api/v1/jobs/{jobId}/progress` | Retrieve progress snapshots | All deployments | | `GET /api/v1/jobs/{jobId}/warnings` | Retrieve warning messages | All deployments | | `GET /api/v1/jobs/{jobId}/errors` | Retrieve error messages | All deployments | | `GET /api/v1/jobs/{jobId}/export` | Download result as ZIP archive | All deployments | | `POST /api/v1/jobs/{jobId}/stop` | Send graceful stop signal to a running job | All deployments | | `DELETE /api/v1/jobs/{jobId}` | Delete all persisted data for a job | All deployments | | `POST /api/v1/jobs/search` | Search jobs by metadata criteria | On-premise (free-search enabled) | | `POST /api/v1/jobs/import` | Import a pre-computed result directly | On-premise (import enabled) |  All job endpoints require the `X-Tenant-Id` header, injected by the API gateway. The `jobId` returned at submission is the only token needed for all subsequent reads.  ### Synchronous run endpoints (`optimization`)  Available on on-premise installations with synchronous mode enabled. The client holds the HTTP connection open and receives the result directly in the response body.  | Endpoint | Description | |---|---| | `POST /api/v1/runs` | Start a run, return runId immediately (HTTP 202) | | `GET /api/v1/runs/{runId}/result` | Block until run completes, return full result | | `GET /api/v1/runs/{runId}/solution` | Block until run completes, return solution only | | `DELETE /api/v1/runs/{runId}` | Stop the run gracefully | | `GET /api/v1/runs/{runId}/started` | One-shot signal when the run has started |  ### Event stream endpoints (`stream`)  Server-Sent Event streams for monitoring a running synchronous optimization in near real time. Subscribe to one or more streams while a `POST /api/v1/runs` call is in progress.  | Endpoint | Event type | |---|---| | `GET /api/v1/runs/{runId}/stream/progress` | Progress percentage and timing | | `GET /api/v1/runs/{runId}/stream/status` | Lifecycle status transitions | | `GET /api/v1/runs/{runId}/stream/warnings` | Non-fatal solver warnings | | `GET /api/v1/runs/{runId}/stream/errors` | Solver error events |  ### Health endpoint (`health`)  | Endpoint | Description | |---|---| | `GET /api/v1/health` | Service liveness and readiness |  ---  ## Deployment modes and feature flags  Endpoints that require specific conditions are activated via Spring `@Conditional` annotations and application properties. Endpoints not active in a given deployment are absent from the service entirely and do not appear in the runtime spec.  | Condition | Property / annotation | Effect | |---|---|---| | Database connected | `DatabaseEnabledCondition` | Activates all `job` endpoints | | Sync mode | `SynchControllersEnabledCondition` | Activates `optimization` and `stream` endpoints | | Free search | `DatabaseFreeSearchEnabledCondition` | Activates `POST /api/v1/jobs/search` | | Import | `DatabaseJobImportEnabledCondition` | Activates `POST /api/v1/jobs/import` |  ---  ## Tenant isolation  Every job endpoint is scoped by `X-Tenant-Id`, injected by the API gateway. Persisted documents are tagged with both `jobId` and `tenantId`. A request with a valid `jobId` but a mismatched `tenantId` returns no data. The `jobId` is a UUID v4 (122 bits of randomness) and is not a security credential — security is enforced by the verified `tenantId` from the gateway header.  ---  ## Encryption at rest  Results can be stored encrypted in two modes:  - **CLIENT mode**: key derived from a caller-provided passphrase via PBKDF2.   Pass the same secret in `X-Encryption-Secret` when reading back. - **KMS mode**: server-generated data encryption key (DEK) wrapped by an   external key management service (Azure Key Vault, AWS KMS). Decryption is   transparent to the caller.  The `encrypted` and `sec` fields in `DatabaseInfoSearchResult` indicate which mode was used for each stored result.  ---  ## Client generation  The OpenAPI schema can be used to generate typed clients for any language. The `operationId` values follow `{verb}{Resource}` lowerCamelCase convention (`createJob`, `getJobResult`, `listJobs`, etc.) for predictable generated method names.  ---  This service is based on **JOpt Core (unknown)**. 

    The version of the OpenAPI document: 1.3.5-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

# import models into model package
from touroptimizer_py_client.models.absolute_node_color_capacity import AbsoluteNodeColorCapacity
from touroptimizer_py_client.models.absolute_node_color_multi_route_constraint import AbsoluteNodeColorMultiRouteConstraint
from touroptimizer_py_client.models.any_def import AnyDef
from touroptimizer_py_client.models.any_def_all_of_time_defs import AnyDefAllOfTimeDefs
from touroptimizer_py_client.models.binding_resource_constraint import BindingResourceConstraint
from touroptimizer_py_client.models.bit_type_constraint import BitTypeConstraint
from touroptimizer_py_client.models.bit_type_qualification import BitTypeQualification
from touroptimizer_py_client.models.bit_type_with_expertise_constraint import BitTypeWithExpertiseConstraint
from touroptimizer_py_client.models.bit_type_with_expertise_qualification import BitTypeWithExpertiseQualification
from touroptimizer_py_client.models.capacity_resource import CapacityResource
from touroptimizer_py_client.models.connected_constraint import ConnectedConstraint
from touroptimizer_py_client.models.connection_by_time import ConnectionByTime
from touroptimizer_py_client.models.connection_related_late_margin import ConnectionRelatedLateMargin
from touroptimizer_py_client.models.constraint import Constraint
from touroptimizer_py_client.models.constraint_type import ConstraintType
from touroptimizer_py_client.models.construction_hook import ConstructionHook
from touroptimizer_py_client.models.construction_optimization_algorithm_config import ConstructionOptimizationAlgorithmConfig
from touroptimizer_py_client.models.core_build_options import CoreBuildOptions
from touroptimizer_py_client.models.creator_setting import CreatorSetting
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult
from touroptimizer_py_client.models.date_def import DateDef
from touroptimizer_py_client.models.day import Day
from touroptimizer_py_client.models.day_month import DayMonth
from touroptimizer_py_client.models.day_month_year import DayMonthYear
from touroptimizer_py_client.models.degrading_load_capacity import DegradingLoadCapacity
from touroptimizer_py_client.models.different_visitor_node_relation import DifferentVisitorNodeRelation
from touroptimizer_py_client.models.edge_element_connection import EdgeElementConnection
from touroptimizer_py_client.models.element_connection import ElementConnection
from touroptimizer_py_client.models.element_connection_type import ElementConnectionType
from touroptimizer_py_client.models.encoded_polyline import EncodedPolyline
from touroptimizer_py_client.models.event_node import EventNode
from touroptimizer_py_client.models.event_pillar_node import EventPillarNode
from touroptimizer_py_client.models.excluding_resource_constraint import ExcludingResourceConstraint
from touroptimizer_py_client.models.geo_address import GeoAddress
from touroptimizer_py_client.models.geo_node import GeoNode
from touroptimizer_py_client.models.geo_pillar_node import GeoPillarNode
from touroptimizer_py_client.models.heuristic_optimization_algorithm_config import HeuristicOptimizationAlgorithmConfig
from touroptimizer_py_client.models.hook_type import HookType
from touroptimizer_py_client.models.i_load import ILoad
from touroptimizer_py_client.models.i_load_capacity import ILoadCapacity
from touroptimizer_py_client.models.i_node_depot import INodeDepot
from touroptimizer_py_client.models.i_resource_depot import IResourceDepot
from touroptimizer_py_client.models.idle_event_node import IdleEventNode
from touroptimizer_py_client.models.integer_multi_constraint_helper_item import IntegerMultiConstraintHelperItem
from touroptimizer_py_client.models.j_opt_optimization_error import JOptOptimizationError
from touroptimizer_py_client.models.j_opt_optimization_progress import JOptOptimizationProgress
from touroptimizer_py_client.models.j_opt_optimization_status import JOptOptimizationStatus
from touroptimizer_py_client.models.j_opt_optimization_warning import JOptOptimizationWarning
from touroptimizer_py_client.models.json_config import JSONConfig
from touroptimizer_py_client.models.job_accepted_response import JobAcceptedResponse
from touroptimizer_py_client.models.load_dimension import LoadDimension
from touroptimizer_py_client.models.location_parameters import LocationParameters
from touroptimizer_py_client.models.long_long_pair import LongLongPair
from touroptimizer_py_client.models.magneto_node_constraint import MagnetoNodeConstraint
from touroptimizer_py_client.models.max_distance_construction_hook import MaxDistanceConstructionHook
from touroptimizer_py_client.models.mixed_flex_load import MixedFlexLoad
from touroptimizer_py_client.models.mongo_optimization_persistence_setting import MongoOptimizationPersistenceSetting
from touroptimizer_py_client.models.multi_time_window_node_relation import MultiTimeWindowNodeRelation
from touroptimizer_py_client.models.node import Node
from touroptimizer_py_client.models.node_color import NodeColor
from touroptimizer_py_client.models.node_color_capacity import NodeColorCapacity
from touroptimizer_py_client.models.node_color_multi_route_constraint import NodeColorMultiRouteConstraint
from touroptimizer_py_client.models.node_relation import NodeRelation
from touroptimizer_py_client.models.node_relation_type import NodeRelationType
from touroptimizer_py_client.models.node_type import NodeType
from touroptimizer_py_client.models.offered_node import OfferedNode
from touroptimizer_py_client.models.opening_hours import OpeningHours
from touroptimizer_py_client.models.optimization_key_setting import OptimizationKeySetting
from touroptimizer_py_client.models.optimization_options import OptimizationOptions
from touroptimizer_py_client.models.optimization_persistence_setting import OptimizationPersistenceSetting
from touroptimizer_py_client.models.optimization_persistence_strategy_setting import OptimizationPersistenceStrategySetting
from touroptimizer_py_client.models.optimization_scheme_options import OptimizationSchemeOptions
from touroptimizer_py_client.models.optimization_status import OptimizationStatus
from touroptimizer_py_client.models.pillar_type import PillarType
from touroptimizer_py_client.models.plugin_setting import PluginSetting
from touroptimizer_py_client.models.plugin_settings import PluginSettings
from touroptimizer_py_client.models.position import Position
from touroptimizer_py_client.models.qualification import Qualification
from touroptimizer_py_client.models.qualification_type import QualificationType
from touroptimizer_py_client.models.range_day import RangeDay
from touroptimizer_py_client.models.range_day_month import RangeDayMonth
from touroptimizer_py_client.models.range_day_month_year import RangeDayMonthYear
from touroptimizer_py_client.models.range_week_day import RangeWeekDay
from touroptimizer_py_client.models.reduced_node_edge_connector_item import ReducedNodeEdgeConnectorItem
from touroptimizer_py_client.models.request_flex_load import RequestFlexLoad
from touroptimizer_py_client.models.resource import Resource
from touroptimizer_py_client.models.resource_location_constraint import ResourceLocationConstraint
from touroptimizer_py_client.models.resource_trip import ResourceTrip
from touroptimizer_py_client.models.resource_type import ResourceType
from touroptimizer_py_client.models.resource_with_priority import ResourceWithPriority
from touroptimizer_py_client.models.rest_optimization import RestOptimization
from touroptimizer_py_client.models.route import Route
from touroptimizer_py_client.models.route_element_detail import RouteElementDetail
from touroptimizer_py_client.models.route_header import RouteHeader
from touroptimizer_py_client.models.route_trip import RouteTrip
from touroptimizer_py_client.models.run_accepted_response import RunAcceptedResponse
from touroptimizer_py_client.models.same_visitor_node_relation import SameVisitorNodeRelation
from touroptimizer_py_client.models.security_helper_item_metadata import SecurityHelperItemMetadata
from touroptimizer_py_client.models.simple_load import SimpleLoad
from touroptimizer_py_client.models.simple_load_capacity import SimpleLoadCapacity
from touroptimizer_py_client.models.simple_node_depot import SimpleNodeDepot
from touroptimizer_py_client.models.simple_resource_depot import SimpleResourceDepot
from touroptimizer_py_client.models.solution import Solution
from touroptimizer_py_client.models.solution_header import SolutionHeader
from touroptimizer_py_client.models.start_reduction_time_definition import StartReductionTimeDefinition
from touroptimizer_py_client.models.start_reduction_time_include_definition import StartReductionTimeIncludeDefinition
from touroptimizer_py_client.models.start_reduction_time_pillar_definition import StartReductionTimePillarDefinition
from touroptimizer_py_client.models.status import Status
from touroptimizer_py_client.models.stay_out_cycle_definition import StayOutCycleDefinition
from touroptimizer_py_client.models.stay_out_definition import StayOutDefinition
from touroptimizer_py_client.models.stream_persistence_strategy_setting import StreamPersistenceStrategySetting
from touroptimizer_py_client.models.string_integer_pair import StringIntegerPair
from touroptimizer_py_client.models.supply_flex_load import SupplyFlexLoad
from touroptimizer_py_client.models.text_solution import TextSolution
from touroptimizer_py_client.models.time_comparison_juncture import TimeComparisonJuncture
from touroptimizer_py_client.models.time_window_node_relation import TimeWindowNodeRelation
from touroptimizer_py_client.models.type_constraint import TypeConstraint
from touroptimizer_py_client.models.type_dictionaries import TypeDictionaries
from touroptimizer_py_client.models.type_dictionary import TypeDictionary
from touroptimizer_py_client.models.type_level_offering import TypeLevelOffering
from touroptimizer_py_client.models.type_level_requirement import TypeLevelRequirement
from touroptimizer_py_client.models.type_qualification import TypeQualification
from touroptimizer_py_client.models.type_with_expertise import TypeWithExpertise
from touroptimizer_py_client.models.type_with_expertise_constraint import TypeWithExpertiseConstraint
from touroptimizer_py_client.models.type_with_expertise_qualification import TypeWithExpertiseQualification
from touroptimizer_py_client.models.uk_post_code import UKPostCode
from touroptimizer_py_client.models.uk_post_code_constraint import UKPostCodeConstraint
from touroptimizer_py_client.models.uk_post_code_qualification import UKPostCodeQualification
from touroptimizer_py_client.models.unload_all_load import UnloadAllLoad
from touroptimizer_py_client.models.violation import Violation
from touroptimizer_py_client.models.week_day import WeekDay
from touroptimizer_py_client.models.working_hours import WorkingHours
from touroptimizer_py_client.models.zone_code_type import ZoneCodeType
from touroptimizer_py_client.models.zone_connection import ZoneConnection
from touroptimizer_py_client.models.zone_number import ZoneNumber
from touroptimizer_py_client.models.zone_number_constraint import ZoneNumberConstraint
from touroptimizer_py_client.models.zone_number_qualification import ZoneNumberQualification

