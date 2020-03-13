# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class CostModelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cost_model(self, cost_model, **kwargs):  # noqa: E501
        """Create a new cost model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cost_model(cost_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CostModel cost_model: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostModelOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_cost_model_with_http_info(cost_model, **kwargs)  # noqa: E501

    def create_cost_model_with_http_info(self, cost_model, **kwargs):  # noqa: E501
        """Create a new cost model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cost_model_with_http_info(cost_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CostModel cost_model: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostModelOut, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cost_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cost_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cost_model' is set
        if self.api_client.client_side_validation and ('cost_model' not in local_var_params or  # noqa: E501
                                                        local_var_params['cost_model'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cost_model` when calling `create_cost_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cost_model' in local_var_params:
            body_params = local_var_params['cost_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/costmodels/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostModelOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_cost_model(self, cost_model_uuid, **kwargs):  # noqa: E501
        """Delete a Cost Model  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cost_model(cost_model_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_cost_model_with_http_info(cost_model_uuid, **kwargs)  # noqa: E501

    def delete_cost_model_with_http_info(self, cost_model_uuid, **kwargs):  # noqa: E501
        """Delete a Cost Model  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cost_model_with_http_info(cost_model_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cost_model_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cost_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cost_model_uuid' is set
        if self.api_client.client_side_validation and ('cost_model_uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cost_model_uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cost_model_uuid` when calling `delete_cost_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cost_model_uuid' in local_var_params:
            path_params['cost_model_uuid'] = local_var_params['cost_model_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/costmodels/{cost_model_uuid}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cost_model(self, cost_model_uuid, **kwargs):  # noqa: E501
        """Get a Cost Model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cost_model(cost_model_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostModelOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_cost_model_with_http_info(cost_model_uuid, **kwargs)  # noqa: E501

    def get_cost_model_with_http_info(self, cost_model_uuid, **kwargs):  # noqa: E501
        """Get a Cost Model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cost_model_with_http_info(cost_model_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostModelOut, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cost_model_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cost_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cost_model_uuid' is set
        if self.api_client.client_side_validation and ('cost_model_uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cost_model_uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cost_model_uuid` when calling `get_cost_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cost_model_uuid' in local_var_params:
            path_params['cost_model_uuid'] = local_var_params['cost_model_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/costmodels/{cost_model_uuid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostModelOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_cost_models(self, **kwargs):  # noqa: E501
        """List the cost models  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cost_models(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: Parameter for selecting the offset of data.
        :param int limit: Parameter for selecting the amount of data in a returned.
        :param str provider_uuid: Filter response on provider uuid.
        :param str source_type: Filter response on provider source type.
        :param str name: Filter response on cost model name.
        :param str description: Filter response on cost model description.
        :param str ordering: Order response on cost model by allowed fields.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostModelPagination
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_cost_models_with_http_info(**kwargs)  # noqa: E501

    def list_cost_models_with_http_info(self, **kwargs):  # noqa: E501
        """List the cost models  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cost_models_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: Parameter for selecting the offset of data.
        :param int limit: Parameter for selecting the amount of data in a returned.
        :param str provider_uuid: Filter response on provider uuid.
        :param str source_type: Filter response on provider source type.
        :param str name: Filter response on cost model name.
        :param str description: Filter response on cost model description.
        :param str ordering: Order response on cost model by allowed fields.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostModelPagination, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['offset', 'limit', 'provider_uuid', 'source_type', 'name', 'description', 'ordering']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cost_models" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `list_cost_models`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_cost_models`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_cost_models`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'provider_uuid' in local_var_params and local_var_params['provider_uuid'] is not None:  # noqa: E501
            query_params.append(('provider_uuid', local_var_params['provider_uuid']))  # noqa: E501
        if 'source_type' in local_var_params and local_var_params['source_type'] is not None:  # noqa: E501
            query_params.append(('source_type', local_var_params['source_type']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'description' in local_var_params and local_var_params['description'] is not None:  # noqa: E501
            query_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/costmodels/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostModelPagination',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_cost_model(self, cost_model_uuid, cost_model, **kwargs):  # noqa: E501
        """Update a Cost Model  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_cost_model(cost_model_uuid, cost_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param CostModel cost_model: Update to a Cost Model (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostModelOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_cost_model_with_http_info(cost_model_uuid, cost_model, **kwargs)  # noqa: E501

    def update_cost_model_with_http_info(self, cost_model_uuid, cost_model, **kwargs):  # noqa: E501
        """Update a Cost Model  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_cost_model_with_http_info(cost_model_uuid, cost_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cost_model_uuid: UUID of Cost Model to get (required)
        :param CostModel cost_model: Update to a Cost Model (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostModelOut, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cost_model_uuid', 'cost_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_cost_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cost_model_uuid' is set
        if self.api_client.client_side_validation and ('cost_model_uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cost_model_uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cost_model_uuid` when calling `update_cost_model`")  # noqa: E501
        # verify the required parameter 'cost_model' is set
        if self.api_client.client_side_validation and ('cost_model' not in local_var_params or  # noqa: E501
                                                        local_var_params['cost_model'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cost_model` when calling `update_cost_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cost_model_uuid' in local_var_params:
            path_params['cost_model_uuid'] = local_var_params['cost_model_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cost_model' in local_var_params:
            body_params = local_var_params['cost_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/costmodels/{cost_model_uuid}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostModelOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
