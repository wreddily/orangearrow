import requests

from .builder import AmazonRequestBuilder
from .response import AmazonItemSearchResponse, AmazonItemLookupResponse


class AmazonProductAPI(object):
    def __init__(self, access_key, secret_key, associate_tag):
        self.access_key = access_key
        self.secret_key = secret_key
        self.associate_tag = associate_tag
        self.request_builder = AmazonRequestBuilder(access_key, secret_key, associate_tag)

    @property
    def _base_default_params(self):
        return {
            'Service': 'AWSECommerceService',
            'AWSAccessKeyId': self.access_key,
            'AssociateTag': self.associate_tag,
            'ResponseGroup': 'Images,ItemAttributes',
            'Version': '2013-08-01'
        }

    def item_search(self, search_index, keywords=None, parameters=None, response_groups=None, page=None):
        if parameters is None:
            parameters = {}
        if response_groups is None:
            response_groups = []
        if keywords is None:
            keywords = []
        params = self._base_default_params
        params['Operation'] = 'ItemSearch'
        if search_index:
            params['SearchIndex'] = search_index
        if keywords:
            params['Keywords'] = ','.join(keywords)
        if response_groups:
            params['ResponseGroup'] = ','.join(response_groups)
        if page:
            params['ItemPage'] = page
        parameters.update(params)
        req_url = self.request_builder.build_request_url(parameters)
        response = self._make_get_request(req_url, AmazonItemSearchResponse)
        return response

    def item_lookup(self, item_id, id_type='ASIN', search_index=None, response_groups=None, parameters=None):
        if parameters is None:
            parameters = {}
        if response_groups is None:
            response_groups = []
        params = self._base_default_params
        params['Operation'] = 'ItemLookup'
        params['ItemId'] = item_id
        params['IdType'] = id_type
        if response_groups:
            params['ResponseGroup'] = ','.join(response_groups)
        if search_index:
            params['SearchIndex'] = search_index
        parameters.update(params)
        req_url = self.request_builder.build_request_url(parameters)
        response = self._make_get_request(req_url, AmazonItemLookupResponse)
        return response

    def _make_get_request(self, req_url, response_class):
        req = requests.get(req_url)
        response = response_class(req)
        return response
