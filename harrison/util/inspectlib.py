from collections import namedtuple

_Where = namedtuple(
    'Where',
    ['filename', 'line_number', 'module_name', 'function_name']
)

class Where(_Where):
    @property
    def pretty(self):
        '''
        Return a string like '/foo/bar.py:230 in foo.bar.my_func'.
        '''
        return '{}:{} in {}.{}'.format(
            self.filename,
            self.line_number,
            self.module_name,
            self.function_name)

def stack_frame_info(stacklevel):
    '''
    Return a named tuple with information about the given stack frame:
        - filename
        - line_number
        - module_name
        - function_name

    stacklevel: How far up the stack to look. 1 means the immediate caller, 2
      its caller, and so on.
    '''
    import inspect

    if stacklevel < 1:
        raise ValueError('A stacklevel less than 1 is pointless')

    frame, filename, line_number, function_name, _, _ = inspect.stack()[stacklevel]
    module_name = inspect.getmodule(frame).__name__

    return Where(
        filename=filename,
        line_number=line_number,
        module_name=module_name,
        function_name=function_name
    )
