# SourceOutAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**authentication** | [**object**](.md) | Dictionary containing resource name. | [optional] 
**billing_source** | [**object**](.md) | Dictionary containing billing source. | [optional] 
**provider_linked** | **bool** | Flag to indicate if provider is linked to source. | [optional] [default to False]
**infrastructure** | **str** | OpenShift foundational infrastructure type. | [optional] 
**cost_models** | [**list[ProviderOutAllOfCostModels]**](ProviderOutAllOfCostModels.md) | List of cost model name and UUIDs associated with this provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


