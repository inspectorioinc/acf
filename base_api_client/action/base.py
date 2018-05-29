from base_api_client.protocol.base import BaseProtocol
from base_api_client.wrapper.base import (
    BaseParamsWrapper, BaseResultWrapper
)


class BaseAction(object):

    PROTOCOL = BaseProtocol
    PARAMS_WRAPPER = BaseParamsWrapper
    RESULT_WRAPPER = BaseResultWrapper

    def __call__(self, *args, **kwargs):
        args, kwargs = self.PARAMS_WRAPPER().wrap(*args, **kwargs)
        result = self.PROTOCOL().execute(*args, **kwargs)
        return self.RESULT_WRAPPER(result).wrap()
