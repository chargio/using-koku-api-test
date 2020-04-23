# openapi_client.SourcesApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source**](SourcesApi.md#get_source) | **GET** /sources/{source_id}/ | Get a source
[**get_source_stats**](SourcesApi.md#get_source_stats) | **GET** /sources/{source_id}/stats/ | Get a source statistics
[**list_sources**](SourcesApi.md#list_sources) | **GET** /sources/ | List the sources
[**update_source**](SourcesApi.md#update_source) | **PATCH** /sources/{source_id}/ | Update a source


# **get_source**
> SourceOut get_source(source_id)

Get a source

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
    api_instance = openapi_client.SourcesApi(api_client)
    source_id = 1 # int | ID of source to get

    try:
        # Get a source
        api_response = api_instance.get_source(source_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SourcesApi->get_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of source to get | 

### Return type

[**SourceOut**](SourceOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Source object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_stats**
> object get_source_stats(source_id)

Get a source statistics

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
    api_instance = openapi_client.SourcesApi(api_client)
    source_id = 1 # int | ID of source to get

    try:
        # Get a source statistics
        api_response = api_instance.get_source_stats(source_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SourcesApi->get_source_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of source to get | 

### Return type

**object**

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Source Statistics object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources**
> SourcePagination list_sources(type=type, name=name, offset=offset, limit=limit)

List the sources

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
    api_instance = openapi_client.SourcesApi(api_client)
    type = 'type_example' # str | The type of source to filter for. (optional)
name = 'name_example' # str | The name of the source to filter for. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 10 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 10)

    try:
        # List the sources
        api_response = api_instance.list_sources(type=type, name=name, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of source to filter for. | [optional] 
 **name** | **str**| The name of the source to filter for. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 10]

### Return type

[**SourcePagination**](SourcePagination.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of source objects |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> SourceOut update_source(source_id, source_in)

Update a source

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
    api_instance = openapi_client.SourcesApi(api_client)
    source_id = 1 # int | ID of source to update
source_in = openapi_client.SourceIn() # SourceIn | 

    try:
        # Update a source
        api_response = api_instance.update_source(source_id, source_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SourcesApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of source to update | 
 **source_in** | [**SourceIn**](SourceIn.md)|  | 

### Return type

[**SourceOut**](SourceOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Source object |  -  |
**424** | Dependency not available |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

