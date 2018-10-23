from acf.clients.base import BaseClient

from ..resources.anything import AnythingResource
from ..resources.request_inspection import RequestInspectionResource
from ..resources.status import StatusResource


class HttpbinClient(BaseClient):

    RESOURCES = {
        'anything': AnythingResource,
        'request_inspection': RequestInspectionResource,
        'status': StatusResource,
    }
