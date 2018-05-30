class BaseError(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message


class UnknownResourceError(BaseError):
    pass


class UnknownActionError(BaseError):
    pass
