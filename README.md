# Python REST Client Examples for JOpt TourOptimizer

<a href="https://www.dna-evolutions.com/" target="_blank"><img src="https://www.dna-evolutions.com/images/dna_logo.png" width="200"
title="DNA-Evolutions" alt="DNA-Evolutions"></a>

Python examples for the [JOpt TourOptimizer](https://hub.docker.com/r/dnaevolutions/jopt_touroptimizer) REST API. Run route optimizations, monitor progress via SSE streams, and persist results to a database -- all from Python.

---

## Compatibility

Requires **JOpt TourOptimizer >= 1.3.5** ([Docker Hub](https://hub.docker.com/r/dnaevolutions/jopt_touroptimizer)).

The API models in this repository were generated from the [OpenAPI spec](https://github.com/DNA-Evolutions/Java-REST-Client-Examples/blob/master/src/main/resources/swagger/touroptimizer/spec/touroptimizer_spec.json).

---

## Quick start

### Option A: Clone and run locally

**Prerequisites**

- Python >= 3.9
- A running TourOptimizer instance (see [Quickstart Guide](https://dna-evolutions.com/docs/getting-started/quickstart/jopt_sandboxes_quickstart))

**Setup**

```bash
git clone https://github.com/DNA-Evolutions/Python-REST-Client-Examples.git
cd Python-REST-Client-Examples

# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# Install the package in editable mode with all dependencies
pip install -e .
```

**Run an example**

```bash
python examples/optimize/tour_optimizer_example.py
```

### Jupyter Notebooks (recommended for getting started)

The fastest way to learn JOpt in Python is through the interactive notebooks.
They walk you through each step with explanations, runnable code, and inline results.

```bash
pip install jupyter
jupyter notebook examples/notebooks/
```

| Notebook | Description |
|----------|-------------|
| [`tour_optimizer_example.ipynb`](examples/notebooks/tour_optimizer_example.ipynb) | **Start here.** Synchronous optimization: health check, build input, submit a run, inspect routes, export to JSON. |
| [`tour_optimizer_job_example.ipynb`](examples/notebooks/tour_optimizer_job_example.ipynb) | Job-based (fire-and-forget) optimization: submit to database, poll progress, retrieve results, search jobs, configure webhooks. |

> Inside the Docker sandbox, the notebooks are ready to use -- just open them in the file explorer and select the **"Python (JOpt)"** kernel.

### Option B: Use the browser-based sandbox (Docker)

No local Python installation needed. The sandbox provides a VS Code environment in your browser with all dependencies pre-installed.

```bash
docker run -it -d \
  --name jopt-py-rest-examples \
  -p 127.0.0.1:8033:8080 \
  -v "$PWD:/home/coder/project" \
  dnaevolutions/jopt_py_example_server:latest
```

Open [http://localhost:8033](http://localhost:8033) and log in with password **`jopt`**.

> The Dockerfile for building the sandbox is included under [`sandbox/python/`](sandbox/python/).

---

## Project structure

```
.
├── examples/
│   ├── notebooks/         # Jupyter notebooks (start here!)
│   ├── optimize/          # Synchronous optimization (start_run -> get_run_result)
│   ├── health/            # Health check (GET /api/v1/health)
│   ├── optimizeFAF/       # Job-based / fire-and-forget (create_job)
│   ├── searchFAF/         # List persisted jobs (list_jobs)
│   └── loadFAF/           # Load job result from database (get_job_result)
├── util/                  # Helper classes (REST caller, test data factories)
├── touroptimizer_py_client/  # Generated API client (do not edit manually)
├── requirements.txt
└── setup.py
```

### Examples overview

**Jupyter Notebooks** (interactive, best for learning):

| Notebook | Description |
|----------|-------------|
| `notebooks/tour_optimizer_example.ipynb` | Synchronous optimization end-to-end. |
| `notebooks/tour_optimizer_job_example.ipynb` | Job-based optimization with database persistence and webhooks. |

**Python scripts** (standalone, ready to run):

| Script | Description |
|--------|-------------|
| `optimize/tour_optimizer_example.py` | Submit an optimization, subscribe to SSE streams, and fetch the result. |
| `optimize/tour_optimizer_example_from_docker.py` | Same as above, using the Docker-to-host URL. |
| `health/tour_optimizer_health_example.py` | Check if the TourOptimizer service is reachable. |
| `optimizeFAF/tour_optimizer_faf_example.py` | Submit an async job with database persistence. |
| `searchFAF/tour_optimizer_search_faf_example.py` | Search for previously persisted jobs by creator. |
| `loadFAF/tour_optimizer_load_faf_example.py` | Load an unencrypted job result by job ID. |
| `loadFAF/tour_optimizer_load_encrypted_faf_example.py` | Load an encrypted job result with a decryption secret. |

---

## API architecture

The generated client in `touroptimizer_py_client/` provides four API classes:

| API class | Purpose |
|-----------|---------|
| `OptimizationApi` | Synchronous runs: `start_run` returns a `run_id`, then `get_run_result(run_id)` blocks until completion. |
| `StreamApi` | Subscribe to real-time SSE streams (progress, status, warnings, errors) for a given `run_id`. |
| `JobApi` | Asynchronous jobs with database persistence: `create_job`, `list_jobs`, `get_job_result`, etc. |
| `HealthApi` | Health check endpoint. |

The client was generated using the [OpenAPI Python Generator](https://openapi-generator.tech/docs/generators/python/):

```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate \
  -i /local/swagger/touroptimizer/spec/touroptimizer_spec.json \
  -g python \
  -o /local/generated/jopt-touroptimizer-py-client \
  --package-name=touroptimizer_py_client \
  --additional-properties="useOneOfDiscriminatorLookup=true"
```

You can also generate a client in other languages (C#, Java, TypeScript, Go, etc.) from the same OpenAPI spec.

---

## Troubleshooting

### Connection refused from the sandbox

```
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8081):
  Max retries exceeded ... [Errno 111] Connection refused
```

The sandbox runs inside a Docker container. Use `http://host.docker.internal:8081` instead of `http://localhost:8081`, or run `tour_optimizer_example_from_docker.py` which uses the correct endpoint automatically.

---

## Documentation

- [Quickstart Guide](https://dna-evolutions.com/docs/getting-started/quickstart/jopt_sandboxes_quickstart) -- Get up and running with TourOptimizer
- [REST Server Documentation](https://dna-evolutions.com/docs/learn-and-explore/rest/rest-server-touroptimizer) -- API details, database setup, and configuration
- [Docker Hub](https://hub.docker.com/r/dnaevolutions/jopt_touroptimizer) -- TourOptimizer Docker images
- [YouTube](https://www.youtube.com/channel/UCzfZjJLp5Rrk7U2UKsOf8Fw) -- Video tutorials
- [LinkedIn](https://www.linkedin.com/company/dna-evolutions/) -- Updates and news

---

## About JOpt

JOpt is a flexible routing optimization engine written in Java, designed for highly constrained tour-optimization problems -- time windows, skills, capacities, mandatory constraints, and more.

<a href="https://www.youtube.com/watch?v=U4mDQGnZGZs" target="_blank"><img src="https://dna-evolutions.com/wp-content/uploads/2021/02/joptIntrox169_small.png" width="500"
title="Introduction Video for DNA's JOpt" alt="Introduction Video for DNA's JOpt"></a>

---

## License

For our license agreement and information about license plans, please visit [www.dna-evolutions.com](https://www.dna-evolutions.com).

---

## Contact

[www.dna-evolutions.com](https://www.dna-evolutions.com) | [info@dna-evolutions.com](mailto:info@dna-evolutions.com)

A product by [DNA Evolutions](https://www.dna-evolutions.com) &copy;
