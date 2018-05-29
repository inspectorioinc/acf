class BaseClient(object):

    RESOURCES = {}

    def __getattr__(self, item):
        print(item)
        try:
            action_name, resource_name = item.split('_')[:2]
        except ValueError:
            raise AttributeError

        resource = self.RESOURCES.get(resource_name)()
        return getattr(resource, action_name, None)
