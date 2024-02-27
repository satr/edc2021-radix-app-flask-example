# BatchStatus

BatchStatus holds general information about batch status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_name** | **str** | BatchName Optional Batch ID of a job | [optional] 
**batch_type** | **str** | BatchType Single job or multiple jobs batch | [optional] 
**created** | **str** | Created timestamp | 
**ended** | **str** | Ended timestamp | [optional] 
**job_id** | **str** | JobId Optional ID of a job | [optional] 
**job_statuses** | [**List[JobStatus]**](JobStatus.md) | JobStatuses of the jobs in the batch | [optional] 
**message** | **str** | Message, if any, of the job | [optional] 
**name** | **str** | Name of the job | 
**started** | **str** | Started timestamp | [optional] 
**status** | **str** | Status of the job | [optional] 

## Example

```python
from openapi_client.models.batch_status import BatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStatus from a JSON string
batch_status_instance = BatchStatus.from_json(json)
# print the JSON string representation of the object
print BatchStatus.to_json()

# convert the object into a dict
batch_status_dict = batch_status_instance.to_dict()
# create an instance of BatchStatus from a dict
batch_status_form_dict = batch_status.from_dict(batch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


