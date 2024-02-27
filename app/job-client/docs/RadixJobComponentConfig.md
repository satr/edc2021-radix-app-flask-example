# RadixJobComponentConfig

RadixJobComponentConfig holds description of RadixJobComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff_limit** | **int** | BackoffLimit defines attempts to restart job if it fails. Corresponds to BackoffLimit in K8s. | [optional] 
**image_tag_name** | **str** | ImageTagName defines the image tag name to use for the job image | [optional] 
**node** | [**RadixNode**](RadixNode.md) |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**time_limit_seconds** | **int** | TimeLimitSeconds defines maximum job run time. Corresponds to ActiveDeadlineSeconds in K8s. | [optional] 

## Example

```python
from openapi_client.models.radix_job_component_config import RadixJobComponentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RadixJobComponentConfig from a JSON string
radix_job_component_config_instance = RadixJobComponentConfig.from_json(json)
# print the JSON string representation of the object
print RadixJobComponentConfig.to_json()

# convert the object into a dict
radix_job_component_config_dict = radix_job_component_config_instance.to_dict()
# create an instance of RadixJobComponentConfig from a dict
radix_job_component_config_form_dict = radix_job_component_config.from_dict(radix_job_component_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


