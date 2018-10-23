from acf.wrappers.http import HttpResultWrapper


class UpdateStatusResultWrapper(HttpResultWrapper):

    @property
    def parsed_result(self):
        return self.response.status_code
