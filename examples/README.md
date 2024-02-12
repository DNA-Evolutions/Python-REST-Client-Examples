# Python Examples

Python Examples are a collection of examples of using the JOpt TourOptimizer suite. The examples are utilizing the Python Client project.

## The Architecture
The utils project is subdivided into different parts:


### TourOptimizer 
Examples dealing with the use of DNA's JOpt containerized TourOptimizer, either via Azure as a service or a local docker instance. Please refer to  <a href="https://github.com/DNA-Evolutions/Docker-REST-TourOptimizer#how-to-start-jopttouroptimizer-docker" target="_blank">How to start JOpt TourOptimizer in docker</a> for more help.


**1. health\tour_optimizer_health_example.py:** Basic example on how to call the JOpt TourOptimizer service health status.

**2a. loadFAF\tour_optimizer_load_faf_example.py:** Guides how to load an optimization from a database

**2b. loadFAF\tour_optimizer_load_encrypted_faf_example.py:** Guides how to load an encrypted optimization from a database

**3. optimize\tour_optimizer_example.py:** Basic example on how to call the JOpt TourOptimizer service

**4. optimizeFAF\tour_optimizer_faf_example.py:** Demonstrates how to run an optimization and save it to the database

**5. searchFAF\tour_optimizer_search_faf_example.py:** Shows how to search optimizations within a database and display their meta info


For setting up a local test enviorment with database support, please refer to the separate **Hands-on Tutorial: Setting Up a Local Fire and Forget TourOptimizer-Database Test Environment** [tutorial](https://github.com/DNA-Evolutions/Docker-REST-TourOptimizer/blob/main/TourOptimizerWithDatabase.md).