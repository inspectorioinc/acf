#
# Container classes
#


class BaseContainer(object):
    pass


class BaseParamsContainer(BaseContainer):

    def __init__(self, output_args=None, output_kwargs=None):
        self.args = output_args or tuple()
        self.kwargs = output_kwargs or dict()


class BaseResultContainer(BaseContainer):

    def __init__(self, result=None, raw_result=None):
        self.result = result
        self.raw_result = raw_result


#
# Wrapper classes
#


class BaseWrapper(object):

    class Meta:
        container = None

    def wrapped(self):
        raise NotImplementedError()


class BaseParamsWrapper(BaseWrapper):

    class Meta:
        container = BaseParamsContainer

    def __init__(self, input_args, input_kwargs):
        self.input_args = input_args
        self.input_kwargs = input_kwargs


class BaseResultWrapper(BaseWrapper):

    class Meta:
        container = BaseResultContainer

    def __init__(self, raw_result):
        self.raw_result = raw_result
