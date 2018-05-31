import requests

from base_api_client.protocols.base import BaseProtocol
from base_api_client.errors.http import RequestError


class HttpProtocol(BaseProtocol):

    def execute(self, *args, **kwargs):
        try:
            return self._perform_request(*args, **kwargs)
        except Exception as error:
            return self._handle_error(error, *args, **kwargs)

    def _perform_request(self, method, url, *args, **kwargs):
        return requests.request(method, url, **kwargs)

    def _handle_error(self, error, *args, **kwargs):
        raise RequestError(
            message=getattr(error, 'message'),
            base_error=error
        )
