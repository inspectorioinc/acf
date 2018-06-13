class JsonPayloadWrapperMixin(object):

    def build_json(self):
        return self.raw_kwargs.get('data') or {
            key: value
            for key, value in self.raw_kwargs.items()
            if key not in self.URL_PARAMS
        }


class QueryParamsWrapperMixin(object):

    METHOD = 'GET'

    def build_params(self):
        return {
            key: value
            for key, value in self.raw_kwargs.items()
            if key not in self.URL_PARAMS
        }
