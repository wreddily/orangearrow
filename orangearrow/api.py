import requests

from .builder import AmazonRequestBuilder
from .response import AmazonProductAPIResponse


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
        }

    def item_search(self, search_index, keywords=None, parameters=None, response_groups=None):
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
        parameters.update(params)
        req_url = self.request_builder.build_request_url(parameters)
        response = self._make_get_request(req_url)
        return response

    def _make_get_request(self, req_url):
        req = requests.get(req_url)
        response = AmazonProductAPIResponse(req)
        return response