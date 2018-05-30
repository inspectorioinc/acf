import requests

from base_api_client.protocols.base import BaseProtocol


class HttpProtocol(BaseProtocol):

    def execute(self, method, url, *args, **kwargs):
        self._authenticate(*args, **kwargs)
        try:
            return self._perform_request(method, url, *args, **kwargs)
        except Exception as e:
            return self._handle_error(method, url, *args, **kwargs)

    def _authenticate(self, *args, **kwargs):
        pass

    def _perform_request(self, method, url, *args, **kwargs):
        return requests.request(method, url, **kwargs)

    def _handle_error(self, error, *args, **kwargs):
        pass
