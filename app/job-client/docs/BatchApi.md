# openapi_client.BatchApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch**](BatchApi.md#create_batch) | **POST** /batches | Create batch
[**delete_batch**](BatchApi.md#delete_batch) | **DELETE** /batches/{batchName} | Delete batch
[**get_batch**](BatchApi.md#get_batch) | **GET** /batches/{batchName} | Gets batch
[**get_batch_job**](BatchApi.md#get_batch_job) | **GET** /batches/{batchName}/jobs/{jobName} | Gets batch job
[**get_batches**](BatchApi.md#get_batches) | **GET** /batches/ | Gets batches
[**stop_batch**](BatchApi.md#stop_batch) | **POST** /batches/{batchName}/stop | Stop batch
[**stop_batch_job**](BatchApi.md#stop_batch_job) | **POST** /batches/{batchName}/jobs/{jobName}/stop | Stop batch job


# **create_batch**
> BatchStatus create_batch(batch_creation)

Create batch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_schedule_description import BatchScheduleDescription
from openapi_client.models.batch_status import BatchStatus
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
    api_instance = openapi_client.BatchApi(api_client)
    batch_creation = openapi_client.BatchScheduleDescription() # BatchScheduleDescription | Batch to create

    try:
        # Create batch
        api_response = api_instance.create_batch(batch_creation)
        print("The response of BatchApi->create_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->create_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_creation** | [**BatchScheduleDescription**](BatchScheduleDescription.md)| Batch to create | 

### Return type

[**BatchStatus**](BatchStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful create batch |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**422** | Invalid data in request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_batch**
> Status delete_batch(batch_name)

Delete batch

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
    api_instance = openapi_client.BatchApi(api_client)
    batch_name = 'batch_name_example' # str | Name of batch

    try:
        # Delete batch
        api_response = api_instance.delete_batch(batch_name)
        print("The response of BatchApi->delete_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->delete_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_name** | **str**| Name of batch | 

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
**200** | Successful delete batch |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch**
> BatchStatus get_batch(batch_name)

Gets batch

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_status import BatchStatus
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
    api_instance = openapi_client.BatchApi(api_client)
    batch_name = 'batch_name_example' # str | Name of batch

    try:
        # Gets batch
        api_response = api_instance.get_batch(batch_name)
        print("The response of BatchApi->get_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_name** | **str**| Name of batch | 

### Return type

[**BatchStatus**](BatchStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get batch |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_job**
> JobStatus get_batch_job(batch_name, job_name)

Gets batch job

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
    api_instance = openapi_client.BatchApi(api_client)
    batch_name = 'batch_name_example' # str | Name of batch
    job_name = 'job_name_example' # str | Name of job

    try:
        # Gets batch job
        api_response = api_instance.get_batch_job(batch_name, job_name)
        print("The response of BatchApi->get_batch_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_batch_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_name** | **str**| Name of batch | 
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

# **get_batches**
> List[BatchStatus] get_batches()

Gets batches

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.batch_status import BatchStatus
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
    api_instance = openapi_client.BatchApi(api_client)

    try:
        # Gets batches
        api_response = api_instance.get_batches()
        print("The response of BatchApi->get_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_batches: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[BatchStatus]**](BatchStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get batches |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_batch**
> Status stop_batch(batch_name)

Stop batch

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
    api_instance = openapi_client.BatchApi(api_client)
    batch_name = 'batch_name_example' # str | Name of batch

    try:
        # Stop batch
        api_response = api_instance.stop_batch(batch_name)
        print("The response of BatchApi->stop_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->stop_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_name** | **str**| Name of batch | 

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
**200** | Successful stop batch |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_batch_job**
> Status stop_batch_job(batch_name, job_name)

Stop batch job

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
    api_instance = openapi_client.BatchApi(api_client)
    batch_name = 'batch_name_example' # str | Name of batch
    job_name = 'job_name_example' # str | Name of job

    try:
        # Stop batch job
        api_response = api_instance.stop_batch_job(batch_name, job_name)
        print("The response of BatchApi->stop_batch_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->stop_batch_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_name** | **str**| Name of batch | 
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
**200** | Successful stop batch job |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

