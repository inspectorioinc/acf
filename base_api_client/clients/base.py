from cached_property import cached_property

from base_api_client.errors.base import UnknownResourceError


class BaseClient(object):
    """
    Base class for any service API client.

    Perform actions on a specific resource in the form of
    client_instance.<resource>.<action>()

    Attributes
    ----------
    RESOURCES: dict of {str: obj}
        Resources the client knows how to interact with.
        Key: name of the resource.
        Value: specific resource class.
    resource_names: list of str
        List with names of the available resources.
    """

    RESOURCES = {}

    @cached_property
    def resource_names(self):
        return self.RESOURCES.keys()

    def __getattr__(self, name):
        resource = self.RESOURCES.get(name)

        if resource is None:
            raise UnknownResourceError(
                'Resource `{name}` is not defined'.format(name=name)
            )

        return resource()

    def __dir__(self):
        return dir(type(self)) + self.resource_names
