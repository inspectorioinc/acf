# API Client Framework

The framework for building well structured API client libraries in Python.

## Minimal API client implementation

The simplest implementation of the API client based on ACF could look like this:

```python
from acf.actions.http import HttpAction
from acf.clients.base import BaseClient
from acf.resources.base import BaseResource


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

## Example of the minimal API client usage

You can evaluate the code above or just execute the following line for importing the Httpbin client.

```python
from example.httpbin_client import HttpbinClient
```

After that you'll be able to [send any test data](http://httpbin.org/#/Anything/post_anything)!

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
