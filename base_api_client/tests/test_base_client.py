import pytest

from base_api_client.clients.base import BaseClient
from base_api_client.errors.base import UnknownResourceError


def test_base_client_getattr():
    class Client(BaseClient):
        RESOURCES = {'resource': list}

    client = Client()

    assert isinstance(client.resource, list)

    with pytest.raises(UnknownResourceError):
        client.unknown_resource
