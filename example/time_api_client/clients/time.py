from base_api_client.clients.base import BaseClient

from example.time_api_client.resources.time import TimeResource


class TimeClient(BaseClient):

    RESOURCES = {
        'time': TimeResource
    }
