import json
import xmltodict


class AmazonProductAPIResponse(object):
    def __init__(self, response_obj):
        self.status_code = response_obj.status_code
        self.raw_response = response_obj.content
        self.data = self._parse_data()
        self.headers = response_obj.headers

    def _parse_data(self):
        data_dict = json.loads(json.dumps(xmltodict.parse(self.raw_response, xml_attribs=False)))
        return data_dict

    @property
    def is_error(self):
        raise NotImplementedError

    @property
    def request_is_valid(self):
        raise NotImplementedError

    @property
    def error_msg(self):
        if self.is_error:
            return self._error_attrib('Message')

    @property
    def error_code(self):
        if self.is_error:
            return self._error_attrib('Code')

    def _error_attrib(self, attrib):
        raise NotImplementedError


class AmazonItemSearchResponse(AmazonProductAPIResponse):
    @property
    def is_error(self):
        return self.status_code >= 400 or not self.request_is_valid

    @property
    def request_is_valid(self):
        return self.data['ItemSearchResponse']['Items']['Request']['IsValid'] == 'True'

    def _error_attrib(self, attrib):
        return self.data['ItemSearchResponse']['Items']['Request']['Errors']['Error'][attrib]
