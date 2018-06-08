import pytest

from base_api_client.wrappers.base import (
    BaseParamsContainer, BaseParamsWrapper,
    BaseResultContainer, BaseResultWrapper,
    BaseWrapper
)


def test_base_wrapper():
    with pytest.raises(NotImplementedError):
        BaseWrapper().wrapped()


def test_base_params_wrapper_init():
    kwargs = {'foo': 'bar'}
    wrapper = BaseParamsWrapper(config={}, **kwargs)

    assert wrapper.raw_kwargs == kwargs


def test_base_result_wrapper_init():
    result = 'foobar'
    wrapper = BaseResultWrapper(config={}, raw_result=result)

    assert wrapper.raw_result == result


def test_base_params_container_init():
    kwargs = {'foo': 'bar'}
    container = BaseParamsContainer(prepared_kwargs=kwargs)

    assert container.kwargs == kwargs

    # test empty output arguments
    container = BaseParamsContainer()

    assert container.kwargs == dict()


def test_base_result_container_init():
    result = 'foobar'
    raw_result = 'foobar\n'
    container = BaseResultContainer(
        parsed_result=result,
        raw_result=raw_result
    )

    assert container.result == result and container.raw_result == raw_result
