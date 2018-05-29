class BaseProtocol(object):

    def execute(self, *args, **kwargs):
        raise NotImplementedError()
