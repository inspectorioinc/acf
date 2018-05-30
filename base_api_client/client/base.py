from base_api_client.error.base import UnknownResourceError


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
    """

    RESOURCES = {}

    def __getattr__(self, name):
        resource = self.RESOURCES.get(name)

        if resource is None:
            raise UnknownResourceError(
                'Resource `{name}` is not defined'.format(name=name)
            )

        return resource()
