# openapi_client.AzureReportsApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_azure_cost_reports**](AzureReportsApi.md#get_azure_cost_reports) | **GET** /reports/azure/costs/ | Query to obtain cost reports
[**get_azure_instance_reports**](AzureReportsApi.md#get_azure_instance_reports) | **GET** /reports/azure/instance-types/ | Query to obtain Azure instance type data
[**get_azure_storage_reports**](AzureReportsApi.md#get_azure_storage_reports) | **GET** /reports/azure/storage/ | Query to obtain AWS storage data


# **get_azure_cost_reports**
> ReportCost get_azure_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain cost reports

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
    api_instance = openapi_client.AzureReportsApi(api_client)
    delta = 'delta_example' # str | Toggle to include delta values in report. (optional)
filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain cost reports
        api_response = api_instance.get_azure_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AzureReportsApi->get_azure_cost_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delta** | **str**| Toggle to include delta values in report. | [optional] 
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportCost**](ReportCost.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_instance_reports**
> ReportInstanceInventory get_azure_instance_reports(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain Azure instance type data

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
    api_instance = openapi_client.AzureReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain Azure instance type data
        api_response = api_instance.get_azure_instance_reports(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AzureReportsApi->get_azure_instance_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **units** | **str**| The units used to report data. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportInstanceInventory**](ReportInstanceInventory.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_storage_reports**
> ReportStorageInventory get_azure_storage_reports(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain AWS storage data

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
    api_instance = openapi_client.AzureReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain AWS storage data
        api_response = api_instance.get_azure_storage_reports(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AzureReportsApi->get_azure_storage_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **units** | **str**| The units used to report data. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportStorageInventory**](ReportStorageInventory.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated report object |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

