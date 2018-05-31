from cached_property import cached_property

from base_api_client.wrappers.base import BaseResultWrapper, BaseParamsWrapper


class HttpParamsWrapper(BaseParamsWrapper):

    REQUEST_KWARGS = [
        'method', 'url', 'params',
        'data', 'headers', 'cookies',
        'auth', 'timeout', 'json'
    ]

    @cached_property
    def wrapped(self):
        return self.Meta.container(
            output_kwargs=self.build_kwargs()
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
        return self.Meta.container(
            result=self.parsed_result, raw_result=self.raw_result
        )

    @cached_property
    def parsed_result(self):
        raise NotImplementedError()
