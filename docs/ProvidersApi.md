# openapi_client.ProvidersApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](ProvidersApi.md#create_provider) | **POST** /providers/ | Create a provider
[**delete_provider**](ProvidersApi.md#delete_provider) | **DELETE** /providers/{uuid}/ | Delete a provider
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /providers/{uuid}/ | Get a provider
[**list_providers**](ProvidersApi.md#list_providers) | **GET** /providers/ | List the providers
[**update_provider**](ProvidersApi.md#update_provider) | **PUT** /providers/{uuid}/ | Update a provider


# **create_provider**
> ProviderOut create_provider(provider_in)

Create a provider

### Example

* Basic Authentication (basic_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basic_auth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://cloud.redhat.com/api/cost-management/v1
configuration.host = "https://cloud.redhat.com/api/cost-management/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvidersApi(api_client)
    provider_in = openapi_client.ProviderIn() # ProviderIn | Provider to add to a Customer

    try:
        # Create a provider
        api_response = api_instance.create_provider(provider_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->create_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_in** | [**ProviderIn**](ProviderIn.md)| Provider to add to a Customer | 

### Return type

[**ProviderOut**](ProviderOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An object describing the provider |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> delete_provider(uuid)

Delete a provider

### Example

* Basic Authentication (basic_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basic_auth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://cloud.redhat.com/api/cost-management/v1
configuration.host = "https://cloud.redhat.com/api/cost-management/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvidersApi(api_client)
    uuid = 'uuid_example' # str | ID of provider to delete

    try:
        # Delete a provider
        api_instance.delete_provider(uuid)
    except ApiException as e:
        print("Exception when calling ProvidersApi->delete_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| ID of provider to delete | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Provider deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficent permissions to delete provider |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> ProviderOut get_provider(uuid, stats=stats)

Get a provider

### Example

* Basic Authentication (basic_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basic_auth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://cloud.redhat.com/api/cost-management/v1
configuration.host = "https://cloud.redhat.com/api/cost-management/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvidersApi(api_client)
    uuid = 'uuid_example' # str | ID of provider to get
stats = 'stats_example' # str | Include provider status (optional)

    try:
        # Get a provider
        api_response = api_instance.get_provider(uuid, stats=stats)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| ID of provider to get | 
 **stats** | **str**| Include provider status | [optional] 

### Return type

[**ProviderOut**](ProviderOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Provider object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProviderPagination list_providers(type=type, name=name, stats=stats, offset=offset, limit=limit)

List the providers

### Example

* Basic Authentication (basic_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basic_auth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://cloud.redhat.com/api/cost-management/v1
configuration.host = "https://cloud.redhat.com/api/cost-management/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvidersApi(api_client)
    type = 'type_example' # str | The type of provider to filter for. (optional)
name = 'name_example' # str | The name of the provider to filter for. (optional)
stats = 'stats_example' # str | Include provider status (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 10 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 10)

    try:
        # List the providers
        api_response = api_instance.list_providers(type=type, name=name, stats=stats, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->list_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of provider to filter for. | [optional] 
 **name** | **str**| The name of the provider to filter for. | [optional] 
 **stats** | **str**| Include provider status | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 10]

### Return type

[**ProviderPagination**](ProviderPagination.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of provider objects |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> ProviderOut update_provider(uuid, provider_in)

Update a provider

### Example

* Basic Authentication (basic_auth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basic_auth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://cloud.redhat.com/api/cost-management/v1
configuration.host = "https://cloud.redhat.com/api/cost-management/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvidersApi(api_client)
    uuid = 'uuid_example' # str | ID of provider to update
provider_in = openapi_client.ProviderIn() # ProviderIn | 

    try:
        # Update a provider
        api_response = api_instance.update_provider(uuid, provider_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->update_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| ID of provider to update | 
 **provider_in** | [**ProviderIn**](ProviderIn.md)|  | 

### Return type

[**ProviderOut**](ProviderOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Provider object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

