import requests
import six

from acf.errors.http import RequestError
from acf.protocols.base import BaseProtocol


class HttpProtocol(BaseProtocol):

    def execute(self, **kwargs):
        try:
            return self._perform_request(**kwargs)
        except Exception as error:
            return self._handle_error(error, **kwargs)

    def _perform_request(self, **kwargs):
        return requests.request(**kwargs)

    def _handle_error(self, error, **kwargs):
        raise RequestError(
            message=six.text_type(error),
            base_error=error
        )
