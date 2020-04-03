# openapi_client.TagsApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aws_tag_data**](TagsApi.md#get_aws_tag_data) | **GET** /tags/aws/ | Query to obtain AWS tags
[**get_azure_tag_data**](TagsApi.md#get_azure_tag_data) | **GET** /tags/azure/ | Query to obtain AWS tags
[**get_open_shift_aws_tag_data**](TagsApi.md#get_open_shift_aws_tag_data) | **GET** /tags/openshift/infrastructures/aws/ | Query to obtain OpenShift-on-AWS tags
[**get_open_shift_azure_tag_data**](TagsApi.md#get_open_shift_azure_tag_data) | **GET** /tags/openshift/infrastructures/azure/ | Query to obtain OpenShift-on-Azure tags
[**get_open_shift_tag_data**](TagsApi.md#get_open_shift_tag_data) | **GET** /tags/openshift/ | Query to obtain OpenShift tags


# **get_aws_tag_data**
> Tags get_aws_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)

Query to obtain AWS tags

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
    api_instance = openapi_client.TagsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
key_only = True # bool | Flag to indicate whether or not only the tag key values will be returned. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain AWS tags
        api_response = api_instance.get_aws_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_aws_tag_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **key_only** | **bool**| Flag to indicate whether or not only the tag key values will be returned. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_tag_data**
> Tags get_azure_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)

Query to obtain AWS tags

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
    api_instance = openapi_client.TagsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
key_only = True # bool | Flag to indicate whether or not only the tag key values will be returned. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain AWS tags
        api_response = api_instance.get_azure_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_azure_tag_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **key_only** | **bool**| Flag to indicate whether or not only the tag key values will be returned. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_shift_aws_tag_data**
> Tags get_open_shift_aws_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)

Query to obtain OpenShift-on-AWS tags

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
    api_instance = openapi_client.TagsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
key_only = True # bool | Flag to indicate whether or not only the tag key values will be returned. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift-on-AWS tags
        api_response = api_instance.get_open_shift_aws_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_open_shift_aws_tag_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **key_only** | **bool**| Flag to indicate whether or not only the tag key values will be returned. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_shift_azure_tag_data**
> Tags get_open_shift_azure_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)

Query to obtain OpenShift-on-Azure tags

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
    api_instance = openapi_client.TagsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
key_only = True # bool | Flag to indicate whether or not only the tag key values will be returned. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift-on-Azure tags
        api_response = api_instance.get_open_shift_azure_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_open_shift_azure_tag_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **key_only** | **bool**| Flag to indicate whether or not only the tag key values will be returned. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_shift_tag_data**
> Tags get_open_shift_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)

Query to obtain OpenShift tags

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
    api_instance = openapi_client.TagsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
key_only = True # bool | Flag to indicate whether or not only the tag key values will be returned. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift tags
        api_response = api_instance.get_open_shift_tag_data(filter=filter, key_only=key_only, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_open_shift_tag_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **key_only** | **bool**| Flag to indicate whether or not only the tag key values will be returned. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

