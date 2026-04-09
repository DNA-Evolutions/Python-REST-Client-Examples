# coding: utf-8

"""
    DNA Evolutions - JOpt.TourOptimizer

    # JOpt.TourOptimizer REST API  ![DNA Evolutions Logo](https://www.dna-evolutions.com/images/dna_logo.png)  JOpt.TourOptimizer is DNA Evolutions' route optimization and scheduling engine for transportation, field service, and resource planning scenarios.  This API is a **reactive Spring WebFlux REST service** with an **OpenAPI 3** contract, designed for integration into third-party systems and for generating typed client SDKs directly from the schema.  ---  ## Endpoint groups  ### Job endpoints (`job`)  The primary integration model for all deployments with a connected database.  Submit an optimization job with `POST /api/v1/jobs` and receive an HTTP 202 response containing a unique `jobId`. Use that jobId to poll for status, progress, warnings, errors, and the final result at any time — no open connection required.  | Endpoint | Description | Availability | |---|---|---| | `POST /api/v1/jobs` | Submit an async optimization job | All deployments | | `GET /api/v1/jobs/{jobId}/status` | Poll job status | All deployments | | `GET /api/v1/jobs/{jobId}/result` | Retrieve full optimization result | All deployments | | `GET /api/v1/jobs/{jobId}/solution` | Retrieve solution payload only | All deployments | | `GET /api/v1/jobs/{jobId}/progress` | Retrieve progress snapshots | All deployments | | `GET /api/v1/jobs/{jobId}/warnings` | Retrieve warning messages | All deployments | | `GET /api/v1/jobs/{jobId}/errors` | Retrieve error messages | All deployments | | `GET /api/v1/jobs/{jobId}/export` | Download result as ZIP archive | All deployments | | `POST /api/v1/jobs/{jobId}/stop` | Send graceful stop signal to a running job | All deployments | | `DELETE /api/v1/jobs/{jobId}` | Delete all persisted data for a job | All deployments | | `POST /api/v1/jobs/search` | Search jobs by metadata criteria | On-premise (free-search enabled) | | `POST /api/v1/jobs/import` | Import a pre-computed result directly | On-premise (import enabled) |  All job endpoints require the `X-Tenant-Id` header, injected by the API gateway. The `jobId` returned at submission is the only token needed for all subsequent reads.  ### Synchronous run endpoints (`optimization`)  Available on on-premise installations with synchronous mode enabled. The client holds the HTTP connection open and receives the result directly in the response body.  | Endpoint | Description | |---|---| | `POST /api/v1/runs` | Start a run, return runId immediately (HTTP 202) | | `GET /api/v1/runs/{runId}/result` | Block until run completes, return full result | | `GET /api/v1/runs/{runId}/solution` | Block until run completes, return solution only | | `DELETE /api/v1/runs/{runId}` | Stop the run gracefully | | `GET /api/v1/runs/{runId}/started` | One-shot signal when the run has started |  ### Event stream endpoints (`stream`)  Server-Sent Event streams for monitoring a running synchronous optimization in near real time. Subscribe to one or more streams while a `POST /api/v1/runs` call is in progress.  | Endpoint | Event type | |---|---| | `GET /api/v1/runs/{runId}/stream/progress` | Progress percentage and timing | | `GET /api/v1/runs/{runId}/stream/status` | Lifecycle status transitions | | `GET /api/v1/runs/{runId}/stream/warnings` | Non-fatal solver warnings | | `GET /api/v1/runs/{runId}/stream/errors` | Solver error events |  ### Health endpoint (`health`)  | Endpoint | Description | |---|---| | `GET /api/v1/health` | Service liveness and readiness |  ---  ## Deployment modes and feature flags  Endpoints that require specific conditions are activated via Spring `@Conditional` annotations and application properties. Endpoints not active in a given deployment are absent from the service entirely and do not appear in the runtime spec.  | Condition | Property / annotation | Effect | |---|---|---| | Database connected | `DatabaseEnabledCondition` | Activates all `job` endpoints | | Sync mode | `SynchControllersEnabledCondition` | Activates `optimization` and `stream` endpoints | | Free search | `DatabaseFreeSearchEnabledCondition` | Activates `POST /api/v1/jobs/search` | | Import | `DatabaseJobImportEnabledCondition` | Activates `POST /api/v1/jobs/import` |  ---  ## Tenant isolation  Every job endpoint is scoped by `X-Tenant-Id`, injected by the API gateway. Persisted documents are tagged with both `jobId` and `tenantId`. A request with a valid `jobId` but a mismatched `tenantId` returns no data. The `jobId` is a UUID v4 (122 bits of randomness) and is not a security credential — security is enforced by the verified `tenantId` from the gateway header.  ---  ## Encryption at rest  Results can be stored encrypted in two modes:  - **CLIENT mode**: key derived from a caller-provided passphrase via PBKDF2.   Pass the same secret in `X-Encryption-Secret` when reading back. - **KMS mode**: server-generated data encryption key (DEK) wrapped by an   external key management service (Azure Key Vault, AWS KMS). Decryption is   transparent to the caller.  The `encrypted` and `sec` fields in `DatabaseInfoSearchResult` indicate which mode was used for each stored result.  ---  ## Client generation  The OpenAPI schema can be used to generate typed clients for any language. The `operationId` values follow `{verb}{Resource}` lowerCamelCase convention (`createJob`, `getJobResult`, `listJobs`, etc.) for predictable generated method names.  ---  This service is based on **JOpt Core (unknown)**. 

    The version of the OpenAPI document: 1.3.5-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from touroptimizer_py_client.models.working_hours import WorkingHours

class TestWorkingHours(unittest.TestCase):
    """WorkingHours unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkingHours:
        """Test WorkingHours
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkingHours`
        """
        model = WorkingHours()
        if include_optional:
            return WorkingHours(
                begin = '2020-03-06T07:00Z',
                end = '2020-03-06T17:00Z',
                zone_id = 'UTC',
                max_time = 'PT480M',
                max_distance = '800.0 km',
                stay_out_cycle_definition = touroptimizer_py_client.models.stay_out_cycle_definition.StayOutCycleDefinition(
                    cycle_length = 'PT7D', 
                    cycle_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                start_reduction_time_definition = touroptimizer_py_client.models.start_reduction_time_definition.StartReductionTimeDefinition(
                    max_route_start_reduction_time = 'PT30M', 
                    is_reduction_time_only_used_for_driving = True, ),
                start_reduction_time_pillar_definition = touroptimizer_py_client.models.start_reduction_time_pillar_definition.StartReductionTimePillarDefinition(
                    max_route_start_reduction_time_pillar = 'PT30M', 
                    is_reduction_time_only_used_for_driving_pillar = True, ),
                start_reduction_time_include_definition = touroptimizer_py_client.models.start_reduction_time_include_definition.StartReductionTimeIncludeDefinition(
                    is_reduction_time_included_in_working_time = True, ),
                local_flex_time = 'PT30M',
                local_post_flex_time = 'PT30M',
                local_post_flex_time_only_on_overtime = True,
                max_local_pillar_after_hours_time = 'PT30M',
                node_color_capacities = [
                    touroptimizer_py_client.models.node_color_capacity.NodeColorCapacity(
                        node_color = touroptimizer_py_client.models.node_color.NodeColor(
                            color_code = 56, 
                            color_id = '', 
                            count_value = 56, ), 
                        max_usage = 1.337, )
                    ],
                working_hours_constraints = [
                    touroptimizer_py_client.models.constraint.Constraint(
                        initial_class_name = '', 
                        type = touroptimizer_py_client.models.constraint_type.ConstraintType(
                            type_name = '', ), 
                        is_hard = True, )
                    ],
                multi_working_hours_constraints = [
                    touroptimizer_py_client.models.constraint.Constraint(
                        initial_class_name = '', 
                        type = touroptimizer_py_client.models.constraint_type.ConstraintType(
                            type_name = '', ), 
                        is_hard = True, )
                    ],
                construction_hooks = [
                    touroptimizer_py_client.models.construction_hook.ConstructionHook(
                        type = touroptimizer_py_client.models.hook_type.HookType(
                            type_name = '', ), )
                    ],
                qualifications = [
                    touroptimizer_py_client.models.qualification.Qualification(
                        type = touroptimizer_py_client.models.qualification_type.QualificationType(
                            type_name = '', ), )
                    ],
                route_start_time_hook = 'PT30M',
                hook_element_connections = [
                    touroptimizer_py_client.models.reduced_node_edge_connector_item.ReducedNodeEdgeConnectorItem(
                        distance = '100.0 km', 
                        time = 'PT30M', 
                        from_element_id = 'MyStartElementId', 
                        to_element_id = 'MyToElementId', )
                    ],
                is_local_service_hub = True,
                is_closed_route = True,
                is_available_for_stay = True
            )
        else:
            return WorkingHours(
                begin = '2020-03-06T07:00Z',
                end = '2020-03-06T17:00Z',
                zone_id = 'UTC',
        )
        """

    def testWorkingHours(self):
        """Test WorkingHours"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
