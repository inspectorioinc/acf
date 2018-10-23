import six


@six.python_2_unicode_compatible
class BaseError(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message

    def __str__(self):
        return self.message


class ImplementationError(BaseError):
    pass


class UnknownResourceError(BaseError):
    pass


class UnknownActionError(BaseError):
    pass
