"""
    DNA Evolutions - JOpt.TourOptimizer

    # JOpt.TourOptimizer REST API  ![DNA Evolutions Logo](https://www.dna-evolutions.com/images/dna_logo.png)  JOpt.TourOptimizer is DNA Evolutions' route optimization and scheduling engine for transportation, field service, and resource planning scenarios.  This API is a **reactive Spring WebFlux REST service** with an **OpenAPI 3** contract, designed for integration into third-party systems and for generating typed client SDKs directly from the schema.  ---  ## Endpoint groups  ### Job endpoints (`job`)  The primary integration model for all deployments with a connected database.  Submit an optimization job with `POST /api/v1/jobs` and receive an HTTP 202 response containing a unique `jobId`. Use that jobId to poll for status, progress, warnings, errors, and the final result at any time — no open connection required.  | Endpoint | Description | Availability | |---|---|---| | `POST /api/v1/jobs` | Submit an async optimization job | All deployments | | `GET /api/v1/jobs/{jobId}/status` | Poll job status | All deployments | | `GET /api/v1/jobs/{jobId}/result` | Retrieve full optimization result | All deployments | | `GET /api/v1/jobs/{jobId}/solution` | Retrieve solution payload only | All deployments | | `GET /api/v1/jobs/{jobId}/progress` | Retrieve progress snapshots | All deployments | | `GET /api/v1/jobs/{jobId}/warnings` | Retrieve warning messages | All deployments | | `GET /api/v1/jobs/{jobId}/errors` | Retrieve error messages | All deployments | | `GET /api/v1/jobs/{jobId}/export` | Download result as ZIP archive | All deployments | | `POST /api/v1/jobs/{jobId}/stop` | Send graceful stop signal to a running job | All deployments | | `DELETE /api/v1/jobs/{jobId}` | Delete all persisted data for a job | All deployments | | `POST /api/v1/jobs/search` | Search jobs by metadata criteria | On-premise (free-search enabled) | | `POST /api/v1/jobs/import` | Import a pre-computed result directly | On-premise (import enabled) |  All job endpoints require the `X-Tenant-Id` header, injected by the API gateway. The `jobId` returned at submission is the only token needed for all subsequent reads.  ### Synchronous run endpoints (`optimization`)  Available on on-premise installations with synchronous mode enabled. The client holds the HTTP connection open and receives the result directly in the response body.  | Endpoint | Description | |---|---| | `POST /api/v1/runs` | Start a run, return runId immediately (HTTP 202) | | `GET /api/v1/runs/{runId}/result` | Block until run completes, return full result | | `GET /api/v1/runs/{runId}/solution` | Block until run completes, return solution only | | `DELETE /api/v1/runs/{runId}` | Stop the run gracefully | | `GET /api/v1/runs/{runId}/started` | One-shot signal when the run has started |  ### Event stream endpoints (`stream`)  Server-Sent Event streams for monitoring a running synchronous optimization in near real time. Subscribe to one or more streams while a `POST /api/v1/runs` call is in progress.  | Endpoint | Event type | |---|---| | `GET /api/v1/runs/{runId}/stream/progress` | Progress percentage and timing | | `GET /api/v1/runs/{runId}/stream/status` | Lifecycle status transitions | | `GET /api/v1/runs/{runId}/stream/warnings` | Non-fatal solver warnings | | `GET /api/v1/runs/{runId}/stream/errors` | Solver error events |  ### Health endpoint (`health`)  | Endpoint | Description | |---|---| | `GET /api/v1/health` | Service liveness and readiness |  ---  ## Deployment modes and feature flags  Endpoints that require specific conditions are activated via Spring `@Conditional` annotations and application properties. Endpoints not active in a given deployment are absent from the service entirely and do not appear in the runtime spec.  | Condition | Property / annotation | Effect | |---|---|---| | Database connected | `DatabaseEnabledCondition` | Activates all `job` endpoints | | Sync mode | `SynchControllersEnabledCondition` | Activates `optimization` and `stream` endpoints | | Free search | `DatabaseFreeSearchEnabledCondition` | Activates `POST /api/v1/jobs/search` | | Import | `DatabaseJobImportEnabledCondition` | Activates `POST /api/v1/jobs/import` |  ---  ## Tenant isolation  Every job endpoint is scoped by `X-Tenant-Id`, injected by the API gateway. Persisted documents are tagged with both `jobId` and `tenantId`. A request with a valid `jobId` but a mismatched `tenantId` returns no data. The `jobId` is a UUID v4 (122 bits of randomness) and is not a security credential — security is enforced by the verified `tenantId` from the gateway header.  ---  ## Encryption at rest  Results can be stored encrypted in two modes:  - **CLIENT mode**: key derived from a caller-provided passphrase via PBKDF2.   Pass the same secret in `X-Encryption-Secret` when reading back. - **KMS mode**: server-generated data encryption key (DEK) wrapped by an   external key management service (Azure Key Vault, AWS KMS). Decryption is   transparent to the caller.  The `encrypted` and `sec` fields in `DatabaseInfoSearchResult` indicate which mode was used for each stored result.  ---  ## Client generation  The OpenAPI schema can be used to generate typed clients for any language. The `operationId` values follow `{verb}{Resource}` lowerCamelCase convention (`createJob`, `getJobResult`, `listJobs`, etc.) for predictable generated method names.  ---  This service is based on **JOpt Core (unknown)**. 

    The version of the OpenAPI document: 1.3.5-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import List, Optional, Tuple, Union
from typing_extensions import Annotated
from touroptimizer_py_client.models.database_info_search import DatabaseInfoSearch
from touroptimizer_py_client.models.database_info_search_result import DatabaseInfoSearchResult
from touroptimizer_py_client.models.j_opt_optimization_error import JOptOptimizationError
from touroptimizer_py_client.models.j_opt_optimization_progress import JOptOptimizationProgress
from touroptimizer_py_client.models.j_opt_optimization_status import JOptOptimizationStatus
from touroptimizer_py_client.models.j_opt_optimization_warning import JOptOptimizationWarning
from touroptimizer_py_client.models.job_accepted_response import JobAcceptedResponse
from touroptimizer_py_client.models.rest_optimization import RestOptimization
from touroptimizer_py_client.models.solution import Solution

from touroptimizer_py_client.api_client import ApiClient, RequestSerialized
from touroptimizer_py_client.api_response import ApiResponse
from touroptimizer_py_client.rest import RESTResponseType


class JobApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_job(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> JobAcceptedResponse:
        """Submit an optimization job.

        Accepts a RestOptimization payload and starts processing asynchronously. Returns HTTP 202 with a JobAcceptedResponse containing a unique jobId. Use the jobId with X-Tenant-Id to poll the job read endpoints for status, progress, warnings, errors, and the final result. Persistence is scoped to the tenant identified by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def create_job_with_http_info(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[JobAcceptedResponse]:
        """Submit an optimization job.

        Accepts a RestOptimization payload and starts processing asynchronously. Returns HTTP 202 with a JobAcceptedResponse containing a unique jobId. Use the jobId with X-Tenant-Id to poll the job read endpoints for status, progress, warnings, errors, and the final result. Persistence is scoped to the tenant identified by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def create_job_without_preload_content(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Submit an optimization job.

        Accepts a RestOptimization payload and starts processing asynchronously. Returns HTTP 202 with a JobAcceptedResponse containing a unique jobId. Use the jobId with X-Tenant-Id to poll the job read endpoints for status, progress, warnings, errors, and the final result. Persistence is scoped to the tenant identified by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes all persisted data to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_job_serialize(
        self,
        x_tenant_id,
        rest_optimization,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter
        if rest_optimization is not None:
            _body_params = rest_optimization


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/jobs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_job(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> bool:
        """Delete all persisted data for a job.

        Permanently removes the optimization result and all associated stream documents (progress, status, warnings, errors) for the given jobId from the database. Does not stop a running optimization — call POST /api/v1/jobs/{jobId}/stop first and wait for the job to terminate before deleting. Idempotent: returns 200 even if no data exists for this jobId.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_job_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bool]:
        """Delete all persisted data for a job.

        Permanently removes the optimization result and all associated stream documents (progress, status, warnings, errors) for the given jobId from the database. Does not stop a running optimization — call POST /api/v1/jobs/{jobId}/stop first and wait for the job to terminate before deleting. Idempotent: returns 200 even if no data exists for this jobId.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_job_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete all persisted data for a job.

        Permanently removes the optimization result and all associated stream documents (progress, status, warnings, errors) for the given jobId from the database. Does not stop a running optimization — call POST /api/v1/jobs/{jobId}/stop first and wait for the job to terminate before deleting. Idempotent: returns 200 even if no data exists for this jobId.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_job_serialize(
        self,
        job_id,
        x_tenant_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/jobs/{jobId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def export_job(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> bytearray:
        """Download the optimization result as a ZIP archive.

        Returns a ZIP archive of the persisted optimization result for the given job. If the result was stored with client-side encryption, provide the original passphrase via X-Encryption-Secret and the archive will be decrypted before streaming. For KMS-encrypted or unencrypted results the header can be omitted — decryption is handled transparently by the server. The Content-Disposition header carries the suggested filename.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def export_job_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Download the optimization result as a ZIP archive.

        Returns a ZIP archive of the persisted optimization result for the given job. If the result was stored with client-side encryption, provide the original passphrase via X-Encryption-Secret and the archive will be decrypted before streaming. For KMS-encrypted or unencrypted results the header can be omitted — decryption is handled transparently by the server. The Content-Disposition header carries the suggested filename.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def export_job_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Download the optimization result as a ZIP archive.

        Returns a ZIP archive of the persisted optimization result for the given job. If the result was stored with client-side encryption, provide the original passphrase via X-Encryption-Secret and the archive will be decrypted before streaming. For KMS-encrypted or unencrypted results the header can be omitted — decryption is handled transparently by the server. The Content-Disposition header carries the suggested filename.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _export_job_serialize(
        self,
        job_id,
        x_tenant_id,
        x_encryption_secret,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        if x_encryption_secret is not None:
            _header_params['X-Encryption-Secret'] = x_encryption_secret
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/octet-stream', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/export',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_errors(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of errors to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[JOptOptimizationError]:
        """Retrieve error messages for a job.

        Returns persisted error messages for the given job. Errors are only persisted if saveError was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of errors to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_errors_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationError]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_errors_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of errors to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[JOptOptimizationError]]:
        """Retrieve error messages for a job.

        Returns persisted error messages for the given job. Errors are only persisted if saveError was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of errors to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_errors_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationError]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_errors_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of errors to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve error messages for a job.

        Returns persisted error messages for the given job. Errors are only persisted if saveError was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of errors to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_errors_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationError]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_errors_serialize(
        self,
        job_id,
        x_tenant_id,
        limit,
        sort_direction,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if sort_direction is not None:
            
            _query_params.append(('sortDirection', sort_direction))
            
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/errors',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_progress(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of snapshots to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[JOptOptimizationProgress]:
        """Retrieve progress snapshots for a job.

        Returns persisted progress snapshots for the given job. Progress events are only persisted if saveProgress was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of snapshots to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_progress_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationProgress]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_progress_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of snapshots to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[JOptOptimizationProgress]]:
        """Retrieve progress snapshots for a job.

        Returns persisted progress snapshots for the given job. Progress events are only persisted if saveProgress was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of snapshots to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_progress_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationProgress]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_progress_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of snapshots to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve progress snapshots for a job.

        Returns persisted progress snapshots for the given job. Progress events are only persisted if saveProgress was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of snapshots to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_progress_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationProgress]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_progress_serialize(
        self,
        job_id,
        x_tenant_id,
        limit,
        sort_direction,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if sort_direction is not None:
            
            _query_params.append(('sortDirection', sort_direction))
            
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/progress',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_result(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RestOptimization:
        """Retrieve the full optimization result for a job.

        Loads the complete persisted optimization snapshot for the given jobId, scoped to the authenticated tenant. If the result was client-encrypted, provide the original secret via X-Encryption-Secret; for KMS-encrypted or unencrypted results the header can be omitted.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_result_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestOptimization",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_result_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RestOptimization]:
        """Retrieve the full optimization result for a job.

        Loads the complete persisted optimization snapshot for the given jobId, scoped to the authenticated tenant. If the result was client-encrypted, provide the original secret via X-Encryption-Secret; for KMS-encrypted or unencrypted results the header can be omitted.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_result_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestOptimization",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_result_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve the full optimization result for a job.

        Loads the complete persisted optimization snapshot for the given jobId, scoped to the authenticated tenant. If the result was client-encrypted, provide the original secret via X-Encryption-Secret; for KMS-encrypted or unencrypted results the header can be omitted.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results. Omit for KMS or unencrypted.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_result_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestOptimization",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_result_serialize(
        self,
        job_id,
        x_tenant_id,
        x_encryption_secret,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        if x_encryption_secret is not None:
            _header_params['X-Encryption-Secret'] = x_encryption_secret
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/result',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_solution(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Solution:
        """Retrieve the solution payload for a job.

        Returns the Solution portion of the optimization result only, omitting the full optimization input echo. Useful for lightweight integrations that do not need the complete RestOptimization envelope. If the result was client-encrypted, provide X-Encryption-Secret.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_solution_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Solution",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_solution_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Solution]:
        """Retrieve the solution payload for a job.

        Returns the Solution portion of the optimization result only, omitting the full optimization input echo. Useful for lightweight integrations that do not need the complete RestOptimization envelope. If the result was client-encrypted, provide X-Encryption-Secret.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_solution_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Solution",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_solution_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        x_encryption_secret: Annotated[Optional[StrictStr], Field(description="Client decryption secret. Required only for CLIENT-mode encrypted results.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve the solution payload for a job.

        Returns the Solution portion of the optimization result only, omitting the full optimization input echo. Useful for lightweight integrations that do not need the complete RestOptimization envelope. If the result was client-encrypted, provide X-Encryption-Secret.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param x_encryption_secret: Client decryption secret. Required only for CLIENT-mode encrypted results.
        :type x_encryption_secret: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_solution_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            x_encryption_secret=x_encryption_secret,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Solution",
            '401': "str",
            '404': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_solution_serialize(
        self,
        job_id,
        x_tenant_id,
        x_encryption_secret,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        if x_encryption_secret is not None:
            _header_params['X-Encryption-Secret'] = x_encryption_secret
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/solution',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_status(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of events to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[JOptOptimizationStatus]:
        """Retrieve status updates for a job.

        Returns persisted status lifecycle events for the given job (e.g. RUNNING, SUCCESS_WITH_SOLUTION, ERROR). Status events are only persisted if saveStatus was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of events to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_status_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationStatus]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_status_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of events to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[JOptOptimizationStatus]]:
        """Retrieve status updates for a job.

        Returns persisted status lifecycle events for the given job (e.g. RUNNING, SUCCESS_WITH_SOLUTION, ERROR). Status events are only persisted if saveStatus was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of events to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_status_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationStatus]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_status_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of events to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve status updates for a job.

        Returns persisted status lifecycle events for the given job (e.g. RUNNING, SUCCESS_WITH_SOLUTION, ERROR). Status events are only persisted if saveStatus was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of events to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_status_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationStatus]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_status_serialize(
        self,
        job_id,
        x_tenant_id,
        limit,
        sort_direction,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if sort_direction is not None:
            
            _query_params.append(('sortDirection', sort_direction))
            
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/status',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_job_warnings(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of warnings to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[JOptOptimizationWarning]:
        """Retrieve warning messages for a job.

        Returns persisted warning messages for the given job. Warnings are only persisted if saveWarning was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of warnings to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_warnings_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationWarning]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_job_warnings_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of warnings to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[JOptOptimizationWarning]]:
        """Retrieve warning messages for a job.

        Returns persisted warning messages for the given job. Warnings are only persisted if saveWarning was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of warnings to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_warnings_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationWarning]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_job_warnings_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of warnings to return.")] = None,
        sort_direction: Annotated[Optional[StrictStr], Field(description="Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.")] = None,
        time_out: Annotated[Optional[StrictStr], Field(description="Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve warning messages for a job.

        Returns persisted warning messages for the given job. Warnings are only persisted if saveWarning was enabled in the MongoOptimizationPersistenceSetting.

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param limit: Maximum number of warnings to return.
        :type limit: int
        :param sort_direction: Sort direction by event time: DESC (newest first) or ASC. Defaults to DESC.
        :type sort_direction: str
        :param time_out: Maximum time to wait for the database response (ISO 8601 duration). Defaults to PT1M.
        :type time_out: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_job_warnings_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            limit=limit,
            sort_direction=sort_direction,
            time_out=time_out,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[JOptOptimizationWarning]",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_job_warnings_serialize(
        self,
        job_id,
        x_tenant_id,
        limit,
        sort_direction,
        time_out,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if sort_direction is not None:
            
            _query_params.append(('sortDirection', sort_direction))
            
        if time_out is not None:
            
            _query_params.append(('timeOut', time_out))
            
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/jobs/{jobId}/warnings',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def import_job(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> JobAcceptedResponse:
        """Import a pre-computed optimization result into the database.

        Persists a RestOptimization payload directly without running the optimizer. The call blocks until the write completes. Returns a JobAcceptedResponse containing the generated jobId, which can be used immediately with GET /api/v1/jobs/{jobId}/result to retrieve the imported result. Persistence must be enabled in the RestOptimization extension settings. The tenant is scoped by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._import_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def import_job_with_http_info(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[JobAcceptedResponse]:
        """Import a pre-computed optimization result into the database.

        Persists a RestOptimization payload directly without running the optimizer. The call blocks until the write completes. Returns a JobAcceptedResponse containing the generated jobId, which can be used immediately with GET /api/v1/jobs/{jobId}/result to retrieve the imported result. Persistence must be enabled in the RestOptimization extension settings. The tenant is scoped by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._import_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def import_job_without_preload_content(
        self,
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant.")],
        rest_optimization: RestOptimization,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Import a pre-computed optimization result into the database.

        Persists a RestOptimization payload directly without running the optimizer. The call blocks until the write completes. Returns a JobAcceptedResponse containing the generated jobId, which can be used immediately with GET /api/v1/jobs/{jobId}/result to retrieve the imported result. Persistence must be enabled in the RestOptimization extension settings. The tenant is scoped by the X-Tenant-Id header.

        :param x_tenant_id: Tenant identifier injected by the API gateway. Scopes the persisted result to this tenant. (required)
        :type x_tenant_id: str
        :param rest_optimization: (required)
        :type rest_optimization: RestOptimization
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._import_job_serialize(
            x_tenant_id=x_tenant_id,
            rest_optimization=rest_optimization,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "JobAcceptedResponse",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _import_job_serialize(
        self,
        x_tenant_id,
        rest_optimization,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter
        if rest_optimization is not None:
            _body_params = rest_optimization


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/jobs/import',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_jobs(
        self,
        database_info_search: DatabaseInfoSearch,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[DatabaseInfoSearchResult]:
        """Search persisted optimization jobs and return metadata summaries.

        Accepts a DatabaseInfoSearch body and returns a stream of metadata summaries for all matching optimization jobs. All fields in the search body are optional and combinable. Results are sorted by upload date, newest first by default. Each entry contains a jobId that can be used directly with GET /api/v1/jobs/{jobId}/result to retrieve the full optimization result. Fields absent for encrypted jobs (creator, ident, status, createdTimeStamp) are omitted from each result entry. On-premise only: requires a connected database.

        :param database_info_search: (required)
        :type database_info_search: DatabaseInfoSearch
        :param x_tenant_id: Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_jobs_serialize(
            database_info_search=database_info_search,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DatabaseInfoSearchResult]",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_jobs_with_http_info(
        self,
        database_info_search: DatabaseInfoSearch,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[DatabaseInfoSearchResult]]:
        """Search persisted optimization jobs and return metadata summaries.

        Accepts a DatabaseInfoSearch body and returns a stream of metadata summaries for all matching optimization jobs. All fields in the search body are optional and combinable. Results are sorted by upload date, newest first by default. Each entry contains a jobId that can be used directly with GET /api/v1/jobs/{jobId}/result to retrieve the full optimization result. Fields absent for encrypted jobs (creator, ident, status, createdTimeStamp) are omitted from each result entry. On-premise only: requires a connected database.

        :param database_info_search: (required)
        :type database_info_search: DatabaseInfoSearch
        :param x_tenant_id: Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_jobs_serialize(
            database_info_search=database_info_search,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DatabaseInfoSearchResult]",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_jobs_without_preload_content(
        self,
        database_info_search: DatabaseInfoSearch,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search persisted optimization jobs and return metadata summaries.

        Accepts a DatabaseInfoSearch body and returns a stream of metadata summaries for all matching optimization jobs. All fields in the search body are optional and combinable. Results are sorted by upload date, newest first by default. Each entry contains a jobId that can be used directly with GET /api/v1/jobs/{jobId}/result to retrieve the full optimization result. Fields absent for encrypted jobs (creator, ident, status, createdTimeStamp) are omitted from each result entry. On-premise only: requires a connected database.

        :param database_info_search: (required)
        :type database_info_search: DatabaseInfoSearch
        :param x_tenant_id: Tenant identifier. When provided, results are scoped to this tenant. In on-premise single-tenant setups this header may be omitted.
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_jobs_serialize(
            database_info_search=database_info_search,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DatabaseInfoSearchResult]",
            '400': "str",
            '401': "str",
            '500': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_jobs_serialize(
        self,
        database_info_search,
        x_tenant_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter
        if database_info_search is not None:
            _body_params = database_info_search


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/jobs/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def stop_job(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> bool:
        """Stop a running job gracefully.

        Sends a graceful stop signal to the running optimization identified by jobId. The optimizer finishes its current iteration and persists the best result found so far. Returns immediately — the stop may take several seconds to complete. Poll GET /api/v1/jobs/{jobId}/status to confirm termination. Returns 200 if the job was found and the signal was sent. Returns 404 if the job is not running (already completed or never started).

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def stop_job_with_http_info(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bool]:
        """Stop a running job gracefully.

        Sends a graceful stop signal to the running optimization identified by jobId. The optimizer finishes its current iteration and persists the best result found so far. Returns immediately — the stop may take several seconds to complete. Poll GET /api/v1/jobs/{jobId}/status to confirm termination. Returns 200 if the job was found and the signal was sent. Returns 404 if the job is not running (already completed or never started).

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def stop_job_without_preload_content(
        self,
        job_id: Annotated[StrictStr, Field(description="Unique job identifier from the JobAcceptedResponse.")],
        x_tenant_id: Annotated[StrictStr, Field(description="Tenant identifier injected by the API gateway.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Stop a running job gracefully.

        Sends a graceful stop signal to the running optimization identified by jobId. The optimizer finishes its current iteration and persists the best result found so far. Returns immediately — the stop may take several seconds to complete. Poll GET /api/v1/jobs/{jobId}/status to confirm termination. Returns 200 if the job was found and the signal was sent. Returns 404 if the job is not running (already completed or never started).

        :param job_id: Unique job identifier from the JobAcceptedResponse. (required)
        :type job_id: str
        :param x_tenant_id: Tenant identifier injected by the API gateway. (required)
        :type x_tenant_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_job_serialize(
            job_id=job_id,
            x_tenant_id=x_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bool",
            '404': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _stop_job_serialize(
        self,
        job_id,
        x_tenant_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if job_id is not None:
            _path_params['jobId'] = job_id
        # process the query parameters
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['X-Tenant-Id'] = x_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'TenantId'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/jobs/{jobId}/stop',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


