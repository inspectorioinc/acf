class Undefined(object):

    # Python 3.x
    def __bool__(self):
        return False

    # Python 2.x
    __nonzero__ = __bool__

    def __str__(self):
        return self.__class__.__name__


UNDEFINED = Undefined()


def defined(value):
    return value is not UNDEFINED
