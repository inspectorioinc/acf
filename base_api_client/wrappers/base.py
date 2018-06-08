#
# Container classes
#


class BaseContainer(object):
    pass


class BaseParamsContainer(BaseContainer):

    def __init__(self, prepared_args=None, prepared_kwargs=None):
        self.args = prepared_args or tuple()
        self.kwargs = prepared_kwargs or dict()


class BaseResultContainer(BaseContainer):

    def __init__(self, parsed_result=None, raw_result=None):
        self.result = parsed_result
        self.raw_result = raw_result


#
# Wrapper classes
#


class BaseWrapper(object):

    class Meta:
        container = None

    def __init__(self, config=None):
        self.config = config or {}

    @property
    def wrapped(self):
        raise NotImplementedError()


class BaseParamsWrapper(BaseWrapper):

    class Meta:
        container = BaseParamsContainer

    def __init__(self, config=None, *args, **kwargs):
        super(BaseParamsWrapper, self).__init__(config=config)
        self.raw_args = args
        self.raw_kwargs = kwargs


class BaseResultWrapper(BaseWrapper):

    class Meta:
        container = BaseResultContainer

    def __init__(self, raw_result, config=None):
        super(BaseResultWrapper, self).__init__(config=config)
        self.raw_result = raw_result
