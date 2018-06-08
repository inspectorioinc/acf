# Inspectorio base API client

A framework containing template functionality that can be used while implementing specific API client libraries for the Inspectorio services.

## Example of the API client usage

```python
>>> from example.time_api_client.clients.time import TimeClient

>>> time_api_client = TimeClient(
        config={'username': 'test', 'password': 'test'}
    )
>>> wrapped_result = time_api_client.time.get_now()
>>> current_time = wrapped_result.result

>>> print(current_time)
2018-06-07T13:25Z
```
