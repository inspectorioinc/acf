# Inspectorio base API client

A framework containing template functionality that can be used while
implementing specific API client libraries for any services.

## Minimal client
Minimal API client could look like this:
```python
from base_api_client.actions.http import HttpAction
from base_api_client.clients.base import BaseClient
from base_api_client.resources.base import BaseResource


class SendAnythingAction(HttpAction):

    METHOD = 'POST'
    URL_PATH_TEMPLATE = 'https://httpbin.org/anything'
    RESULT_KEY = 'json'


class AnythingResource(BaseResource):

    ACTIONS = {
        'send': SendAnythingAction
    }


class HttpbinClient(BaseClient):

    RESOURCES = {
        'anything': AnythingResource
    }
```

## Example of the API client usage
You could evaluate the code above or just execute
```python
from example.httpbin_client import HttpbinClient
```
to get the Httpbin client.
After that you'll be able to try
[sending anything](http://httpbin.org/#/Anything/post_anything)!

```python
>>> client = HttpbinClient()
>>> api_result = client.anything.send(foo='bar')
>>> api_result.is_successful
True

>>> api_result.response
<Response [200]>

>>> api_result.result
{'foo': 'bar'}
```
