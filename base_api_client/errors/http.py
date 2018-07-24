from base_api_client.errors import BaseError


class BaseHttpError(BaseError):

    def __init__(self, message, base_error, *args, **kwargs):
        super(BaseHttpError, self).__init__(message, *args, **kwargs)
        self.base_error = base_error


class ParamsError(BaseHttpError):
    pass


class RequestError(BaseHttpError):
    pass


class ResultError(BaseHttpError):
    def __init__(self, message, base_error, response, *args, **kwargs):
        super(ResultError, self).__init__(message, base_error, *args, **kwargs)
        self.response = response


class ParseResponseError(ResultError):
    pass
