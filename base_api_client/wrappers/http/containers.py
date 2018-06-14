from base_api_client.wrappers.base import BaseResultContainer


class HttpResultContainer(BaseResultContainer):

    def __init__(
        self, is_successful=True, parsed_result=None, raw_result=None
    ):
        super(HttpResultContainer, self).__init__(
            parsed_result=parsed_result, raw_result=raw_result
        )
        self.is_successful = is_successful
