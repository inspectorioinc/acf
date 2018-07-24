class NotSet(object):

    # Python 3.x
    def __bool__(self):
        return False

    # Python 2.x
    __nonzero__ = __bool__

    def __str__(self):
        return self.__class__.__name__


NOT_SET = NotSet()


def defined(value):
    return value is not NOT_SET
