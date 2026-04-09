"""
Endpoint configuration for the JOpt TourOptimizer REST API.

Defines base URLs for connecting to the TourOptimizer service in different environments
(local, Docker, Azure) and provides helper methods for constructing stream endpoint paths.
"""


class Endpoints:
    LOCAL_SWAGGER_TOUROPTIMIZER_URL = "http://localhost:8081"
    LOCAL_SWAGGER_TOUROPTIMIZER_FROM_DOCKER_URL = "http://host.docker.internal:8081"
    AZURE_SWAGGER_TOUROPTIMIZER_URL = "https://joptaas.azure-api.net/touroptimizer/v2/"

    @staticmethod
    def stream_rel_endpoints(run_id: str):
        """
        Returns the relative SSE stream endpoint paths for a given run.

        These paths are appended to the base URL to subscribe to real-time
        progress, status, warning, and error streams during an optimization run.

        :param run_id: The run identifier returned by POST /api/v1/runs.
        :return: List of relative endpoint paths for SSE streams.
        """
        return [
            f"/api/v1/runs/{run_id}/stream/progress",
            f"/api/v1/runs/{run_id}/stream/status",
            f"/api/v1/runs/{run_id}/stream/warnings",
            f"/api/v1/runs/{run_id}/stream/errors"
        ]
