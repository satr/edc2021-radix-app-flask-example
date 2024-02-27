# BatchEvent

BatchEvent holds general information about batch event on change of status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_name** | **str** | BatchName Optional Batch ID of a job | [optional] 
**batch_type** | **str** | BatchType Single job or multiple jobs batch | [optional] 
**created** | **str** | Created timestamp | 
**ended** | **str** | Ended timestamp | [optional] 
**event** | **str** |  | 
**job_id** | **str** | JobId Optional ID of a job | [optional] 
**job_statuses** | [**List[JobStatus]**](JobStatus.md) | JobStatuses of the jobs in the batch | [optional] 
**message** | **str** | Message, if any, of the job | [optional] 
**name** | **str** | Name of the job | 
**started** | **str** | Started timestamp | [optional] 
**status** | **str** | Status of the job | [optional] 

## Example

```python
from openapi_client.models.batch_event import BatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEvent from a JSON string
batch_event_instance = BatchEvent.from_json(json)
# print the JSON string representation of the object
print BatchEvent.to_json()

# convert the object into a dict
batch_event_dict = batch_event_instance.to_dict()
# create an instance of BatchEvent from a dict
batch_event_form_dict = batch_event.from_dict(batch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


