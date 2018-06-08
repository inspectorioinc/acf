from base_api_client.actions.base import BaseAction
from base_api_client.protocols.http import HttpProtocol

from example.time_api_client.wrappers.time import (
    TimeParamsWrapper, TimeResultWrapper
)


class TimeAction(BaseAction):
    PROTOCOL = HttpProtocol
    PARAMS_WRAPPER = TimeParamsWrapper
    RESULT_WRAPPER = TimeResultWrapper
