class BaseError(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message

    def __str__(self):
        return self.message


class UnknownResourceError(BaseError):
    pass


class UnknownActionError(BaseError):
    pass
