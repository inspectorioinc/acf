from base_api_client.wrappers.http import HttpParamsWrapper


def test_http_params_wrapper():

    class BaseWrapper(HttpParamsWrapper):
        URL_COMPONENTS = ['http://example.com', 'api', 'v1']

    class EntityWrapper(BaseWrapper):
        URL_COMPONENTS = ('entity', '{entity_id}')

    class StatusWrapper(BaseWrapper):
        URL_TEMPLATE = BaseWrapper.URL_TEMPLATE + '/status'
        URL_COMPONENTS = EntityWrapper.URL_COMPONENTS

    assert BaseWrapper.URL_TEMPLATE == 'http://example.com/api/v1'

    assert EntityWrapper.URL_TEMPLATE == 'http://example.com/api/v1/' \
                                         'entity/{entity_id}'

    assert StatusWrapper.URL_TEMPLATE == 'http://example.com/api/v1/' \
                                         'status/entity/{entity_id}'
