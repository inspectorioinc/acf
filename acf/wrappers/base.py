class BaseResultContainer(object):

    def __init__(self, result=None, raw_result=None):
        self.result = result
        self.raw_result = raw_result


#
# Wrapper classes
#

class BaseWrapper(object):

    def __init__(self, action, config=None):

        self.action = action
        self.config = config or {}

    @property
    def wrapped(self):
        raise NotImplementedError()


class BaseParamsWrapper(BaseWrapper):

    def __init__(self, action, raw_kwargs, config=None):
        super(BaseParamsWrapper, self).__init__(action=action, config=config)
        self.raw_kwargs = raw_kwargs


class BaseResultWrapper(BaseWrapper):

    class Meta:
        container = BaseResultContainer

    def __init__(self, action, raw_result, config=None):
        super(BaseResultWrapper, self).__init__(action=action, config=config)
        self.raw_result = raw_result
