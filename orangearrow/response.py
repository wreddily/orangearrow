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

    def _error_attrib(self, attrib):
        return list(self.data.values())[0]['Error'][attrib]

    @property
    def error_msg(self):
        if self.is_error:
            return self._error_attrib('Message')

    @property
    def error_code(self):
        if self.is_error:
            return self._error_attrib('Code')

    @property
    def is_error(self):
        return True if self.status_code >= 400 else False
