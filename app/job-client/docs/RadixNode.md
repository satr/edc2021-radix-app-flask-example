# RadixNode

RadixNode defines node attributes, where container should be scheduled

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | **str** | Defines rules for allowed GPU types. More info: https://www.radix.equinor.com/references/reference-radix-config/#gpu +optional | [optional] 
**gpu_count** | **str** | Defines minimum number of required GPUs. +optional | [optional] 

## Example

```python
from openapi_client.models.radix_node import RadixNode

# TODO update the JSON string below
json = "{}"
# create an instance of RadixNode from a JSON string
radix_node_instance = RadixNode.from_json(json)
# print the JSON string representation of the object
print RadixNode.to_json()

# convert the object into a dict
radix_node_dict = radix_node_instance.to_dict()
# create an instance of RadixNode from a dict
radix_node_form_dict = radix_node.from_dict(radix_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


