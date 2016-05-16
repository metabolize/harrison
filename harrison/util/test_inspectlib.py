import unittest
from harrison.util.inspectlib import stack_frame_info

def stack_frame_test_func(stacklevel):
    return stack_frame_info(stacklevel)

class TestStackFrame(unittest.TestCase):

    def test_stack_frame_info(self):
        there = stack_frame_test_func(1)
        # Argh, might be .pyc, or might be .py.
        self.assertRegexpMatches(there.filename, 'test_inspectlib.pyc?')
        self.assertEqual(there.module_name, __name__)
        self.assertEqual(there.function_name, 'stack_frame_test_func')

        here = stack_frame_test_func(2)
        # Argh, might be .pyc, or might be .py.
        self.assertRegexpMatches(here.filename, 'test_inspectlib.pyc?')
        self.assertEqual(here.module_name, __name__)
        self.assertEqual(here.function_name, 'test_stack_frame_info')

        self.assertLess(there.line_number, here.line_number)

        self.assertRegexpMatches(
            here.pretty,
            r'test_inspectlib.py:\d+ in \S*test_inspectlib.test_stack_frame_info$'
        )

        with self.assertRaises(ValueError):
            stack_frame_test_func(0)
