import pytest

from base_api_client.wrappers.base import (
    BaseParamsWrapper,
    BaseResultContainer,
    BaseResultWrapper,
    BaseWrapper,
)


def test_base_wrapper():
    with pytest.raises(NotImplementedError):
        BaseWrapper(action=None).wrapped


def test_base_params_wrapper_init():
    action = object()
    kwargs = {'foo': 'bar'}
    wrapper = BaseParamsWrapper(
        action=action, raw_kwargs=kwargs, config={}
    )

    assert wrapper.action is action
    assert wrapper.raw_kwargs == kwargs


def test_base_result_wrapper_init():
    action = object()
    result = 'foobar'
    wrapper = BaseResultWrapper(action=action, raw_result=result, config={})

    assert wrapper.action is action
    assert wrapper.raw_result == result


def test_base_result_container_init():
    result = 'foobar'
    raw_result = 'foobar\n'
    container = BaseResultContainer(
        result=result,
        raw_result=raw_result
    )

    assert container.result == result and container.raw_result == raw_result
