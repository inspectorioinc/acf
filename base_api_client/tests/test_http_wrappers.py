import mock

import pytest
from faker import Faker

from base_api_client.actions.http import HttpAction
from base_api_client.errors.http import ParamsError, ResultError
from base_api_client.wrappers.http import HttpParamsWrapper, HttpResultWrapper


class BaseAction(HttpAction):
    METHOD = 'GET'
    URL_PATH_TEMPLATE = 'http://example.com'


class TestHttpParamsWrapper(object):

    @staticmethod
    def get_wrapper(action_class, **kwargs):
        action = action_class()
        return HttpParamsWrapper(action=action, raw_kwargs=kwargs)

    @classmethod
    def get_wrapped_kwargs(cls, action_class, **kwargs):
        return cls.get_wrapper(action_class, **kwargs).wrapped

    def test_wrapped_params(self):

        class Action(BaseAction):
            URL_COMPONENTS = ['{entity_id}']

        wrapped_kwargs = self.get_wrapped_kwargs(Action, entity_id=1)
        assert wrapped_kwargs['url'] == 'http://example.com/1'

        expected_message = "Parameter 'entity_id' is required"
        with pytest.raises(ParamsError, match=expected_message):
            self.get_wrapped_kwargs(Action)

        message = Faker().sentence()
        with mock.patch.object(HttpParamsWrapper, 'build_kwargs',
                               side_effect=Exception(message)):
            with pytest.raises(ParamsError, match=message):
                self.get_wrapped_kwargs(Action)

    def test_build_params_and_json(self):
        foo_bar = {'foo': 'bar'}

        wrapped_kwargs = self.get_wrapped_kwargs(BaseAction)
        assert wrapped_kwargs['params'] == {}

        wrapped_kwargs = self.get_wrapped_kwargs(BaseAction, **foo_bar)
        assert wrapped_kwargs['params'] == foo_bar

        class Action(BaseAction):
            PAYLOAD_REQUIRED = True

        wrapped_kwargs = self.get_wrapped_kwargs(Action, **foo_bar)
        assert wrapped_kwargs['json'] == foo_bar
        assert wrapped_kwargs['params'] is None

        wrapped_kwargs = self.get_wrapped_kwargs(Action, data={}, **foo_bar)
        assert wrapped_kwargs['json'] == {}
        assert wrapped_kwargs['params'] == foo_bar

        class Action(BaseAction):
            PAYLOAD_PARAMS = {'value'}
            PAYLOAD_REQUIRED = True

        wrapped_kwargs = self.get_wrapped_kwargs(Action, value=1, **foo_bar)
        assert wrapped_kwargs['json'] == {'value': 1}
        assert wrapped_kwargs['params'] == foo_bar

        class Action(BaseAction):
            URL_QUERY_PARAMS = {'foo', 'bar'}

        faker = Faker()
        expected_params = {'foo': faker.word()}
        kwargs = dict(faker.pydict(), **expected_params)
        kwargs.pop('bar', None)
        wrapped_kwargs = self.get_wrapped_kwargs(Action, **kwargs)

        # 'bar' is not present and it's ok
        assert wrapped_kwargs['params'] == expected_params

    def test_build_headers(self):
        wrapped_kwargs = self.get_wrapped_kwargs(BaseAction)
        assert wrapped_kwargs['headers'] is None

        class Action(BaseAction):
            HEADERS_PARAMS = {'foo', 'bar'}

        faker = Faker()
        expected_headers = {'foo': faker.word()}
        kwargs = dict(faker.pydict(), **expected_headers)
        kwargs.pop('bar', None)
        wrapped_kwargs = self.get_wrapped_kwargs(Action, **kwargs)
        assert wrapped_kwargs['headers'] == expected_headers


class TestHttpResultWrapper(object):

    def test_wrapped_result(self, requests_mock):
        url = 'http://example.com'
        expected_result = {'foo': 'bar'}
        action = BaseAction()

        requests_mock.get(url, json=expected_result)
        result = action()
        assert result.is_successful
        assert result.result == expected_result

        requests_mock.get(url, status_code=500, text='Server error')
        result = action()
        assert not result.is_successful
        assert result.result is None

        message = Faker().sentence()
        with mock.patch.object(HttpResultWrapper.Meta, 'container',
                               side_effect=Exception(message)):
            with pytest.raises(ResultError, match=message):
                action()
