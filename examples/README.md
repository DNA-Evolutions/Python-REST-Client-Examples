# Python Examples

Python Examples are a collection of examples of using the JOpt TourOptimizer suite. The examples are utilizing the Python Client project.

## The Architecture
The utils project is subdivided into different parts:


### TourOptimizer 
Examples dealing with the use of DNA's JOpt containerized TourOptimizer, either via Azure as a service or a local docker instance. Please refer to  <a href="https://github.com/DNA-Evolutions/Docker-REST-TourOptimizer#how-to-start-jopttouroptimizer-docker" target="_blank">How to start JOpt TourOptimizer in docker</a> for more help.


**1. health\tour_optimizer_health_example.py:** Basic example on how to call the JOpt TourOptimizer service health status.

**2a. loadFAF\tour_optimizer_load_faf_example.py:** Guides how to load a job result from the database.

**2b. loadFAF\tour_optimizer_load_encrypted_faf_example.py:** Guides how to load an encrypted job result from the database.

**3. optimize\tour_optimizer_example.py:** Basic example on how to call the JOpt TourOptimizer service. Uses `start_run` to obtain a `run_id`, then fetches the result via `get_run_result`.

**4. optimizeFAF\tour_optimizer_faf_example.py:** Demonstrates how to create an optimization job and persist it to the database.

**5. searchFAF\tour_optimizer_search_faf_example.py:** Shows how to list jobs within a database and display their meta info.


**6a. notebooks\tour_optimizer_example.ipynb:** Interactive Jupyter notebook walking through the full synchronous optimization workflow step by step -- health check, input creation, optimization, result inspection, and JSON export.

**6b. notebooks\tour_optimizer_job_example.ipynb:** Interactive Jupyter notebook for the job-based (fire-and-forget) workflow -- submit a job, poll for progress, retrieve the result from the database, search for jobs, and configure completion webhooks.


For more documentation, please refer to our <a href="https://dna-evolutions.com/docs/learn-and-explore/rest/rest-server-touroptimizer" target="_blank">documentation hub</a>.
