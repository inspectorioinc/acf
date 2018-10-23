import pytest

from acf.actions.base import BaseAction
from acf.errors import UnknownActionError
from acf.resources.base import BaseResource


class Action(BaseAction):
    pass


class Resource(BaseResource):
    ACTIONS = {'get': BaseAction}


def test_base_resource_getattr():
    resource = Resource()

    assert isinstance(resource.get, BaseAction)

    with pytest.raises(UnknownActionError):
        resource.unknown_action


def test_base_resource_dir():
    resource = Resource()
    assert 'get' in dir(resource)
