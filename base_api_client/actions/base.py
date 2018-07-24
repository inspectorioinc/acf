from base_api_client.protocols.base import BaseProtocol
from base_api_client.wrappers.base import (
    BaseParamsWrapper, BaseResultWrapper
)


class BaseAction(object):
    """
    Base class for an action that can be performed on a resource.

    Attributes
    ----------
    PROTOCOL: obj
        Protocol class that specifies rules of communication with the resource.
    PARAMS_WRAPPER: obj
        Wrapper class that handles request parameters.
    RESULT_WRAPPER: obj
        Wrapper class that handles response from the resource.
    """

    PROTOCOL = BaseProtocol
    PARAMS_WRAPPER = BaseParamsWrapper
    RESULT_WRAPPER = BaseResultWrapper

    def __init__(self, config=None):
        self.config = config or {}

    def __call__(self, **kwargs):
        wrapped_kwargs = self.PARAMS_WRAPPER(
            action=self, config=self.config, raw_kwargs=kwargs
        ).wrapped
        result = self.PROTOCOL().execute(**wrapped_kwargs)
        return self.RESULT_WRAPPER(
            action=self, config=self.config, raw_result=result
        ).wrapped
