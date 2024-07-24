# Python-REST-Client-Examples by DNA-Evolutions



<a href="https://dna-evolutions.com/" target="_blank"><img src="https://docs.dna-evolutions.com/indexres/dna-temp-logo.png" width="110"
title="DNA-Evolutions" alt="DNA-Evolutions"></a>


Containerizing an application helps to use it more conveniently across different platforms and, most importantly, as a microservice. Further, scaling an application becomes more straightforward as various standardized orchestration tools can be utilized. A Microservice can be launched either (locally) or, for example, as a highly-scalable web-micro-service in a Kubernetes cluster.

---

# Compatibility
This client can be used with <a href="https://hub.docker.com/r/dnaevolutions/jopt_touroptimizer" target="_blank">JOpt-TourOptimizer Spring Server</a>
Compatible Versions:
- 1.2.6-SNAPSHOT (this version was used to create the models of this repository)
- 1.2.7-SNAPSHOT (<a href="https://github.com/DNA-Evolutions/Java-REST-Client-Examples/blob/master/src/main/resources/swagger/touroptimizer/spec/touroptimizer_spec.json" target="_blank">Specs</a> )

---

# Further Documentation, Contact and Links

- Further documentation 	- <a href="https://docs.dna-evolutions.com" target="_blank">docs.dna-evolutions.com</a>
- Special features 	- <a href="https://docs.dna-evolutions.com/overview_docs/special_features/Special_Features.html" target="_blank">Overview of special features</a>
- Our official repository 	- <a href="https://public.repo.dna-evolutions.com" target="_blank">public.repo.dna-evolutions.com</a>
- Our official JavaDocs 		- <a href="https://public.javadoc.dna-evolutions.com" target="_blank">public.javadoc.dna-evolutions.com</a>
- Our YouTube channel - <a href="https://www.youtube.com/channel/UCzfZjJLp5Rrk7U2UKsOf8Fw" target="_blank">DNA Tutorials</a>
- Documentation - <a href="https://docs.dna-evolutions.com/rest/touroptimizer/rest_touroptimizer.html" target="_blank">DNA's RESTful Spring-TourOptimizer in Docker </a>
- Our DockerHub channel - <a href="https://hub.docker.com/u/dnaevolutions" target="_blank">DNA DockerHub</a>
- Our LinkedIn channel - <a href="https://www.linkedin.com/company/dna-evolutions/" target="_blank">DNA LinkedIn</a>


If you need any help, don't hesitate to get in contact with us via our company website <a href="https://www.dna-evolutions.com" target="_blank">www.dna-evolutions.com</a> or write an email to <a href="mailto:info@dna-evolutions.com">info@dna-evolutions.com</a>.


---


# Short Introduction
This repository is part of our JOpt-REST-Suite. It provides examples of how to set up a REST client in Python to access the following DNA Evolution's web services:

- JOpt-TourOptimizer based on JOpt-Core (available as a local Container and via Azure)

The service can be called via an API-Key using our Microsoft Azure-Kubernetes Infrastructure. If you are interested in hosting our JOpt-REST-GeoCoder and JOpt-REST-GeoRouter products in your environment, please get in contact with us.

All our RESTful Services utilize <a href="https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html" target="_blank">Spring WebFlux</a> and <a href="https://swagger.io/" target="_blank">Swagger</a>. Internally the Java version of TourOptimizer is used. Indeed all specifications for the different services are derived from the core library, leading to guaranteed compatibility between all three services.

<a href="https://dna-evolutions.com/" target="_blank"><img src="https://docs.dna-evolutions.com/indexres/dna-evolutions-product-infographic-jopt-cloud-integration-highres.svg" width="600"
title="DNA-Evolutions Integration" alt="DNA-Evolutions Integration"></a>

### JOpt-TourOptimizer
Optimize a problem consisting of Nodes, Resources, and optionally externally provided connections. In contrast to our other services, we allow you to host your JOpt-TourOptimizer locally. Please refer to <a href="https://github.com/DNA-Evolutions/Docker-REST-TourOptimizer#how-to-start-jopttouroptimizer-docker" target="_blank">"How to start JOpt TourOptimizer in docker"</a> for more help.

---

# Outline of this repository

Examples</a>
1. <a href="https://github.com/DNA-Evolutions/Python-REST-Client-Examples/tree/master/examples" target="_blank">TourOptimizer Python Examples</a>

Each of the sections has its README.

---


# The architecture of the generated REST-Client-API

The Python-REST-Client class files used by the examples of this repository were generated utilizing the <a href="https://openapi-generator.tech/docs/generators/python/" target="_blank">openapi-python Generator</a>  by <a href="https://github.com/OpenAPITools" target="_blank">OpenAPI Tools</a>.

For creating the models, we used the containerized version of Open-API-Generator by calling:

```xml
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate  -i '/local/swagger/touroptimizer/spec/touroptimizer_spec.json' -g python  -o /local/generated/jopt-touroptimizer-py-client  --package-name=touroptimizer_py_client --additional-properties="useOneOfDiscriminatorLookup=true"

```

where `${PWD}` needs to be adjusted to find the Open-API-docs under `/local/swagger/touroptimizer/spec/touroptimizer_spec.json` when mounting the volume `${PWD}` into `/local`. Calling the command will generate the Python client that is part of this repository. You can find the `touroptimizer_spec.json` <a href="https://github.com/DNA-Evolutions/Java-REST-Client-Examples/blob/master/src/main/resources/swagger/touroptimizer/spec/touroptimizer_spec.json" target="_blank">here</a>.

**Attention:** The generated models seem to have some bugs. The first commit of this repository is fixing those issues.

You can also generate a client in the programming language of your choice utilizing our API-docs. REST facilitates software integration in your desired language (including famous ones like C#, Java, JS, Scala, Python, and many more ). Don't hesitate to reach out to us if you need help setting up your client.


For setting up a local test enviorment with database support, please refer to the separate **Hands-on Tutorial: Setting Up a Local Fire and Forget TourOptimizer-Database Test Environment** [tutorial](https://github.com/DNA-Evolutions/Docker-REST-TourOptimizer/blob/main/TourOptimizerWithDatabase.md).

---

# Getting started

You can start using our examples:

* [Clone this repository](#clone-this-repository)
* [Use our sandbox in your browser (Docker required)](#use-our-sandbox-in-your-browser-docker-required)


## Clone this repository
Clone this repository and import it in your favourite IDE.

### Prerequisites

* Python installed
* Please check **requirements.txt**
* Working Docker environment for local TourOptimizer instance


### Install necessary files
You can call (from the main folder):

```bash
	python setup.py install
```
 
### Run the examples

Run a file from the **examples** subfolders. 


## Use our sandbox in your browser (Docker required)
If you want to get started without the hassle of installing Python and an IDE, we provide a sandbox. The sandbox is based on  [code-server](https://github.com/cdr/code-server) and can be used inside your browser, and the interface itself is based on Visual Code. The sandbox is available via DockerHub ([here](https://hub.docker.com/r/dnaevolutions/jopt_py_example_server)). You have to host the sandbox in your Docker environment (Please provide at least 2-4Gb of Ram and 2 Cores). You can pull the sandbox from our DockerHub account (The Dockerfile for creating the sandbox is included in this repository). The latest version of our examples is cloned by default on launching the Docker container, and you can start testing JOpt-PYthon-REST right away.


### Starting the sandbox and persist your changes
You must mount a volume to which the examples of this project are downloaded on the container's startup. After re-launching the container, the latest version of our examples is only cloned if the folder is not already existing, keeping your files safe from being overridden.

Launching a sandbox and mount your current directory ('$PWD') or any other directory you want:

```
docker run -it -d --name jopt-py-rest-examples -p 127.0.0.1:8033:8080 -v "$PWD/:/home/coder/project" dnaevolutions/jopt_py_example_server:latest
```

### Using the sandbox

After starting the container, you can open [http://localhost:8043/](http://localhost:8033) with your browser and login with the password:

```
jopt
```

### Common problems: ###

- If you see the an error like this:

```
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8081): Max retries exceeded with url: /healthStatus (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fc7c86ac1d0>: Failed to establish a new connection: [Errno 111] Connection refused'))
```

You are trying to connect to a local JOpt server but have not adjusted the endpoint. Remember, the sandbox is a docker container and you need to connect to it via the endpoint `http://host.docker.internal:8081` instead of ~`http://localhost:8081`~. You can run `tour_optimizer_example_from_docker.py` from the package `examples.optimize` where `Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_FROM_DOCKER_URL` is used instead of `Endpoints.LOCAL_SWAGGER_TOUROPTIMIZER_URL`.


---


## Why use JOpt products from DNA Evolutions?
JOpt is a flexible routing optimization engine written in Java, allowing to solve tour-optimization problems that are highly restricted. For example, regarding time windows, skills, and even mandatory constraints can be applied.

Click to open our video:

<a href="https://www.youtube.com/watch?v=U4mDQGnZGZs" target="_blank"><img src="https://dna-evolutions.com/wp-content/uploads/2021/02/joptIntrox169_small.png" width="500"
title="Introduction Video for DNA's JOpt" alt="Introduction Video for DNA's JOpt"></a>

---

## Agreement
For reading our license agreement and for further information about license plans, please visit <a href="https://www.dna-evolutions.com" target="_blank">www.dna-evolutions.com</a>.

--- 

## Authors
A product by [dna-evolutions ](https://www.dna-evolutions.com)&copy;
