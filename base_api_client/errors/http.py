from base_api_client.errors.base import BaseError


class RequestError(BaseError):

    def __init__(self, message, base_error, *args, **kwargs):
        super(RequestError, self).__init__(message, *args, **kwargs)
        self.base_error = base_error
