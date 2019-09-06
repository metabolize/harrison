import re
import pytest
from .inspectlib import stack_frame_info


def stack_frame_test_func(stacklevel):
    return stack_frame_info(stacklevel)


def test_stack_frame_info():
    there = stack_frame_test_func(1)
    # Argh, might be .pyc, or might be .py.
    print(there.filename)
    assert re.search("test_inspectlib.pyc?", there.filename)
    assert there.module_name == __name__
    assert there.function_name == "stack_frame_test_func"

    here = stack_frame_test_func(2)
    # Argh, might be .pyc, or might be .py.
    assert re.search("test_inspectlib.pyc?", here.filename)
    assert here.module_name == __name__
    assert here.function_name == "test_stack_frame_info"

    assert there.line_number < here.line_number

    assert re.search(
        r"test_inspectlib.py:\d+ in \S*test_inspectlib.test_stack_frame_info$",
        here.pretty,
    )

    with pytest.raises(ValueError):
        stack_frame_test_func(0)


def test_stack_frame_info_works_when_module_can_not_be_identified(mocker):
    mock_getmodule = mocker.patch("inspect.getmodule")
    mock_getmodule.return_value = None
    stack_frame_test_func(1)
