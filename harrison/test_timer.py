import unittest
import signal
from harrison.timer import TimeoutTimer
from harrison.timer import TimeoutError

class TestTimeoutTimer(unittest.TestCase):
    TEST_KWARGS_LIST = [
        {'timeout': 5},
        {'timeout': 5, 'desc': 'Description'},
        {'timeout': 5, 'verbose': True},
        {'timeout': 5, 'desc': 'Description', 'verbose': True}
    ]

    TEST_ARGS_LIST = [
        [None],
        [5]
    ]

    @staticmethod
    def expected_timeout(timeout, desc='', verbose=True):
        _ = (desc, verbose) # for pylint
        if timeout is None:
            return 0
        return timeout

    def test_timeout_timer_is_set_correctly_with_args(self):
        for test_args in self.TEST_ARGS_LIST:
            with TimeoutTimer(*test_args):
                # turns off timer and returns the previous setting in seconds
                set_number_of_seconds = signal.alarm(0)
            expected_number_of_seconds = self.expected_timeout(*test_args)
            self.assertEqual(set_number_of_seconds, expected_number_of_seconds)

    def test_timeout_timer_is_set_correctly_with_kwargs(self):
        for test_kwargs in self.TEST_KWARGS_LIST:
            with TimeoutTimer(**test_kwargs):
                # turns off timer and returns the previous setting in seconds
                set_number_of_seconds = signal.alarm(0)
            expected_number_of_seconds = self.expected_timeout(**test_kwargs)
            self.assertEqual(set_number_of_seconds, expected_number_of_seconds)

    def test_timeout_raises_timeout_error(self):
        def will_time_out():
            from time import sleep
            with TimeoutTimer(timeout=1, desc='Not enough time'):
                sleep(2) # Seems appropriate to have at least one real timeout
        self.assertRaises(TimeoutError, will_time_out)

    def test_timeout_does_not_raise_on_clean_exit(self):
        def will_not_time_out():
            with TimeoutTimer(timeout=1, desc='Plenty of time'):
                return 'a_random_return_value'
        self.assertEqual('a_random_return_value', will_not_time_out())

    def test_two_timeouts_raises(self):
        def uses_nested_timeouts():
            with TimeoutTimer(5):
                with TimeoutTimer(3):
                    pass
        self.assertRaises(NotImplementedError, uses_nested_timeouts)
        # And let's make sure that the alarm is cancelled too
        leftover_timeout = signal.alarm(0)
        self.assertEqual(leftover_timeout, 0)
