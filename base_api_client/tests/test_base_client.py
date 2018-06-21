import pytest
from faker import Faker

from base_api_client.clients.base import BaseClient
from base_api_client.errors.base import UnknownResourceError
from base_api_client.resources.base import BaseResource


class Resource(BaseResource):
    pass


class Client(BaseClient):
    RESOURCES = {'resource': Resource}


def test_base_client_init():
    client = Client()
    assert client.config == {}

    faker = Faker()
    config = faker.pydict()
    client = Client(config=config)
    assert client.config == config

    kwargs = faker.pydict()
    client = Client(config, **kwargs)
    config.update(**kwargs)
    assert client.config == config

    client = Client(**kwargs)
    assert client.config == kwargs

    token = faker.uuid4()
    client = Client(token=token)
    assert client.config == {'token': token}


def test_base_client_getattr():
    client = Client()

    assert isinstance(client.resource, Resource)

    with pytest.raises(UnknownResourceError):
        client.unknown_resource


def test_base_client_dir():
    client = Client()
    assert 'resource' in dir(client)
