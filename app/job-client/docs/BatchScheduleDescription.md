# BatchScheduleDescription

BatchScheduleDescription holds description about batch scheduling job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_radix_job_component_config** | [**RadixJobComponentConfig**](RadixJobComponentConfig.md) |  | [optional] 
**job_schedule_descriptions** | [**List[JobScheduleDescription]**](JobScheduleDescription.md) | JobScheduleDescriptions descriptions of jobs to schedule within the batch | 

## Example

```python
from openapi_client.models.batch_schedule_description import BatchScheduleDescription

# TODO update the JSON string below
json = "{}"
# create an instance of BatchScheduleDescription from a JSON string
batch_schedule_description_instance = BatchScheduleDescription.from_json(json)
# print the JSON string representation of the object
print BatchScheduleDescription.to_json()

# convert the object into a dict
batch_schedule_description_dict = batch_schedule_description_instance.to_dict()
# create an instance of BatchScheduleDescription from a dict
batch_schedule_description_form_dict = batch_schedule_description.from_dict(batch_schedule_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


