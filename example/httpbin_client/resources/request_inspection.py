from ..actions.request_inspection import (
    GetHeadersAction, GetIPAction, GetUserAgentAction
)
from .base import HttpbinResource


class RequestInspectionResource(HttpbinResource):

    ACTIONS = {
        'get_headers': GetHeadersAction,
        'get_ip': GetIPAction,
        'get_user_agent': GetUserAgentAction,
    }
