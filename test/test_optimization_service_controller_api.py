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

from touroptimizer_py_client.api.optimization_service_controller_api import OptimizationServiceControllerApi


class TestOptimizationServiceControllerApi(unittest.TestCase):
    """OptimizationServiceControllerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OptimizationServiceControllerApi()

    def tearDown(self) -> None:
        pass

    def test_error(self) -> None:
        """Test case for error

        Stream of error. During the optimization run you can obtain optimization errors in percentage by subscribing to this stream
        """
        pass

    def test_progress(self) -> None:
        """Test case for progress

        Stream of progress. During the optimization run you can obtain the optimization progress in percentage and other useful information about the optimization progress by subscribing to this stream
        """
        pass

    def test_run(self) -> None:
        """Test case for run

        Provide an optimization and let JOpt solve it.
        """
        pass

    def test_run_only_result(self) -> None:
        """Test case for run_only_result

        Provide an optimization and let JOpt solve it. You only get back the result
        """
        pass

    def test_run_started_sginal(self) -> None:
        """Test case for run_started_sginal

        Emmits once an optimization started
        """
        pass

    def test_status(self) -> None:
        """Test case for status

        Stream of status messages. During the optimization run you can obtain the optimization status by subscribing to this stream
        """
        pass

    def test_stop_optimization_run(self) -> None:
        """Test case for stop_optimization_run

        This entrypoint stops the optimization gracefully.
        """
        pass

    def test_warning(self) -> None:
        """Test case for warning

        Stream of warning messages. During the optimization run you can obtain optimization warnings by subscribing to this stream
        """
        pass


if __name__ == '__main__':
    unittest.main()
