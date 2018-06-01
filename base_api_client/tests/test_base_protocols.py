import pytest
import requests_mock

from base_api_client.protocols.base import BaseProtocol
from base_api_client.protocols.http import HttpProtocol


def test_base_protocol_execute():
    with pytest.raises(NotImplementedError):
        BaseProtocol().execute()


@requests_mock.mock()
def test_http_protocol_execute(requests_mocker):
    url = 'http://test.com'
    method = 'get'
    expected_response = 'some response'

    requests_mocker.request(method, url, text=expected_response)
    response = HttpProtocol().execute(method=method, url=url)

    assert response.text == expected_response
