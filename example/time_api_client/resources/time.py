from base_api_client.resources.base import BaseResource

from example.time_api_client.actions.time import TimeAction


class TimeResource(BaseResource):

    ACTIONS = {
        'get_now': TimeAction
    }
