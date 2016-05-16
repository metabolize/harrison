def profile(message=None, verbose=False):
    """Decorator for profiling a function.

    TODO: Support `@profile` syntax (without parens). This would involve
    inspecting the args. In this case `profile` would receive a single
    argument, which is the function to be decorated.

    """
    import functools
    from harrison.registered_timer import RegisteredTimer

    # Adjust the call stack index for RegisteredTimer so the call is Timer use
    # is properly attributed.
    class DecoratorTimer(RegisteredTimer):
        _CALLER_STACK_INDEX = 2

    def wrapper(fn):
        desc = message or fn.__name__

        @functools.wraps(fn)
        def wrapped_fn(*args, **kwargs):
            with DecoratorTimer(desc=desc, verbose=verbose):
                return fn(*args, **kwargs)
        return wrapped_fn

    return wrapper
