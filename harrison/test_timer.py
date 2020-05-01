import signal
import pytest
from .timer import TimeoutError, TimeoutTimer

TEST_KWARGS_LIST = [
    {"timeout": 5},
    {"timeout": 5, "desc": "Description"},
    {"timeout": 5, "verbose": True},
    {"timeout": 5, "desc": "Description", "verbose": True},
]

TEST_ARGS_LIST = [[None], [5]]


def expected_timeout(timeout, desc="", verbose=True):
    _ = (desc, verbose)  # for pylint
    if timeout is None:
        return 0
    return timeout


def test_timeout_timer_is_set_correctly_with_args():
    for test_args in TEST_ARGS_LIST:
        with TimeoutTimer(*test_args):
            # turns off timer and returns the previous setting in seconds
            set_number_of_seconds = signal.alarm(0)
        expected_number_of_seconds = expected_timeout(*test_args)
        assert set_number_of_seconds == expected_number_of_seconds


def test_timeout_timer_is_set_correctly_with_kwargs():
    for test_kwargs in TEST_KWARGS_LIST:
        with TimeoutTimer(**test_kwargs):
            # turns off timer and returns the previous setting in seconds
            set_number_of_seconds = signal.alarm(0)
        expected_number_of_seconds = expected_timeout(**test_kwargs)
        assert set_number_of_seconds == expected_number_of_seconds


def test_timeout_raises_timeout_error():
    with pytest.raises(TimeoutError):
        from time import sleep

        with TimeoutTimer(timeout=1, desc="Not enough time"):
            sleep(2)  # Seems appropriate to have at least one real timeout


def test_timeout_does_not_raise_on_clean_exit():
    def will_not_time_out():
        with TimeoutTimer(timeout=1, desc="Plenty of time"):
            return "a_random_return_value"

    assert will_not_time_out() == "a_random_return_value"


def test_two_timeouts_raises():
    with pytest.raises(NotImplementedError):
        with TimeoutTimer(5):
            with TimeoutTimer(3):
                pass
    # And let's make sure that the alarm is cancelled too
    leftover_timeout = signal.alarm(0)
    assert leftover_timeout == 0
