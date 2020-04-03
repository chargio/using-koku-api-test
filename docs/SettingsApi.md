# openapi_client.SettingsApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_settings**](SettingsApi.md#assign_settings) | **POST** /settings/ | Assign to cost management settings
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings/ | Query to cost management settings


# **assign_settings**
> assign_settings(setting_in=setting_in)

Assign to cost management settings

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
    api_instance = openapi_client.SettingsApi(api_client)
    setting_in = openapi_client.SettingIn() # SettingIn | Application settings that needs to stored (optional)

    try:
        # Assign to cost management settings
        api_instance.assign_settings(setting_in=setting_in)
    except ApiException as e:
        print("Exception when calling SettingsApi->assign_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_in** | [**SettingIn**](SettingIn.md)| Application settings that needs to stored | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings successfully stored |  -  |
**400** | Invalid Input Error |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> list[SettingOut] get_settings()

Query to cost management settings

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
    api_instance = openapi_client.SettingsApi(api_client)
    
    try:
        # Query to cost management settings
        api_response = api_instance.get_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SettingOut]**](SettingOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data driven forms components |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

