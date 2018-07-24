from .base import HttpbinAction


class GetHeadersAction(HttpbinAction):

    METHOD = 'GET'
    URL_COMPONENTS = ['headers']
    RESULT_KEY = 'headers'


class GetIPAction(HttpbinAction):

    METHOD = 'GET'
    URL_COMPONENTS = ['ip']
    RESULT_KEY = 'origin'


class GetUserAgentAction(HttpbinAction):

    METHOD = 'GET'
    URL_COMPONENTS = ['user-agent']
    RESULT_KEY = 'user-agent'
