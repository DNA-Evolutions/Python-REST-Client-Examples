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

from touroptimizer_py_client.api.read_database_service_controller_api import ReadDatabaseServiceControllerApi


class TestReadDatabaseServiceControllerApi(unittest.TestCase):
    """ReadDatabaseServiceControllerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReadDatabaseServiceControllerApi()

    def tearDown(self) -> None:
        pass

    def test_find_error(self) -> None:
        """Test case for find_error

        Find error by creator. Only works, if connected to a database.
        """
        pass

    def test_find_optimization(self) -> None:
        """Test case for find_optimization

        Find optimizations by creator and id. Only works, if connected to a database.
        """
        pass

    def test_find_progress(self) -> None:
        """Test case for find_progress

        Find progress by creator. Only works, if connected to a database.
        """
        pass

    def test_find_solution(self) -> None:
        """Test case for find_solution

        Find solutions by creator and id. Only works, if connected to a database.
        """
        pass

    def test_find_status(self) -> None:
        """Test case for find_status

        Find status by creator. Only works, if connected to a database.
        """
        pass

    def test_find_warning(self) -> None:
        """Test case for find_warning

        Find warning by creator. Only works, if connected to a database.
        """
        pass

    def test_finds_optimization_infos(self) -> None:
        """Test case for finds_optimization_infos

        Find optimization-infos by creator. Only works, if connected to a database.
        """
        pass

    def test_finds_solution_infos(self) -> None:
        """Test case for finds_solution_infos

        Find solution-infos by creator. Only works, if connected to a database.
        """
        pass


if __name__ == '__main__':
    unittest.main()
