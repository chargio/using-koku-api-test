# openapi_client.CostModelsApi

All URIs are relative to *https://cloud.redhat.com/api/cost-management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_model**](CostModelsApi.md#create_cost_model) | **POST** /costmodels/ | Create a new cost model.
[**delete_cost_model**](CostModelsApi.md#delete_cost_model) | **DELETE** /costmodels/{cost_model_uuid}/ | Delete a Cost Model
[**get_cost_model**](CostModelsApi.md#get_cost_model) | **GET** /costmodels/{cost_model_uuid}/ | Get a Cost Model.
[**list_cost_models**](CostModelsApi.md#list_cost_models) | **GET** /costmodels/ | List the cost models
[**update_cost_model**](CostModelsApi.md#update_cost_model) | **PUT** /costmodels/{cost_model_uuid}/ | Update a Cost Model


# **create_cost_model**
> CostModelOut create_cost_model(cost_model)

Create a new cost model.

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
    api_instance = openapi_client.CostModelsApi(api_client)
    cost_model = openapi_client.CostModel() # CostModel | 

    try:
        # Create a new cost model.
        api_response = api_instance.create_cost_model(cost_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CostModelsApi->create_cost_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_model** | [**CostModel**](CostModel.md)|  | 

### Return type

[**CostModelOut**](CostModelOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An object describing the cost model |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cost_model**
> delete_cost_model(cost_model_uuid)

Delete a Cost Model

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
    api_instance = openapi_client.CostModelsApi(api_client)
    cost_model_uuid = 'cost_model_uuid_example' # str | UUID of Cost Model to get

    try:
        # Delete a Cost Model
        api_instance.delete_cost_model(cost_model_uuid)
    except ApiException as e:
        print("Exception when calling CostModelsApi->delete_cost_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_model_uuid** | [**str**](.md)| UUID of Cost Model to get | 

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
**204** | Cost Model deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cost_model**
> CostModelOut get_cost_model(cost_model_uuid)

Get a Cost Model.

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
    api_instance = openapi_client.CostModelsApi(api_client)
    cost_model_uuid = 'cost_model_uuid_example' # str | UUID of Cost Model to get

    try:
        # Get a Cost Model.
        api_response = api_instance.get_cost_model(cost_model_uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CostModelsApi->get_cost_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_model_uuid** | [**str**](.md)| UUID of Cost Model to get | 

### Return type

[**CostModelOut**](CostModelOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Cost Model object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_models**
> CostModelPagination list_cost_models(offset=offset, limit=limit, provider_uuid=provider_uuid, source_type=source_type, name=name, description=description, ordering=ordering)

List the cost models

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
    api_instance = openapi_client.CostModelsApi(api_client)
    offset = 0 # int | Parameter for selecting the offset of data. (optional) (default to 0)
limit = 10 # int | Parameter for selecting the amount of data in a returned. (optional) (default to 10)
provider_uuid = 'provider_uuid_example' # str | Filter response on provider uuid. (optional)
source_type = 'source_type_example' # str | Filter response on provider source type. (optional)
name = 'name_example' # str | Filter response on cost model name. (optional)
description = 'description_example' # str | Filter response on cost model description. (optional)
ordering = 'ordering_example' # str | Order response on cost model by allowed fields. (optional)

    try:
        # List the cost models
        api_response = api_instance.list_cost_models(offset=offset, limit=limit, provider_uuid=provider_uuid, source_type=source_type, name=name, description=description, ordering=ordering)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CostModelsApi->list_cost_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Parameter for selecting the offset of data. | [optional] [default to 0]
 **limit** | **int**| Parameter for selecting the amount of data in a returned. | [optional] [default to 10]
 **provider_uuid** | [**str**](.md)| Filter response on provider uuid. | [optional] 
 **source_type** | **str**| Filter response on provider source type. | [optional] 
 **name** | **str**| Filter response on cost model name. | [optional] 
 **description** | **str**| Filter response on cost model description. | [optional] 
 **ordering** | **str**| Order response on cost model by allowed fields. | [optional] 

### Return type

[**CostModelPagination**](CostModelPagination.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of cost model objects |  -  |
**401** | Unauthorized |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cost_model**
> CostModelOut update_cost_model(cost_model_uuid, cost_model)

Update a Cost Model

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
    api_instance = openapi_client.CostModelsApi(api_client)
    cost_model_uuid = 'cost_model_uuid_example' # str | UUID of Cost Model to get
cost_model = openapi_client.CostModel() # CostModel | Update to a Cost Model

    try:
        # Update a Cost Model
        api_response = api_instance.update_cost_model(cost_model_uuid, cost_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CostModelsApi->update_cost_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_model_uuid** | [**str**](.md)| UUID of Cost Model to get | 
 **cost_model** | [**CostModel**](CostModel.md)| Update to a Cost Model | 

### Return type

[**CostModelOut**](CostModelOut.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Cost Model object |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

