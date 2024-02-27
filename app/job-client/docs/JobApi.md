# openapi_client.JobApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobApi.md#create_job) | **POST** /jobs | Create job
[**delete_job**](JobApi.md#delete_job) | **DELETE** /jobs/{jobName} | Delete job
[**get_job**](JobApi.md#get_job) | **GET** /jobs/{jobName} | Gets job
[**get_jobs**](JobApi.md#get_jobs) | **GET** /jobs/ | Gets jobs
[**stop_job**](JobApi.md#stop_job) | **POST** /jobs/{jobName}/stop | Stop job


# **create_job**
> JobStatus create_job(job_creation)

Create job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_schedule_description import JobScheduleDescription
from openapi_client.models.job_status import JobStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.JobApi(api_client)
    job_creation = openapi_client.JobScheduleDescription() # JobScheduleDescription | Job to create

    try:
        # Create job
        api_response = api_instance.create_job(job_creation)
        print("The response of JobApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_creation** | [**JobScheduleDescription**](JobScheduleDescription.md)| Job to create | 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful create job |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**422** | Invalid data in request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> Status delete_job(job_name)

Delete job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.JobApi(api_client)
    job_name = 'job_name_example' # str | Name of job

    try:
        # Delete job
        api_response = api_instance.delete_job(job_name)
        print("The response of JobApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->delete_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| Name of job | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful delete job |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobStatus get_job(job_name)

Gets job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_status import JobStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.JobApi(api_client)
    job_name = 'job_name_example' # str | Name of job

    try:
        # Gets job
        api_response = api_instance.get_job(job_name)
        print("The response of JobApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| Name of job | 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get job |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> List[JobStatus] get_jobs()

Gets jobs

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_status import JobStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.JobApi(api_client)

    try:
        # Gets jobs
        api_response = api_instance.get_jobs()
        print("The response of JobApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_jobs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[JobStatus]**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get jobs |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_job**
> Status stop_job(job_name)

Stop job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.JobApi(api_client)
    job_name = 'job_name_example' # str | Name of job

    try:
        # Stop job
        api_response = api_instance.stop_job(job_name)
        print("The response of JobApi->stop_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->stop_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| Name of job | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful delete job |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

