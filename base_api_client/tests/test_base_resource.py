import pytest

from base_api_client.errors.base import UnknownActionError
from base_api_client.resources.base import BaseResource


class Resource(BaseResource):
    ACTIONS = {'get': list}


def test_base_resource_getattr():
    resource = Resource()

    assert isinstance(resource.get, list)

    with pytest.raises(UnknownActionError):
        resource.unknown_action


def test_base_resource_dir():
    resource = Resource()
    assert 'get' in dir(resource)
