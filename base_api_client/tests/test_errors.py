import six
from faker import Faker

from base_api_client.errors import BaseError


class TestErrors(object):

    def test_base_error(self):
        faker = Faker()
        message = faker.sentence()
        error = BaseError(message)
        assert six.text_type(error) == message

    def test_base_error_non_ascii(self):
        faker = Faker('ru')
        message = faker.sentence()
        error = BaseError(message)
        assert six.text_type(error) == message
