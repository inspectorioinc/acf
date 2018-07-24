from ..actions.anything import SendAnythingAction
from .base import HttpbinResource


class AnythingResource(HttpbinResource):

    ACTIONS = {
        'send': SendAnythingAction
    }
