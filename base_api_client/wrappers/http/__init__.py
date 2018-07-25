from cached_property import cached_property

from base_api_client.constants import defined, UNDEFINED
from base_api_client.errors.http import (
    ParamsError,
    ParseResponseError,
    ResultError
)
from base_api_client.wrappers.base import BaseParamsWrapper, BaseResultWrapper
from base_api_client.wrappers.http.containers import HttpResultContainer

__all__ = ['HttpParamsWrapper', 'HttpResultWrapper']


class HttpParamsWrapper(BaseParamsWrapper):

    REQUEST_KWARGS = [
        'method', 'url', 'params',
        'data', 'headers', 'cookies',
        'files', 'auth', 'timeout', 'json'
    ]

    @cached_property
    def wrapped(self):
        try:
            return self.build_kwargs()
        except ParamsError as error:
            raise error
        except Exception as error:
            raise ParamsError(
                message=getattr(error, 'message', None) or str(error),
                base_error=error
            )

    def build_kwargs(self):
        default = self.build_empty
        return {
            kwarg: getattr(
                self, 'build_{kwarg}'.format(kwarg=kwarg), default
            )()
            for kwarg in self.REQUEST_KWARGS
        }

    def get_data_from_raw_kwargs(self, include=UNDEFINED, exclude=UNDEFINED):
        if defined(include):
            return {
                key: value
                for key, value in self.raw_kwargs.items()
                if key in include
            }

        if exclude:
            exclude.update(self.action.DEFINED_PARAMS or ())
        else:
            exclude = self.action.DEFINED_PARAMS

        if defined(exclude):
            return {
                key: value
                for key, value in self.raw_kwargs.items()
                if key not in exclude
            }

        return self.raw_kwargs

    def build_method(self):
        return self.action.METHOD

    def build_url(self):
        try:
            return self.action.URL_PATH_TEMPLATE.format(**self.raw_kwargs)
        except KeyError as error_key:
            raise ParamsError(
                message='Parameter {} is required'.format(error_key),
                base_error=error_key
            )

    def build_params(self):
        """Returns query string params"""

        url_query_params = self.action.URL_QUERY_PARAMS
        if defined(url_query_params):
            return self.get_data_from_raw_kwargs(include=url_query_params)

        if (not self.action.PAYLOAD_REQUIRED or
                defined(self.action.PAYLOAD_PARAMS)):
            return self.get_data_from_raw_kwargs()

        if 'data' in self.raw_kwargs:
            return self.get_data_from_raw_kwargs(exclude={'data'})

    def build_json(self):
        """Returns the payload if it's required"""

        if self.action.PAYLOAD_REQUIRED:
            if 'data' in self.raw_kwargs:
                return self.raw_kwargs['data']
            return self.get_data_from_raw_kwargs(
                include=self.action.PAYLOAD_PARAMS
            )

    def build_headers(self):
        """
        Returns headers if HEADERS_PARAMS constant
        is defined for the action
        """

        headers_params = self.action.HEADERS_PARAMS
        if defined(headers_params):
            return self.get_data_from_raw_kwargs(include=headers_params)

    def build_empty(self):
        pass


class HttpResultWrapper(BaseResultWrapper):

    class Meta:
        container = HttpResultContainer

    @cached_property
    def wrapped(self):
        try:
            try:
                is_successful = self.is_successful
                parsed_result = self.parsed_result
            except ValueError as error:
                if self.response_status_is_successful:
                    raise ParseResponseError(
                        'Can not parse content of the API response',
                        base_error=error,
                        response=self.response
                    )
                else:
                    is_successful = False
                    parsed_result = None

            return self.Meta.container(
                is_successful=is_successful,
                parsed_result=parsed_result,
                raw_result=self.raw_result
            )
        except ParseResponseError as error:
            raise error
        except Exception as error:
            raise ResultError(
                message=getattr(error, 'message', None) or str(error),
                base_error=error,
                response=self.response
            )

    @property
    def response(self):
        return self.raw_result

    @property
    def response_status_is_successful(self):
        return 200 <= self.response.status_code < 300

    is_successful = response_status_is_successful

    @property
    def parsed_result(self):
        if self.response.status_code != 204:
            result = self.response.json()
            result_key = getattr(self.action, 'RESULT_KEY', None)
            if result_key is not None:
                return result.get(result_key)
            return result
