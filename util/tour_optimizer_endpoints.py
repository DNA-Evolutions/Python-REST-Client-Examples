class Endpoints:
    LOCAL_SWAGGER_TOUROPTIMIZER_URL = "http://localhost:8081"
    AZURE_SWAGGER_TOUROPTIMIZER_URL = "https://joptaas.azure-api.net/touroptimizer/v2/"
    
    STREAM_REL_ENDPOINTS = [
    "/api/optimize/stream/progress",
    "/api/optimize/stream/status",
    "/api/optimize/stream/warning",
    "/api/optimize/stream/error"
]