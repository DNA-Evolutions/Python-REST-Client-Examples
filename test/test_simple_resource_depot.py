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

from touroptimizer_py_client.models.simple_resource_depot import SimpleResourceDepot

class TestSimpleResourceDepot(unittest.TestCase):
    """SimpleResourceDepot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleResourceDepot:
        """Test SimpleResourceDepot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleResourceDepot`
        """
        model = SimpleResourceDepot()
        if include_optional:
            return SimpleResourceDepot(
                maximal_unit_matched_capacity = 1.337,
                capacity_unit_map = {
                    'key' : 1.337
                    },
                per_kilometer_cost_factor_map = {
                    'key' : 56
                    },
                type_name = 'SimpleResourceDepot',
                empty_at_end_of_route_factor_map = {
                    'key' : 56
                    }
            )
        else:
            return SimpleResourceDepot(
                maximal_unit_matched_capacity = 1.337,
                type_name = 'SimpleResourceDepot',
        )
        """

    def testSimpleResourceDepot(self):
        """Test SimpleResourceDepot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
