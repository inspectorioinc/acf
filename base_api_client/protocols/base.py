class BaseProtocol(object):
    """
    Base class for resources communication protocols.
    """

    def execute(self, **kwargs):
        raise NotImplementedError()
