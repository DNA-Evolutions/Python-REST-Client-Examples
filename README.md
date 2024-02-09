# touroptimizer-py-client
This is DNA's JOpt.TourOptimizer service. A RESTful Spring Boot application using springdoc-openapi and OpenAPI 3. JOpt.TourOpptimizer is a service that delivers route optimization and automatic scheduling features to be easily integrated into any third-party application. JOpt.TourOpptimizer encapsulates all necessary optimization functionality and provides a comprehensive REST API that offers a domain-specific optimization interface for the transportation industry. The service is stateless and does not come with graphical user interfaces, map depiction or any databases. These extensions and adjustments are supposed to be introduced by the consumer of the service while integrating it into his/her own application. The service will allow for many suitable adjustments and user-specific settings to adjust the behaviour and optimization goals (e.g. minimizing distance, maximizing resource utilization, etc.) through a comprehensive set of functions. This will enable you to gain control of the complete optimization processes.This service is based on JOpt (null)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.2.6-SNAPSHOT
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://dna-evolutions.com](https://dna-evolutions.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import touroptimizer_py_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import touroptimizer_py_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import touroptimizer_py_client
from touroptimizer_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = touroptimizer_py_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with touroptimizer_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = touroptimizer_py_client.OptimizationFAFServiceControllerApi(api_client)
    rest_optimization = touroptimizer_py_client.RestOptimization() # RestOptimization | 

    try:
        # Provide an optimization and let JOpt solve it.
        api_response = api_instance.run_faf(rest_optimization)
        print("The response of OptimizationFAFServiceControllerApi->run_faf:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OptimizationFAFServiceControllerApi->run_faf: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OptimizationFAFServiceControllerApi* | [**run_faf**](docs/OptimizationFAFServiceControllerApi.md#run_faf) | **POST** /api/optimizefaf/runFAF | Provide an optimization and let JOpt solve it.
*OptimizationFAFServiceControllerApi* | [**run_only_result_faf**](docs/OptimizationFAFServiceControllerApi.md#run_only_result_faf) | **POST** /api/optimizefaf/runOnlyResultFAF | 
*OptimizationHealthControllerApi* | [**health_status**](docs/OptimizationHealthControllerApi.md#health_status) | **GET** /healthStatus | Get the health status of this endpoint.
*OptimizationServiceControllerApi* | [**error**](docs/OptimizationServiceControllerApi.md#error) | **GET** /api/optimize/stream/error | Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
*OptimizationServiceControllerApi* | [**progress**](docs/OptimizationServiceControllerApi.md#progress) | **GET** /api/optimize/stream/progress | Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
*OptimizationServiceControllerApi* | [**run**](docs/OptimizationServiceControllerApi.md#run) | **POST** /api/optimize/run | Provide an optimization and let JOpt solve it.
*OptimizationServiceControllerApi* | [**run_only_result**](docs/OptimizationServiceControllerApi.md#run_only_result) | **POST** /api/optimize/runOnlyResult | Provide an optimization and let JOpt solve it. You only get back the result
*OptimizationServiceControllerApi* | [**run_started_sginal**](docs/OptimizationServiceControllerApi.md#run_started_sginal) | **GET** /api/optimize/startedSginal | Emmits once an optimization started
*OptimizationServiceControllerApi* | [**status**](docs/OptimizationServiceControllerApi.md#status) | **GET** /api/optimize/stream/status | Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
*OptimizationServiceControllerApi* | [**stop_optimization_run**](docs/OptimizationServiceControllerApi.md#stop_optimization_run) | **POST** /api/optimize/stop | This entrypoint stops the optimization gracefully.
*OptimizationServiceControllerApi* | [**warning**](docs/OptimizationServiceControllerApi.md#warning) | **GET** /api/optimize/stream/warning | Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream
*ReadDatabaseEncryptedServiceControllerApi* | [**find_encrypted_optimization**](docs/ReadDatabaseEncryptedServiceControllerApi.md#find_encrypted_optimization) | **POST** /api/db/read/findEncryptedOptimization | Find encrypted optimizations by id and creator. Only works, if connected to a database.
*ReadDatabaseEncryptedServiceControllerApi* | [**find_encrypted_solution**](docs/ReadDatabaseEncryptedServiceControllerApi.md#find_encrypted_solution) | **POST** /api/db/read/findEncryptedSolution | Find encrypted solutions by id and creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_error**](docs/ReadDatabaseServiceControllerApi.md#find_error) | **POST** /api/db/read/findError | Find error by creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_optimization**](docs/ReadDatabaseServiceControllerApi.md#find_optimization) | **POST** /api/db/read/findOptimization | Find optimizations by creator and id. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_progress**](docs/ReadDatabaseServiceControllerApi.md#find_progress) | **POST** /api/db/read/findProgress | Find progress by creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_solution**](docs/ReadDatabaseServiceControllerApi.md#find_solution) | **POST** /api/db/read/findSolution | Find solutions by creator and id. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_status**](docs/ReadDatabaseServiceControllerApi.md#find_status) | **POST** /api/db/read/findStatus | Find status by creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**find_warning**](docs/ReadDatabaseServiceControllerApi.md#find_warning) | **POST** /api/db/read/findWarning | Find warning by creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**finds_optimization_infos**](docs/ReadDatabaseServiceControllerApi.md#finds_optimization_infos) | **POST** /api/db/read/findsOptimizationInfos | Find optimization-infos by creator. Only works, if connected to a database.
*ReadDatabaseServiceControllerApi* | [**finds_solution_infos**](docs/ReadDatabaseServiceControllerApi.md#finds_solution_infos) | **POST** /api/db/read/findsSolutionInfos | Find solution-infos by creator. Only works, if connected to a database.
*HealthStatusApi* | [**health_status**](docs/HealthStatusApi.md#health_status) | **GET** /healthStatus | Get the health status of this endpoint.
*OptimizationApi* | [**run**](docs/OptimizationApi.md#run) | **POST** /api/optimize/run | Provide an optimization and let JOpt solve it.
*OptimizationApi* | [**run_only_result**](docs/OptimizationApi.md#run_only_result) | **POST** /api/optimize/runOnlyResult | Provide an optimization and let JOpt solve it. You only get back the result
*OptimizationApi* | [**stop_optimization_run**](docs/OptimizationApi.md#stop_optimization_run) | **POST** /api/optimize/stop | This entrypoint stops the optimization gracefully.
*OptimizationFAFApi* | [**run_faf**](docs/OptimizationFAFApi.md#run_faf) | **POST** /api/optimizefaf/runFAF | Provide an optimization and let JOpt solve it.
*OptimizationFAFApi* | [**run_only_result_faf**](docs/OptimizationFAFApi.md#run_only_result_faf) | **POST** /api/optimizefaf/runOnlyResultFAF | 
*StreamApi* | [**error**](docs/StreamApi.md#error) | **GET** /api/optimize/stream/error | Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
*StreamApi* | [**progress**](docs/StreamApi.md#progress) | **GET** /api/optimize/stream/progress | Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
*StreamApi* | [**status**](docs/StreamApi.md#status) | **GET** /api/optimize/stream/status | Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
*StreamApi* | [**warning**](docs/StreamApi.md#warning) | **GET** /api/optimize/stream/warning | Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream


## Documentation For Models

 - [AbsoluteNodeColorCapacity](docs/AbsoluteNodeColorCapacity.md)
 - [AbsoluteNodeColorMultiRouteConstraint](docs/AbsoluteNodeColorMultiRouteConstraint.md)
 - [BindingResourceConstraint](docs/BindingResourceConstraint.md)
 - [CapacityResource](docs/CapacityResource.md)
 - [ConnectedConstraint](docs/ConnectedConstraint.md)
 - [ConnectionByTime](docs/ConnectionByTime.md)
 - [ConnectionRelatedLateMargin](docs/ConnectionRelatedLateMargin.md)
 - [Constraint](docs/Constraint.md)
 - [ConstraintType](docs/ConstraintType.md)
 - [CoreBuildOptions](docs/CoreBuildOptions.md)
 - [CreatorSetting](docs/CreatorSetting.md)
 - [DatabaseEncryptedItemSearch](docs/DatabaseEncryptedItemSearch.md)
 - [DatabaseInfoSearch](docs/DatabaseInfoSearch.md)
 - [DatabaseInfoSearchResult](docs/DatabaseInfoSearchResult.md)
 - [DatabaseItemSearch](docs/DatabaseItemSearch.md)
 - [DateDef](docs/DateDef.md)
 - [DegradingLoadCapacity](docs/DegradingLoadCapacity.md)
 - [DifferentVisitorNodeRelation](docs/DifferentVisitorNodeRelation.md)
 - [EdgeElementConnection](docs/EdgeElementConnection.md)
 - [ElementConnection](docs/ElementConnection.md)
 - [ElementConnectionType](docs/ElementConnectionType.md)
 - [EncodedPolyline](docs/EncodedPolyline.md)
 - [EventNode](docs/EventNode.md)
 - [EventPillarNode](docs/EventPillarNode.md)
 - [ExcludingResourceConstraint](docs/ExcludingResourceConstraint.md)
 - [GeoAddress](docs/GeoAddress.md)
 - [GeoNode](docs/GeoNode.md)
 - [GeoPillarNode](docs/GeoPillarNode.md)
 - [ILoad](docs/ILoad.md)
 - [ILoadCapacity](docs/ILoadCapacity.md)
 - [INodeDepot](docs/INodeDepot.md)
 - [IResourceDepot](docs/IResourceDepot.md)
 - [IdleEventNode](docs/IdleEventNode.md)
 - [IntegerMultiConstraintHelperItem](docs/IntegerMultiConstraintHelperItem.md)
 - [JOptOptimizationError](docs/JOptOptimizationError.md)
 - [JOptOptimizationProgress](docs/JOptOptimizationProgress.md)
 - [JOptOptimizationStatus](docs/JOptOptimizationStatus.md)
 - [JOptOptimizationWarning](docs/JOptOptimizationWarning.md)
 - [JSONConfig](docs/JSONConfig.md)
 - [LoadDimension](docs/LoadDimension.md)
 - [LocationParameters](docs/LocationParameters.md)
 - [LongLongPair](docs/LongLongPair.md)
 - [MixedFlexLoad](docs/MixedFlexLoad.md)
 - [MongoOptimizationPersistenceSetting](docs/MongoOptimizationPersistenceSetting.md)
 - [MultiTimeWindowNodeRelation](docs/MultiTimeWindowNodeRelation.md)
 - [Node](docs/Node.md)
 - [NodeColor](docs/NodeColor.md)
 - [NodeColorCapacity](docs/NodeColorCapacity.md)
 - [NodeColorMultiRouteConstraint](docs/NodeColorMultiRouteConstraint.md)
 - [NodeRelation](docs/NodeRelation.md)
 - [NodeRelationType](docs/NodeRelationType.md)
 - [NodeType](docs/NodeType.md)
 - [OfferedNode](docs/OfferedNode.md)
 - [OpeningHours](docs/OpeningHours.md)
 - [OptimizationKeySetting](docs/OptimizationKeySetting.md)
 - [OptimizationOptions](docs/OptimizationOptions.md)
 - [OptimizationPersistenceSetting](docs/OptimizationPersistenceSetting.md)
 - [OptimizationPersistenceStratgySetting](docs/OptimizationPersistenceStratgySetting.md)
 - [OptimizationStatus](docs/OptimizationStatus.md)
 - [PluginSetting](docs/PluginSetting.md)
 - [PluginSettings](docs/PluginSettings.md)
 - [Position](docs/Position.md)
 - [Qualification](docs/Qualification.md)
 - [QualificationType](docs/QualificationType.md)
 - [ReducedNodeEdgeConnectorItem](docs/ReducedNodeEdgeConnectorItem.md)
 - [RequestFlexLoad](docs/RequestFlexLoad.md)
 - [Resource](docs/Resource.md)
 - [ResourceLocationConstraint](docs/ResourceLocationConstraint.md)
 - [ResourceTrip](docs/ResourceTrip.md)
 - [ResourceType](docs/ResourceType.md)
 - [ResourceWithPriority](docs/ResourceWithPriority.md)
 - [RestOptimization](docs/RestOptimization.md)
 - [Route](docs/Route.md)
 - [RouteElementDetail](docs/RouteElementDetail.md)
 - [RouteHeader](docs/RouteHeader.md)
 - [RouteTrip](docs/RouteTrip.md)
 - [SameVisitorNodeRelation](docs/SameVisitorNodeRelation.md)
 - [SecurityHelperItemMetadata](docs/SecurityHelperItemMetadata.md)
 - [SimpleLoad](docs/SimpleLoad.md)
 - [SimpleLoadCapacity](docs/SimpleLoadCapacity.md)
 - [SimpleNodeDepot](docs/SimpleNodeDepot.md)
 - [SimpleResourceDepot](docs/SimpleResourceDepot.md)
 - [Solution](docs/Solution.md)
 - [SolutionHeader](docs/SolutionHeader.md)
 - [StartReductionTimeDefinition](docs/StartReductionTimeDefinition.md)
 - [StartReductionTimeIncludeDefinition](docs/StartReductionTimeIncludeDefinition.md)
 - [StartReductionTimePillarDefinition](docs/StartReductionTimePillarDefinition.md)
 - [Status](docs/Status.md)
 - [StayOutCycleDefinition](docs/StayOutCycleDefinition.md)
 - [StayOutDefinition](docs/StayOutDefinition.md)
 - [StreamPersistenceStratgySetting](docs/StreamPersistenceStratgySetting.md)
 - [StringIntegerPair](docs/StringIntegerPair.md)
 - [SupplyFlexLoad](docs/SupplyFlexLoad.md)
 - [TextSolution](docs/TextSolution.md)
 - [TimeComparisonJuncture](docs/TimeComparisonJuncture.md)
 - [TimeWindowNodeRelation](docs/TimeWindowNodeRelation.md)
 - [TypeConstraint](docs/TypeConstraint.md)
 - [TypeQualification](docs/TypeQualification.md)
 - [TypeWithExpertise](docs/TypeWithExpertise.md)
 - [TypeWithExpertiseConstraint](docs/TypeWithExpertiseConstraint.md)
 - [TypeWithExpertiseQualification](docs/TypeWithExpertiseQualification.md)
 - [UKPostCode](docs/UKPostCode.md)
 - [UKPostCodeConstraint](docs/UKPostCodeConstraint.md)
 - [UKPostCodeQualification](docs/UKPostCodeQualification.md)
 - [UnloadAllLoad](docs/UnloadAllLoad.md)
 - [Violation](docs/Violation.md)
 - [WorkingHours](docs/WorkingHours.md)
 - [ZoneNumber](docs/ZoneNumber.md)
 - [ZoneNumberConstraint](docs/ZoneNumberConstraint.md)
 - [ZoneNumberQualification](docs/ZoneNumberQualification.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

info@dna-evolutions.com


