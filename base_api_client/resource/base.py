class BaseResource(object):

    ACTIONS = {}

    def __getattr__(self, item):
        return self.ACTIONS.get(item)()
