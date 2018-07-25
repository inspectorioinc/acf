import pytest

from base_api_client.actions.http import HttpAction
from base_api_client.constants import defined
from base_api_client.errors import ImplementationError


class TestHttpAction(object):

    class BaseAction(HttpAction):
        URL_COMPONENTS = ['http://example.com', 'api', 'v1']

    def test_url_path_template(self):
        assert self.BaseAction.URL_PATH_TEMPLATE == 'http://example.com/api/v1'

    def test_trailing_slash(self):
        assert not defined(self.BaseAction.USE_TRAILING_SLASH)

        class TrailingSlashAction(self.BaseAction):
            USE_TRAILING_SLASH = True

        class AnotherAction(TrailingSlashAction):
            URL_COMPONENTS = ('test',)

        assert TrailingSlashAction.URL_PATH_TEMPLATE == 'http://example.com/' \
                                                        'api/v1/'
        assert AnotherAction.URL_PATH_TEMPLATE == 'http://example.com/' \
                                                  'api/v1/test/'

    def test_payload_required(self):
        assert not defined(self.BaseAction.PAYLOAD_REQUIRED)

        test_values = (
            ('GET', False),
            ('POST', True),
            ('PUT', True),
            ('PATCH', True),
            ('DELETE', False),
        )

        for method, expected_value in test_values:

            class Action(HttpAction):
                METHOD = method

            assert Action.PAYLOAD_REQUIRED is expected_value

        class BaseAction(HttpAction):
            PAYLOAD_REQUIRED = True

        class Action(BaseAction):
            METHOD = 'GET'

        assert Action.PAYLOAD_REQUIRED is True

    def test_path_params(self):
        BaseAction = self.BaseAction

        class EntityAction(BaseAction):
            URL_COMPONENTS = ('entity', '{entity_id}')

        class StatusAction(BaseAction):
            URL_PATH_TEMPLATE = BaseAction.URL_PATH_TEMPLATE + '/status/'
            URL_COMPONENTS = EntityAction.URL_COMPONENTS

        assert EntityAction.URL_PATH_TEMPLATE == 'http://example.com/api/v1/' \
                                                 'entity/{entity_id}'
        assert EntityAction.URL_PATH_PARAMS == {'entity_id'}

        assert StatusAction.URL_PATH_TEMPLATE == 'http://example.com/api/v1/' \
                                                 'status/entity/{entity_id}'
        assert StatusAction.URL_PATH_PARAMS == {'entity_id'}

        with pytest.raises(ImplementationError):
            class BrokenAction(HttpAction):
                URL_PATH_TEMPLATE = 'http://example.com/{}/test'

        with pytest.raises(ImplementationError):
            class AnotherBrokenAction(HttpAction):
                URL_COMPONENTS = ('{}', 'test')
