# RouteHeader

The header of the solution per route is summarizing important data like number of elements in the route , total time needed for the route etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | The abstract cost value of the route. | 
**time** | **str** | The time that is needed for the route. | 
**idle_time** | **str** | The accumlated idleTime of the route. | 
**prod_time** | **str** | The productive time of the route. Productive time is working-time spend at a node. | 
**tran_time** | **str** | The tranTime. The summed transit time of the route. | 
**termi_time** | **str** | The termiTime. The time taken from the last element to the termination element of the route. | 
**distance** | **str** | The distance. The summed transit distance of the route. | 
**termi_distance** | **str** | The termiDistance. The distance taken from the last element to the termination element of the route. | 
**route_violations** | [**List[Violation]**](Violation.md) | The routeViolations. Violations that occur on route level. For example, overtime, overdistance etc. | 
**is_closed** | **bool** | The isClosed boolean describes if a Resource has to visit the termination element of the Route. By default, the start element and the termination element of a Route is the Resource itself. In case of a closed route, by default, the Resource returns to its original starting location. | 
**is_alternate_destination** | **bool** | The isAlternateDestination boolean. Descibes of the Resource has an alternate destination. The Resource has to end it&#39;s Route at the alternate destination there but  will start from the original route start again the next working hour. | 

## Example

```python
from touroptimizer_py_client.models.route_header import RouteHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RouteHeader from a JSON string
route_header_instance = RouteHeader.from_json(json)
# print the JSON string representation of the object
print RouteHeader.to_json()

# convert the object into a dict
route_header_dict = route_header_instance.to_dict()
# create an instance of RouteHeader from a dict
route_header_form_dict = route_header.from_dict(route_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


