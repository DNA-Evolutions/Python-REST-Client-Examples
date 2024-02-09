# coding: utf-8

"""
    DNA Evolutions - JOpt.TourOptimizer

    This is DNA's JOpt.TourOptimizer service. A RESTful Spring Boot application using springdoc-openapi and OpenAPI 3. JOpt.TourOpptimizer is a service that delivers route optimization and automatic scheduling features to be easily integrated into any third-party application. JOpt.TourOpptimizer encapsulates all necessary optimization functionality and provides a comprehensive REST API that offers a domain-specific optimization interface for the transportation industry. The service is stateless and does not come with graphical user interfaces, map depiction or any databases. These extensions and adjustments are supposed to be introduced by the consumer of the service while integrating it into his/her own application. The service will allow for many suitable adjustments and user-specific settings to adjust the behaviour and optimization goals (e.g. minimizing distance, maximizing resource utilization, etc.) through a comprehensive set of functions. This will enable you to gain control of the complete optimization processes.This service is based on JOpt (null)

    The version of the OpenAPI document: 1.2.6-SNAPSHOT
    Contact: info@dna-evolutions.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from touroptimizer_py_client.models.route_header import RouteHeader

class TestRouteHeader(unittest.TestCase):
    """RouteHeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteHeader:
        """Test RouteHeader
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteHeader`
        """
        model = RouteHeader()
        if include_optional:
            return RouteHeader(
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
                        value = '507.98525', 
                        desc = 'Late time [min]: 507.98525', 
                        category = 'CONSTRAINTVIOLATION', 
                        attribute = 'TIMECONSTRAINT', 
                        sub_attribute = 'LATE', 
                        code = 5, )
                    ],
                is_closed = True,
                is_alternate_destination = True
            )
        else:
            return RouteHeader(
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
                        value = '507.98525', 
                        desc = 'Late time [min]: 507.98525', 
                        category = 'CONSTRAINTVIOLATION', 
                        attribute = 'TIMECONSTRAINT', 
                        sub_attribute = 'LATE', 
                        code = 5, )
                    ],
                is_closed = True,
                is_alternate_destination = True,
        )
        """

    def testRouteHeader(self):
        """Test RouteHeader"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
