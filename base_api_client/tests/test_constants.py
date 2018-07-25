import pytest

from base_api_client.constants import NOT_SET, defined


class TestConstants(object):

    def test_not_set(self):
        assert bool(NOT_SET) is False
        assert str(NOT_SET) == 'NotSet'

    def test_not_defined(self):
        assert not defined(NOT_SET)

    @pytest.mark.parametrize('value', (None, 0, '', [], (), set()))
    def test_defined(self, value):
        assert defined(value)
