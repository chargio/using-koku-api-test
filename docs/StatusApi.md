# openapi_client.StatusApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status/ | Obtain server status


# **get_status**
> Status get_status()

Obtain server status

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
    api_instance = openapi_client.StatusApi(api_client)
    
    try:
        # Obtain server status
        api_response = api_instance.get_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object describing the server status |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

