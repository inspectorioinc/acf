import pytest

from acf.errors.http import ParseResponseError

from . import HttpbinClient


class TestHttpbinClient(object):

    def test_send_anything(self, requests_mock):
        url = 'https://httpbin.org/anything'
        data = {'foo': 'bar'}
        expected_response = {'json': data}

        requests_mock.post(url, json=expected_response)

        client = HttpbinClient()
        result = client.anything.send(**data)

        assert result.is_successful
        assert result.result == data
        assert result.response.status_code == 200
        assert result.response.json() == expected_response

    def test_anything_parsing_error(self, requests_mock):
        url = 'https://httpbin.org/anything'

        requests_mock.post(url, text='not a valid json')

        client = HttpbinClient()
        with pytest.raises(ParseResponseError):
            client.anything.send(foo='bar')

    def test_update_status(self, requests_mock):
        client = HttpbinClient()

        for status in 200, 204, 404, 502:
            url = 'https://httpbin.org/status/{}'.format(status)
            requests_mock.put(url, status_code=status)
            result = client.status.update(status=status)
            assert result.result == status
