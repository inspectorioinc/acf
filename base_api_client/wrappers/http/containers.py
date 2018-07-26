from base_api_client.wrappers.base import BaseResultContainer


class HttpResultContainer(BaseResultContainer):

    def __init__(
        self, is_successful=True, result=None, raw_result=None
    ):
        super(HttpResultContainer, self).__init__(
            result=result, raw_result=raw_result
        )
        self.is_successful = is_successful

    @property
    def response(self):
        return self.raw_result
