# JobScheduleDescription

JobScheduleDescription holds description about scheduling job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff_limit** | **int** | BackoffLimit defines attempts to restart job if it fails. Corresponds to BackoffLimit in K8s. | [optional] 
**image_tag_name** | **str** | ImageTagName defines the image tag name to use for the job image | [optional] 
**job_id** | **str** | JobId Optional ID of a job | [optional] 
**node** | [**RadixNode**](RadixNode.md) |  | [optional] 
**payload** | **str** | Payload holding json data to be mapped to component | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**time_limit_seconds** | **int** | TimeLimitSeconds defines maximum job run time. Corresponds to ActiveDeadlineSeconds in K8s. | [optional] 

## Example

```python
from openapi_client.models.job_schedule_description import JobScheduleDescription

# TODO update the JSON string below
json = "{}"
# create an instance of JobScheduleDescription from a JSON string
job_schedule_description_instance = JobScheduleDescription.from_json(json)
# print the JSON string representation of the object
print JobScheduleDescription.to_json()

# convert the object into a dict
job_schedule_description_dict = job_schedule_description_instance.to_dict()
# create an instance of JobScheduleDescription from a dict
job_schedule_description_form_dict = job_schedule_description.from_dict(job_schedule_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


