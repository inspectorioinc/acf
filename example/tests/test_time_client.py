import pytest

from base_api_client.errors.http import ParseResponseError

from example.time_api_client import TimeClient


def test_time_client(requests_mock):
    url = 'http://worldclockapi.com/api/json/utc/now'
    method = 'GET'
    expected_response = (
        '{"$id":"1","currentDateTime":"2018-06-20T16:46Z","utcOffset":"00:00:0'
        '0","isDayLightSavingsTime":false,"dayOfTheWeek":"Wednesday","timeZone'
        'Name":"UTC","currentFileTime":131739868138015358,"ordinalDate":"2018-'
        '171","serviceResponse":null}'
    )

    requests_mock.request(method, url, text=expected_response)

    client = TimeClient()
    result = client.time.get_now(timezone='utc')

    assert result.is_successful
    assert result.result == '2018-06-20T16:46Z'
    assert result.response.status_code == 200


def test_time_client_error(requests_mock):
    url = 'http://worldclockapi.com/api/json/utc/now'
    method = 'GET'
    expected_response = 'not valid json'

    requests_mock.request(method, url, text=expected_response)

    client = TimeClient()
    with pytest.raises(ParseResponseError):
        client.time.get_now(timezone='utc')


def test_time_client_not_found(requests_mock):
    url = 'http://worldclockapi.com/api/json/utc/now'
    method = 'GET'
    expected_status_code = 404
    expected_response = 'not found'

    requests_mock.request(method, url, status_code=expected_status_code,
                          text=expected_response)

    client = TimeClient()
    result = client.time.get_now(timezone='utc')

    assert not result.is_successful
    assert result.result is None
    assert result.response.status_code == 404
