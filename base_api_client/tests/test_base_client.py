import pytest

from base_api_client.clients.base import BaseClient
from base_api_client.errors.base import UnknownResourceError


class Client(BaseClient):
    RESOURCES = {'resource': list}


def test_base_client_getattr():
    client = Client()

    assert isinstance(client.resource, list)

    with pytest.raises(UnknownResourceError):
        client.unknown_resource


def test_base_client_dir():
    client = Client()
    assert 'resource' in dir(client)
