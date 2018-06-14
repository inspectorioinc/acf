def initialize_url_template(cls):
    if hasattr(cls, 'URL_COMPONENTS'):
        cls.URL_TEMPLATE = '/'.join(cls.URL_COMPONENTS)
    return cls
