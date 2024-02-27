# JobStatus

JobStatus holds general information about job status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_name** | **str** | BatchName Optional Batch ID of a job | [optional] 
**created** | **str** | Created timestamp | 
**ended** | **str** | Ended timestamp | [optional] 
**job_id** | **str** | JobId Optional ID of a job | [optional] 
**message** | **str** | Message, if any, of the job | [optional] 
**name** | **str** | Name of the job | 
**started** | **str** | Started timestamp | [optional] 
**status** | **str** | Status of the job | [optional] 

## Example

```python
from openapi_client.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print JobStatus.to_json()

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_form_dict = job_status.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


