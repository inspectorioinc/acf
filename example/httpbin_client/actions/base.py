from base_api_client.actions.http import HttpAction


class HttpbinAction(HttpAction):

    URL_PATH_TEMPLATE = 'https://httpbin.org'
