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

from touroptimizer_py_client.models.route import Route

class TestRoute(unittest.TestCase):
    """Route unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Route:
        """Test Route
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Route`
        """
        model = Route()
        if include_optional:
            return Route(
                header = touroptimizer_py_client.models.route_header.RouteHeader(
                    cost = 2468.32, 
                    time = 'PT30M', 
                    idle_time = 'PT30M', 
                    prod_time = 'PT30M', 
                    tran_time = 'PT310M', 
                    termi_time = 'PT800M', 
                    distance = '800.0 km', 
                    termi_distance = '53.0 km', 
                    route_violations = [
                        touroptimizer_py_client.models.violation.Violation(
                            value = '', 
                            desc = 'Late time [min]: 507.98525', 
                            offender = 'Node_0', 
                            category = 'CONSTRAINTVIOLATION', 
                            attribute = 'TIMECONSTRAINT', 
                            sub_attribute = 'LATE', 
                            code = 5, )
                        ], 
                    is_closed = True, 
                    is_alternate_destination = True, ),
                id = 11,
                resource_id = 'Laura',
                route_trip = touroptimizer_py_client.models.route_trip.RouteTrip(
                    trips = [
                        touroptimizer_py_client.models.resource_trip.ResourceTrip(
                            line = touroptimizer_py_client.models.encoded_polyline.EncodedPolyline(
                                encoded_polyline = '', 
                                precision = 1.337, ), 
                            from_element_id = '', 
                            to_element_id = '', 
                            raw_json = touroptimizer_py_client.models.raw_json.rawJson(), )
                        ], ),
                start_time = '2020-03-06T07:00Z',
                start_element_id = 'Laura',
                start_position = touroptimizer_py_client.models.position.Position(
                    latitude = 48.384037, 
                    longitude = 10.005226, 
                    location_id = 'MyLocationId', 
                    geo_address = touroptimizer_py_client.models.geo_address.GeoAddress(
                        location_id = 'MyLocationId', 
                        housenumber = '5', 
                        streetname = 'Marlene-Dietrich-Strasse', 
                        city = 'Neu-Ulm', 
                        county = '', 
                        state = '', 
                        statecode = '', 
                        country = 'Germany', 
                        macrocountry = 'Berlin', 
                        countrycode = 'DE', 
                        postalcode = '89231', 
                        layer = '', 
                        source = '', 
                        accuracy = '', 
                        confidence = 1.0, 
                        label = '', ), 
                    location_parameters = touroptimizer_py_client.models.location_parameters.LocationParameters(
                        layers = 'address', 
                        size = 1, 
                        radius = 20, 
                        sources = 'all', ), ),
                end_element_id = 'Laura',
                end_position = touroptimizer_py_client.models.position.Position(
                    latitude = 48.384037, 
                    longitude = 10.005226, 
                    location_id = 'MyLocationId', 
                    geo_address = touroptimizer_py_client.models.geo_address.GeoAddress(
                        location_id = 'MyLocationId', 
                        housenumber = '5', 
                        streetname = 'Marlene-Dietrich-Strasse', 
                        city = 'Neu-Ulm', 
                        county = '', 
                        state = '', 
                        statecode = '', 
                        country = 'Germany', 
                        macrocountry = 'Berlin', 
                        countrycode = 'DE', 
                        postalcode = '89231', 
                        layer = '', 
                        source = '', 
                        accuracy = '', 
                        confidence = 1.0, 
                        label = '', ), 
                    location_parameters = touroptimizer_py_client.models.location_parameters.LocationParameters(
                        layers = 'address', 
                        size = 1, 
                        radius = 20, 
                        sources = 'all', ), ),
                optimizable_element_ids = [
                    ''
                    ],
                non_optimizable_element_ids = [
                    ''
                    ],
                optional_optimizable_element_ids = [
                    ''
                    ],
                pillar_element_ids = [
                    ''
                    ],
                element_details = [
                    touroptimizer_py_client.models.route_element_detail.RouteElementDetail(
                        element_id = 'Customer-A', 
                        start_time = '2020-03-06T08:00Z', 
                        arrival_time = '2020-03-06T07:00Z', 
                        departure_time = '2020-03-06T10:00Z', 
                        transition_time = 'PT23M', 
                        effective_position = touroptimizer_py_client.models.position.Position(
                            latitude = 48.384037, 
                            longitude = 10.005226, 
                            location_id = 'MyLocationId', 
                            geo_address = touroptimizer_py_client.models.geo_address.GeoAddress(
                                location_id = 'MyLocationId', 
                                housenumber = '5', 
                                streetname = 'Marlene-Dietrich-Strasse', 
                                city = 'Neu-Ulm', 
                                county = '', 
                                state = '', 
                                statecode = '', 
                                country = 'Germany', 
                                macrocountry = 'Berlin', 
                                countrycode = 'DE', 
                                postalcode = '89231', 
                                layer = '', 
                                source = '', 
                                accuracy = '', 
                                confidence = 1.0, 
                                label = '', ), 
                            location_parameters = touroptimizer_py_client.models.location_parameters.LocationParameters(
                                layers = 'address', 
                                size = 1, 
                                radius = 20, 
                                sources = 'all', ), ), 
                        idle_time = 'PT60M', 
                        zone_id = 'UTC', 
                        white_space_idle_time = 'PT26M', 
                        duration_time = 'PT120M', 
                        transition_distance = '100.0 km', 
                        choosen_working_hours_index = 1, 
                        chosen_opening_hours_index = 1, 
                        early_deviation = 'PT30M', 
                        late_deviation = 'PT-30M', 
                        schedule_status = 'INTIME', 
                        visitor_id = 'Laura', 
                        load_change = [
                            1.337
                            ], 
                        cur_capacity = [
                            1.337
                            ], 
                        before_visit_node_depot = touroptimizer_py_client.models.i_node_depot.INodeDepot(
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
                        after_visit_node_depot = touroptimizer_py_client.models.i_node_depot.INodeDepot(
                            depot_id = '', 
                            type_name = '', ), 
                        node_violations = [
                            touroptimizer_py_client.models.violation.Violation(
                                value = '', 
                                desc = 'Late time [min]: 507.98525', 
                                offender = 'Node_0', 
                                category = 'CONSTRAINTVIOLATION', 
                                attribute = 'TIMECONSTRAINT', 
                                sub_attribute = 'LATE', 
                                code = 5, )
                            ], 
                        is_unlocated_idle_time = True, )
                    ],
                pillar_latest_effective_arrival_offset_map = {
                    'key' : 56
                    },
                flags = [
                    'FINALIZED_PILLARFORCEARRANGER'
                    ],
                additional_route_start_offset = 56,
                is_locked_down = False,
                is_inactive = False,
                is_finalized = False
            )
        else:
            return Route(
                id = 11,
                resource_id = 'Laura',
                start_time = '2020-03-06T07:00Z',
                start_element_id = 'Laura',
                end_element_id = 'Laura',
                optimizable_element_ids = [
                    ''
                    ],
                non_optimizable_element_ids = [
                    ''
                    ],
                optional_optimizable_element_ids = [
                    ''
                    ],
                pillar_element_ids = [
                    ''
                    ],
                element_details = [
                    touroptimizer_py_client.models.route_element_detail.RouteElementDetail(
                        element_id = 'Customer-A', 
                        start_time = '2020-03-06T08:00Z', 
                        arrival_time = '2020-03-06T07:00Z', 
                        departure_time = '2020-03-06T10:00Z', 
                        transition_time = 'PT23M', 
                        effective_position = touroptimizer_py_client.models.position.Position(
                            latitude = 48.384037, 
                            longitude = 10.005226, 
                            location_id = 'MyLocationId', 
                            geo_address = touroptimizer_py_client.models.geo_address.GeoAddress(
                                location_id = 'MyLocationId', 
                                housenumber = '5', 
                                streetname = 'Marlene-Dietrich-Strasse', 
                                city = 'Neu-Ulm', 
                                county = '', 
                                state = '', 
                                statecode = '', 
                                country = 'Germany', 
                                macrocountry = 'Berlin', 
                                countrycode = 'DE', 
                                postalcode = '89231', 
                                layer = '', 
                                source = '', 
                                accuracy = '', 
                                confidence = 1.0, 
                                label = '', ), 
                            location_parameters = touroptimizer_py_client.models.location_parameters.LocationParameters(
                                layers = 'address', 
                                size = 1, 
                                radius = 20, 
                                sources = 'all', ), ), 
                        idle_time = 'PT60M', 
                        zone_id = 'UTC', 
                        white_space_idle_time = 'PT26M', 
                        duration_time = 'PT120M', 
                        transition_distance = '100.0 km', 
                        choosen_working_hours_index = 1, 
                        chosen_opening_hours_index = 1, 
                        early_deviation = 'PT30M', 
                        late_deviation = 'PT-30M', 
                        schedule_status = 'INTIME', 
                        visitor_id = 'Laura', 
                        load_change = [
                            1.337
                            ], 
                        cur_capacity = [
                            1.337
                            ], 
                        before_visit_node_depot = touroptimizer_py_client.models.i_node_depot.INodeDepot(
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
                        after_visit_node_depot = touroptimizer_py_client.models.i_node_depot.INodeDepot(
                            depot_id = '', 
                            type_name = '', ), 
                        node_violations = [
                            touroptimizer_py_client.models.violation.Violation(
                                value = '', 
                                desc = 'Late time [min]: 507.98525', 
                                offender = 'Node_0', 
                                category = 'CONSTRAINTVIOLATION', 
                                attribute = 'TIMECONSTRAINT', 
                                sub_attribute = 'LATE', 
                                code = 5, )
                            ], 
                        is_unlocated_idle_time = True, )
                    ],
        )
        """

    def testRoute(self):
        """Test Route"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
