import pytest

from base_api_client.client.base import BaseClient


def test_base_client_getattr():
    class Client(BaseClient):
        RESOURCES = {'resource': list}

    client = Client()

    assert isinstance(client.resource, list)

    with pytest.raises(AttributeError):
        client.unknown_resource
