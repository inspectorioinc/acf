import requests

from base_api_client.protocol.base import BaseProtocol


class HttpProtocol(BaseProtocol):

    def execute(self, method, url, *args, **kwargs):
        return requests.request(method, url, **kwargs)