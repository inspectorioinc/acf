from cached_property import cached_property

from base_api_client.wrappers.base import (
    BaseParamsWrapper, BaseResultContainer, BaseResultWrapper
)
from base_api_client.errors.http import ParamsError, ResultError


def initialize_url_template(cls):
    if hasattr(cls, 'URL_COMPONENTS'):
        cls.URL_TEMPLATE = '/'.join(cls.URL_COMPONENTS)
    return cls


class HttpParamsWrapper(BaseParamsWrapper):

    REQUEST_KWARGS = [
        'method', 'url', 'params',
        'data', 'headers', 'cookies',
        'files', 'auth', 'timeout', 'json'
    ]

    METHOD = None
    URL_COMPONENTS = None
    URL_TEMPLATE = None

    @cached_property
    def wrapped(self):
        try:
            return self.Meta.container(
                prepared_kwargs=self.build_kwargs()
            )
        except KeyError as error_key:
            raise ParamsError(
                message='Parameter `{}` is required.'.format(error_key),
                base_error=error_key
            )
        except Exception as error:
            raise ParamsError(
                message=getattr(error, 'message'),
                base_error=error
            )

    def build_kwargs(self):
        return {
            kwarg: getattr(
                self, 'build_{kwarg}'.format(kwarg=kwarg), self.build_empty
            )()
            for kwarg in self.REQUEST_KWARGS
        }

    def build_method(self):
        return self.METHOD

    def build_url(self):
        return self.URL_TEMPLATE.format(**self.raw_kwargs)

    def build_empty(self):
        pass


class HttpResultContainer(BaseResultContainer):

    def __init__(
        self, is_successful=True, parsed_result=None, raw_result=None
    ):
        super(HttpResultContainer, self).__init__(
            parsed_result=parsed_result, raw_result=raw_result
        )
        self.is_successful = is_successful


class HttpResultWrapper(BaseResultWrapper):

    class Meta:
        container = HttpResultContainer

    @cached_property
    def wrapped(self):
        try:
            return self.Meta.container(
                is_successful=self._is_successful,
                parsed_result=self._parsed_result,
                raw_result=self.raw_result
            )
        except Exception as error:
            raise ResultError(
                message=getattr(error, 'message'),
                base_error=error
            )

    @property
    def _is_successful(self):
        return True

    @property
    def _parsed_result(self):
        raise NotImplementedError()
