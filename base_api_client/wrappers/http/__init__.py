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

    def filter_raw_kwargs(self, include=UNDEFINED, exclude=UNDEFINED):
        check = None

        if defined(include):
            def check(key):
                return key in include
        elif defined(exclude):
            def check(key):
                return key not in exclude

        if check:
            return {
                key: value
                for key, value in self.raw_kwargs.items()
                if check(key)
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
            return self.filter_raw_kwargs(include=url_query_params)

        if self.action.PAYLOAD_REQUIRED:
            if 'data' in self.raw_kwargs:
                return self.filter_raw_kwargs(
                    exclude={'data'}.union(self.action.DEFINED_PARAMS or ())
                )
            if defined(self.action.PAYLOAD_PARAMS):
                return self.filter_raw_kwargs(
                    exclude=self.action.DEFINED_PARAMS
                )

            # We should not return query string params if payload is
            # required but the 'data' is not in kwargs and
            # URL_QUERY_PARAMS and PAYLOAD_PARAMS were not defined,
            # because all the kwargs that are not in DEFINED_PARAMS
            # will be used to build the payload by default.

        else:
            return self.filter_raw_kwargs(exclude=self.action.DEFINED_PARAMS)

    def build_json(self):
        """Returns the payload if it's required"""

        if self.action.PAYLOAD_REQUIRED:
            if 'data' in self.raw_kwargs:
                return self.raw_kwargs['data']
            return self.filter_raw_kwargs(
                include=self.action.PAYLOAD_PARAMS,
                exclude=self.action.DEFINED_PARAMS
            )

    def build_headers(self):
        """
        Returns headers if HEADERS_PARAMS constant
        is defined for the action
        """

        headers_params = self.action.HEADERS_PARAMS
        if defined(headers_params):
            return self.filter_raw_kwargs(include=headers_params)

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
                result = self.result
            except ValueError as error:
                if self.response_status_is_successful:
                    raise ParseResponseError(
                        'Can not parse content of the API response',
                        base_error=error,
                        response=self.response
                    )
                else:
                    is_successful = False
                    result = None

            return self.Meta.container(
                is_successful=is_successful,
                result=result,
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
            return self.response.json()

    @property
    def result(self):
        result_key = self.action.RESULT_KEY
        if result_key:
            return self.parsed_result.get(result_key)
        return self.parsed_result
