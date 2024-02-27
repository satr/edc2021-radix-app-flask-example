# ResourceRequirements

More info: https://www.radix.equinor.com/references/reference-radix-config/#resources-common

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **Dict[str, str]** |  | [optional] 
**requests** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.resource_requirements import ResourceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRequirements from a JSON string
resource_requirements_instance = ResourceRequirements.from_json(json)
# print the JSON string representation of the object
print ResourceRequirements.to_json()

# convert the object into a dict
resource_requirements_dict = resource_requirements_instance.to_dict()
# create an instance of ResourceRequirements from a dict
resource_requirements_form_dict = resource_requirements.from_dict(resource_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


