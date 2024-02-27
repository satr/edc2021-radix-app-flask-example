# coding: utf-8

"""
    Radix job scheduler server.

    This is the API Server for the Radix job scheduler server.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openapi_client.models.radix_node import RadixNode
from openapi_client.models.resource_requirements import ResourceRequirements

class RadixJobComponentConfig(BaseModel):
    """
    RadixJobComponentConfig holds description of RadixJobComponent  # noqa: E501
    """
    backoff_limit: Optional[StrictInt] = Field(None, alias="backoffLimit", description="BackoffLimit defines attempts to restart job if it fails. Corresponds to BackoffLimit in K8s.")
    image_tag_name: Optional[StrictStr] = Field(None, alias="imageTagName", description="ImageTagName defines the image tag name to use for the job image")
    node: Optional[RadixNode] = None
    resources: Optional[ResourceRequirements] = None
    time_limit_seconds: Optional[StrictInt] = Field(None, alias="timeLimitSeconds", description="TimeLimitSeconds defines maximum job run time. Corresponds to ActiveDeadlineSeconds in K8s.")
    __properties = ["backoffLimit", "imageTagName", "node", "resources", "timeLimitSeconds"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RadixJobComponentConfig:
        """Create an instance of RadixJobComponentConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of node
        if self.node:
            _dict['node'] = self.node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RadixJobComponentConfig:
        """Create an instance of RadixJobComponentConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RadixJobComponentConfig.parse_obj(obj)

        _obj = RadixJobComponentConfig.parse_obj({
            "backoff_limit": obj.get("backoffLimit"),
            "image_tag_name": obj.get("imageTagName"),
            "node": RadixNode.from_dict(obj.get("node")) if obj.get("node") is not None else None,
            "resources": ResourceRequirements.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "time_limit_seconds": obj.get("timeLimitSeconds")
        })
        return _obj

