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

from touroptimizer_py_client.models.node import Node

class TestNode(unittest.TestCase):
    """Node unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Node:
        """Test Node
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Node`
        """
        model = Node()
        if include_optional:
            return Node(
                id = 'MySecondNode',
                extra_info = 'My custom extra info',
                location_id = 'MyFirstNode',
                constraint_alias_id = 'MyNodeXXX',
                type = touroptimizer_py_client.models.node_type.NodeType(
                    type_name = '', ),
                opening_hours = [
                    touroptimizer_py_client.models.opening_hours.OpeningHours(
                        begin = '2020-03-06T06:00Z', 
                        end = '2020-03-06T19:00Z', 
                        zone_id = 'UTC', 
                        service_hours_offsets = [
                            touroptimizer_py_client.models.long_long_pair.LongLongPair(
                                left = 56, 
                                right = 56, )
                            ], 
                        is_preffered = False, 
                        is_solo_access_hours = True, )
                    ],
                visit_duration = 'PT60M',
                constraints = [
                    touroptimizer_py_client.models.constraint.Constraint(
                        initial_class_name = '', 
                        type = touroptimizer_py_client.models.constraint_type.ConstraintType(
                            type_name = '', ), 
                        is_hard = True, )
                    ],
                offered_node = touroptimizer_py_client.models.offered_node.OfferedNode(
                    individual_multiplier = 1.337, ),
                load_dimension = touroptimizer_py_client.models.load_dimension.LoadDimension(
                    unload_all_dimension = 56, 
                    total_load_dimension = 56, 
                    unload_all = True, ),
                load = [
                    1.337
                    ],
                qualifications = [
                    touroptimizer_py_client.models.qualification.Qualification(
                        type = touroptimizer_py_client.models.qualification_type.QualificationType(
                            type_name = '', ), )
                    ],
                lockdown_time = 56,
                fix_cost = 1.337,
                priority = 56,
                priority_first = 56,
                priority_last = 56,
                node_color = touroptimizer_py_client.models.node_color.NodeColor(
                    color_code = 56, 
                    color_id = '', 
                    count_value = 56, ),
                min_auto_filter_protected_executions = 56,
                node_depot = touroptimizer_py_client.models.i_node_depot.INodeDepot(
                    items = [
                        touroptimizer_py_client.models.i_load.ILoad(
                            priority = 56, 
                            load_value = 1.337, 
                            request = True, 
                            fuzzy_visit = True, 
                            id = '', 
                            type_name = '', )
                        ], 
                    depot_id = '', 
                    type_name = '', ),
                route_dependent_visit_duration = True,
                allow_move_to_reduce_flex_time = True,
                min_visit_duration = 'PT10M',
                joint_visit_duration = 'PT60M',
                return_start_duration = '',
                is_optimizable = True,
                is_optional = True,
                is_unassigned = True,
                is_ignore_on_zero_duration = True,
                is_causing_idle_time_cost = True,
                is_wait_on_early_arrival_first_node = True,
                is_wait_on_early_arrival = True,
                is_unlocated_hub_connection_time = True,
                is_opening_hours_includes_duration = True,
                is_work_node = True,
                is_stay_node = True,
                is_ignore_on_zero_load = True
            )
        else:
            return Node(
                id = 'MySecondNode',
                type = touroptimizer_py_client.models.node_type.NodeType(
                    type_name = '', ),
                opening_hours = [
                    touroptimizer_py_client.models.opening_hours.OpeningHours(
                        begin = '2020-03-06T06:00Z', 
                        end = '2020-03-06T19:00Z', 
                        zone_id = 'UTC', 
                        service_hours_offsets = [
                            touroptimizer_py_client.models.long_long_pair.LongLongPair(
                                left = 56, 
                                right = 56, )
                            ], 
                        is_preffered = False, 
                        is_solo_access_hours = True, )
                    ],
                visit_duration = 'PT60M',
        )
        """

    def testNode(self):
        """Test Node"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
