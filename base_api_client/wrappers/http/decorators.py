def initialize_url_template(cls):
    """
    Decorator that initializes URL_TEMPLATE constant
    of the HttpParamsWrapper child class
    using predefined URL_COMPONENTS list
    """
    if hasattr(cls, 'URL_COMPONENTS'):
        cls.URL_TEMPLATE = '/'.join(cls.URL_COMPONENTS)
    return cls
