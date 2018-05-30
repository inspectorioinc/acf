from base_api_client.error.base import UnknownActionError


class BaseResource(object):
    """
    Base class for any resource provided by a service.

    Perform actions on a specific resource in the form of
    resource_instance.<action>()

    Attributes
    ----------
    ACTIONS: dict of {str: obj}
        Actions allowed to perform on a resource.
        Key: name of the action.
        Value: specific action class.
    """

    ACTIONS = {}

    def __getattr__(self, name):
        action = self.ACTIONS.get(name)

        if action is None:
            raise UnknownActionError(
                'Action `{name}` is not defined'.format(name=name)
            )

        return action()
