import pytest

from base_api_client.wrapper.base import (
    BaseParamsContainer, BaseParamsWrapper,
    BaseResultContainer, BaseResultWrapper,
    BaseWrapper
)


def test_base_wrapper():
    with pytest.raises(NotImplementedError):
        BaseWrapper().wrapped()


def test_base_params_wrapper():
    args = (42,)
    kwargs = {'foo': 'bar'}
    wrapper = BaseParamsWrapper(args, kwargs)

    assert wrapper.input_args == args
    assert wrapper.input_kwargs == kwargs


def test_base_result_wrapper():
    result = 'foobar'
    wrapper = BaseResultWrapper(result)

    assert wrapper.raw_result == result


def test_base_params_container_init():
    args = (42,)
    kwargs = {'foo': 'bar'}
    container = BaseParamsContainer(output_args=args, output_kwargs=kwargs)

    assert container.args == args and container.kwargs == kwargs

    # test empty output arguments
    container = BaseParamsContainer()

    assert container.args == tuple() and container.kwargs == dict()


def test_base_result_container_init():
    result = 'foobar'
    raw_result = 'foobar\n'
    container = BaseResultContainer(result=result, raw_result=raw_result)

    assert container.result == result and container.raw_result == raw_result
