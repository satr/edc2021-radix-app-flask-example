# coding: utf-8

"""
    Radix job scheduler server.

    This is the API Server for the Radix job scheduler server.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.radix_job_component_config import RadixJobComponentConfig  # noqa: E501

class TestRadixJobComponentConfig(unittest.TestCase):
    """RadixJobComponentConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RadixJobComponentConfig:
        """Test RadixJobComponentConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RadixJobComponentConfig`
        """
        model = RadixJobComponentConfig()  # noqa: E501
        if include_optional:
            return RadixJobComponentConfig(
                backoff_limit = 56,
                image_tag_name = '',
                node = openapi_client.models.radix_node.RadixNode(
                    gpu = '', 
                    gpu_count = '', ),
                resources = openapi_client.models.resource_requirements_describes_the_compute_resource_requirements/.ResourceRequirements describes the compute resource requirements.(
                    limits = {
                        'key' : ''
                        }, 
                    requests = {
                        'key' : ''
                        }, ),
                time_limit_seconds = 56
            )
        else:
            return RadixJobComponentConfig(
        )
        """

    def testRadixJobComponentConfig(self):
        """Test RadixJobComponentConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
