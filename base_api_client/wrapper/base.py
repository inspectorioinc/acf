class BaseWrapper(object):

    def wrap(self, *args, **kwargs):
        raise NotImplementedError()


class BaseParamsWrapper(BaseWrapper):
    pass


class BaseResultWrapper(BaseWrapper):

    def __init__(self, raw_result):
        self.raw_result = raw_result
