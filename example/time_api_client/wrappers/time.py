import json

from base_api_client.wrappers.http import HttpParamsWrapper, HttpResultWrapper


class TimeParamsWrapper(HttpParamsWrapper):

    METHOD = 'GET'
    URL_TEMPLATE = 'http://worldclockapi.com/api/json/{timezone}/now'
    DEFAULT_TIMEZONE = 'utc'

    def build_url(self):
        return self.URL_TEMPLATE.format(
            timezone=self.raw_kwargs.get('timezone', self.DEFAULT_TIMEZONE)
        )


class TimeResultWrapper(HttpResultWrapper):

    @property
    def _parsed_result(self):
        return json.loads(self.raw_result.content)['currentDateTime']
