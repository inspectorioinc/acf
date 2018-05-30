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

    def __call__(self, *args, **kwargs):
        wrapped_params = self.PARAMS_WRAPPER(args, kwargs).wrapped
        result = self.PROTOCOL().execute(
            *wrapped_params.args, **wrapped_params.kwargs
        )
        return self.RESULT_WRAPPER(result).wrapped
