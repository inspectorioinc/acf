from cached_property import cached_property
from six import add_metaclass

from base_api_client.wrappers.base import BaseParamsWrapper, BaseResultWrapper
from base_api_client.wrappers.http.containers import HttpResultContainer
from base_api_client.errors.http import ParamsError, ResultError

__all__ = ['HttpParamsWrapper', 'HttpResultWrapper']


class HttpParamsWrapperMetaclass(type):
    """
    Metaclass that updates URL_TEMPLATE constant
    of the HttpParamsWrapper child class
    using predefined URL_COMPONENTS iterable if it's available
    """

    def __new__(mcs, name, bases, class_dict):
        url_components = class_dict.get('URL_COMPONENTS')

        if url_components:
            if 'URL_TEMPLATE' in class_dict:
                url_template = class_dict['URL_TEMPLATE']
            else:
                url_template = None
                for base_class in bases:
                    if hasattr(base_class, 'URL_TEMPLATE'):
                        url_template = base_class.URL_TEMPLATE
                        break

            if url_template:
                url_components = [url_template] + list(url_components)

            class_dict['URL_TEMPLATE'] = '/'.join(url_components)

        return super(HttpParamsWrapperMetaclass, mcs).__new__(
            mcs, name, bases, class_dict
        )


@add_metaclass(HttpParamsWrapperMetaclass)
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


class HttpResultWrapper(BaseResultWrapper):

    class Meta:
        container = HttpResultContainer

    @cached_property
    def wrapped(self):
        try:
            return self.Meta.container(
                is_successful=self.is_successful,
                parsed_result=self.parsed_result,
                raw_result=self.raw_result
            )
        except Exception as error:
            raise ResultError(
                message=getattr(error, 'message'),
                base_error=error
            )

    @property
    def is_successful(self):
        return 200 <= self.raw_result.status_code < 300

    @property
    def parsed_result(self):
        raise NotImplementedError()
