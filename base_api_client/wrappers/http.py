from cached_property import cached_property

from base_api_client.wrappers.base import BaseResultWrapper, BaseParamsWrapper
from base_api_client.errors.http import ParamsError, ResultError


class HttpParamsWrapper(BaseParamsWrapper):

    REQUEST_KWARGS = [
        'method', 'url', 'params',
        'data', 'headers', 'cookies',
        'auth', 'timeout', 'json'
    ]

    @cached_property
    def wrapped(self):
        try:
            return self.Meta.container(
                prepared_kwargs=self.build_kwargs()
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

    def build_empty(self):
        pass


class HttpResultWrapper(BaseResultWrapper):

    @cached_property
    def wrapped(self):
        try:
            return self.Meta.container(
                parsed_result=self.parsed_result,
                raw_result=self.raw_result
            )
        except Exception as error:
            raise ResultError(
                message=getattr(error, 'message'),
                base_error=error
            )

    @cached_property
    def parsed_result(self):
        raise NotImplementedError()
