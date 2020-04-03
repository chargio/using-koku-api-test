# openapi_client.OpenShiftReportsApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_shift_aws_cost_reports**](OpenShiftReportsApi.md#get_open_shift_aws_cost_reports) | **GET** /reports/openshift/infrastructures/aws/costs/ | Query to obtain OpenShift on AWS cost reports
[**get_open_shift_aws_inventory_instance_report**](OpenShiftReportsApi.md#get_open_shift_aws_inventory_instance_report) | **GET** /reports/openshift/infrastructures/aws/instance-types/ | Query to obtain OpenShift on AWS instance data
[**get_open_shift_aws_inventory_storage_report**](OpenShiftReportsApi.md#get_open_shift_aws_inventory_storage_report) | **GET** /reports/openshift/infrastructures/aws/storage/ | Query to obtain OpenShift on AWS storage data
[**get_open_shift_azure_cost_reports**](OpenShiftReportsApi.md#get_open_shift_azure_cost_reports) | **GET** /reports/openshift/infrastructures/azure/costs/ | Query to obtain OpenShift on Azure cost reports
[**get_open_shift_azure_inventory_instance_report**](OpenShiftReportsApi.md#get_open_shift_azure_inventory_instance_report) | **GET** /reports/openshift/infrastructures/azure/instance-types/ | Query to obtain OpenShift on Azure instance data
[**get_open_shift_azure_inventory_storage_report**](OpenShiftReportsApi.md#get_open_shift_azure_inventory_storage_report) | **GET** /reports/openshift/infrastructures/azure/storage/ | Query to obtain OpenShift on Azure storage data
[**get_open_shift_compute_reports**](OpenShiftReportsApi.md#get_open_shift_compute_reports) | **GET** /reports/openshift/compute/ | Query to obtain OpenShift compute usage information
[**get_open_shift_cost_reports**](OpenShiftReportsApi.md#get_open_shift_cost_reports) | **GET** /reports/openshift/costs/ | Query to obtain cost reports
[**get_open_shift_memory_reports**](OpenShiftReportsApi.md#get_open_shift_memory_reports) | **GET** /reports/openshift/memory/ | Query to obtain OpenShift memory usage information
[**get_open_shift_volume_reports**](OpenShiftReportsApi.md#get_open_shift_volume_reports) | **GET** /reports/openshift/volumes/ | Query to obtain OpenShift volume usage information


# **get_open_shift_aws_cost_reports**
> ReportCosts get_open_shift_aws_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain OpenShift on AWS cost reports

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    delta = 'delta_example' # str | Toggle to include delta values in report. (optional)
filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on AWS cost reports
        api_response = api_instance.get_open_shift_aws_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_aws_cost_reports: %s\n" % e)
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

[**ReportCosts**](ReportCosts.md)

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

# **get_open_shift_aws_inventory_instance_report**
> ReportOpenShiftAWSInstanceInventory get_open_shift_aws_inventory_instance_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain OpenShift on AWS instance data

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on AWS instance data
        api_response = api_instance.get_open_shift_aws_inventory_instance_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_aws_inventory_instance_report: %s\n" % e)
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

[**ReportOpenShiftAWSInstanceInventory**](ReportOpenShiftAWSInstanceInventory.md)

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

# **get_open_shift_aws_inventory_storage_report**
> ReportOpenShiftAWSStorageInventory get_open_shift_aws_inventory_storage_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain OpenShift on AWS storage data

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on AWS storage data
        api_response = api_instance.get_open_shift_aws_inventory_storage_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_aws_inventory_storage_report: %s\n" % e)
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

[**ReportOpenShiftAWSStorageInventory**](ReportOpenShiftAWSStorageInventory.md)

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

# **get_open_shift_azure_cost_reports**
> ReportCosts get_open_shift_azure_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain OpenShift on Azure cost reports

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    delta = 'delta_example' # str | Toggle to include delta values in report. (optional)
filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on Azure cost reports
        api_response = api_instance.get_open_shift_azure_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_azure_cost_reports: %s\n" % e)
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

[**ReportCosts**](ReportCosts.md)

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

# **get_open_shift_azure_inventory_instance_report**
> ReportOpenShiftAzureInstanceInventory get_open_shift_azure_inventory_instance_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain OpenShift on Azure instance data

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on Azure instance data
        api_response = api_instance.get_open_shift_azure_inventory_instance_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_azure_inventory_instance_report: %s\n" % e)
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

[**ReportOpenShiftAzureInstanceInventory**](ReportOpenShiftAzureInstanceInventory.md)

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

# **get_open_shift_azure_inventory_storage_report**
> ReportOpenShiftAzureStorageInventory get_open_shift_azure_inventory_storage_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)

Query to obtain OpenShift on Azure storage data

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
units = 'units_example' # str | The units used to report data. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift on Azure storage data
        api_response = api_instance.get_open_shift_azure_inventory_storage_report(filter=filter, group_by=group_by, order_by=order_by, units=units, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_azure_inventory_storage_report: %s\n" % e)
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

[**ReportOpenShiftAzureStorageInventory**](ReportOpenShiftAzureStorageInventory.md)

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

# **get_open_shift_compute_reports**
> ReportOpenShiftCpu get_open_shift_compute_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain OpenShift compute usage information

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift compute usage information
        api_response = api_instance.get_open_shift_compute_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_compute_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportOpenShiftCpu**](ReportOpenShiftCpu.md)

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

# **get_open_shift_cost_reports**
> ReportCost get_open_shift_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    delta = 'delta_example' # str | Toggle to include delta values in report. (optional)
filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain cost reports
        api_response = api_instance.get_open_shift_cost_reports(delta=delta, filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_cost_reports: %s\n" % e)
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

# **get_open_shift_memory_reports**
> ReportOpenShiftMemory get_open_shift_memory_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain OpenShift memory usage information

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift memory usage information
        api_response = api_instance.get_open_shift_memory_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_memory_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportOpenShiftMemory**](ReportOpenShiftMemory.md)

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

# **get_open_shift_volume_reports**
> ReportOpenShiftVolume get_open_shift_volume_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)

Query to obtain OpenShift volume usage information

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
    api_instance = openapi_client.OpenShiftReportsApi(api_client)
    filter = None # object | The filter to apply to the report as a URL encoded dictionary. (optional)
group_by = None # object | The grouping to apply to the report as a URL encoded dictionary. (optional)
order_by = None # object | The ordering to apply to the report as a URL encoded dictionary. (optional)
offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 100 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 100)

    try:
        # Query to obtain OpenShift volume usage information
        api_response = api_instance.get_open_shift_volume_reports(filter=filter, group_by=group_by, order_by=order_by, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenShiftReportsApi->get_open_shift_volume_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| The filter to apply to the report as a URL encoded dictionary. | [optional] 
 **group_by** | [**object**](.md)| The grouping to apply to the report as a URL encoded dictionary. | [optional] 
 **order_by** | [**object**](.md)| The ordering to apply to the report as a URL encoded dictionary. | [optional] 
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 100]

### Return type

[**ReportOpenShiftVolume**](ReportOpenShiftVolume.md)

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

