class BaseProtocol(object):
    """
    Base class for resources communication protocols.
    """

    def execute(self, *args, **kwargs):
        raise NotImplementedError()
