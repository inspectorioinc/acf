from .base import HttpbinAction


class SendAnythingAction(HttpbinAction):

    METHOD = 'POST'
    URL_COMPONENTS = ('anything',)
    RESULT_KEY = 'json'
