from ..wrappers.status import UpdateStatusResultWrapper
from .base import HttpbinAction


class UpdateStatusAction(HttpbinAction):

    METHOD = 'PUT'
    URL_COMPONENTS = ('status', '{status}')

    RESULT_WRAPPER = UpdateStatusResultWrapper
