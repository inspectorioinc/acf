import json

from base_api_client.wrappers.http import HttpParamsWrapper, HttpResultWrapper


class TimeParamsWrapper(HttpParamsWrapper):

    METHOD = 'GET'
    URL_COMPONENTS = [
        'http://worldclockapi.com/api',
        'json/{timezone}/now'
    ]


class TimeResultWrapper(HttpResultWrapper):

    @property
    def parsed_result(self):
        return json.loads(self.raw_result.content)['currentDateTime']
