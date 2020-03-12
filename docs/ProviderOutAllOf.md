# ProviderOutAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**authentication** | [**ProviderAuthenticationOut**](ProviderAuthenticationOut.md) |  | 
**billing_source** | [**ProviderBillingSourceOut**](ProviderBillingSourceOut.md) |  | 
**customer** | [**CustomerOut**](CustomerOut.md) |  | 
**created_by** | [**UserOut**](UserOut.md) |  | 
**stats** | [**object**](.md) | Dictionary key is the start of a billing month.  Value is report processing statistics. | [optional] 
**infrastructure** | **str** | OpenShift foundational infrastructure type. | [optional] 
**active** | **bool** | Flag to indicate when the provider is configured correctly | [optional] 
**cost_models** | [**list[ProviderOutAllOfCostModels]**](ProviderOutAllOfCostModels.md) | List of cost model name and UUIDs associated with this provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


