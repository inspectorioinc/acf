import pytest

from base_api_client.constants import UNDEFINED, defined


class TestConstants(object):

    def test_undefined(self):
        assert bool(UNDEFINED) is False
        assert str(UNDEFINED) == 'Undefined'

    def test_not_defined(self):
        assert not defined(UNDEFINED)

    @pytest.mark.parametrize('value', (None, 0, '', [], (), set()))
    def test_defined(self, value):
        assert defined(value)
