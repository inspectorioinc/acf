from ..actions.status import UpdateStatusAction
from .base import HttpbinResource


class StatusResource(HttpbinResource):

    ACTIONS = {
        'update': UpdateStatusAction
    }
