import re

from six import add_metaclass

from base_api_client.constants import NOT_SET, defined
from base_api_client.errors import ImplementationError
from base_api_client.protocols.http import HttpProtocol
from base_api_client.wrappers.http import HttpParamsWrapper, HttpResultWrapper

from .base import BaseAction


PARAM_REGEX = re.compile('{(?P<param>.*?)}')
PARAM_CONSTANT_NAMES = (
    'URL_PATH_PARAMS',
    'URL_QUERY_PARAMS',
    'PAYLOAD_PARAMS',
    'HEADERS_PARAMS',
)


class HttpActionMetaclass(type):
    """HttpActionMetaclass

    This metaclass is used for updating URL_PATH_TEMPLATE constant
    of the HttpAction child class using predefined URL_COMPONENTS
    iterable if it's available and initializing params constants.
    """

    def __new__(mcs, name, bases, class_dict):
        mcs.init_url_path_template(bases, class_dict)
        mcs.init_url_path_params(class_dict)
        mcs.init_defined_params(bases, class_dict)
        mcs.init_payload_required(bases, class_dict)

        return super(HttpActionMetaclass, mcs).__new__(
            mcs, name, bases, class_dict
        )

    @staticmethod
    def get_value(key, bases, class_dict):
        if key in class_dict:
            return class_dict[key]

        for base_class in bases:
            if hasattr(base_class, key):
                return getattr(base_class, key)

    @classmethod
    def init_url_path_template(mcs, bases, class_dict):
        url_components = class_dict.get('URL_COMPONENTS')
        use_trailing_slash = mcs.get_value('USE_TRAILING_SLASH',
                                           bases, class_dict)
        url_path_template = mcs.get_value('URL_PATH_TEMPLATE',
                                          bases, class_dict)

        if url_components:
            if url_path_template:
                url_path_template = url_path_template.rstrip('/')
                url_components = [url_path_template] + list(url_components)

            url_path_template = '/'.join(url_components)

            if use_trailing_slash and not url_path_template.endswith('/'):
                url_path_template += '/'

            class_dict['URL_PATH_TEMPLATE'] = url_path_template
        elif (use_trailing_slash and url_path_template
              and not url_path_template.endswith('/')):
            class_dict['URL_PATH_TEMPLATE'] = url_path_template + '/'

    @classmethod
    def init_url_path_params(mcs, class_dict):
        url_path_template = class_dict.get('URL_PATH_TEMPLATE')

        if url_path_template:
            class_dict['URL_PATH_PARAMS'] = params = set()
            for match in PARAM_REGEX.finditer(url_path_template):
                param = match.group('param')
                if not param:
                    raise ImplementationError(
                        'Unnamed params are not supported'
                    )
                params.add(param)

    @classmethod
    def init_defined_params(mcs, bases, class_dict):
        defined_params = set()
        for key in PARAM_CONSTANT_NAMES:
            params = mcs.get_value(key, bases, class_dict)
            if params:
                defined_params.update(params)

        if not defined_params:
            defined_params = NOT_SET
        base_defined_params = mcs.get_value(
            'DEFINED_PARAMS', bases, class_dict
        )
        if defined_params != base_defined_params:
            class_dict['DEFINED_PARAMS'] = defined_params

    @classmethod
    def init_payload_required(mcs, bases, class_dict):
        payload_required = mcs.get_value('PAYLOAD_REQUIRED', bases, class_dict)
        if not defined(payload_required):
            method = mcs.get_value('METHOD', bases, class_dict)
            if defined(method):
                class_dict['PAYLOAD_REQUIRED'] = method.upper() in {
                    'POST', 'PUT', 'PATCH'
                }


@add_metaclass(HttpActionMetaclass)
class HttpAction(BaseAction):

    PROTOCOL = HttpProtocol
    PARAMS_WRAPPER = HttpParamsWrapper
    RESULT_WRAPPER = HttpResultWrapper

    METHOD = NOT_SET
    URL_PATH_TEMPLATE = NOT_SET
    URL_COMPONENTS = NOT_SET
    USE_TRAILING_SLASH = NOT_SET
    PAYLOAD_REQUIRED = NOT_SET

    URL_QUERY_PARAMS = NOT_SET
    PAYLOAD_PARAMS = NOT_SET
    HEADERS_PARAMS = NOT_SET

    # There is no sense in overriding the following constants
    # because they will be set by the metaclass
    URL_PATH_PARAMS = None
    DEFINED_PARAMS = None
