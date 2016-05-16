from harrison import Timer


shared_registry = {}


def aggregate_registry_timers():
    """Returns a list of aggregate timing information for registered timers.

    Each element is a 3-tuple of

        - timer description
        - aggregate elapsed time
        - number of calls

    The list is sorted by the first start time of each aggregate timer.

    """
    import itertools

    timers = sorted(shared_registry.values(), key=lambda t: t.desc)
    aggregate_timers = []
    for k, g in itertools.groupby(timers, key=lambda t: t.desc):
        group = list(g)
        num_calls = len(group)
        total_elapsed_ms = sum(t.elapsed_time_ms for t in group)
        first_start_time = min(t.start_time for t in group)
        # We'll use the first start time as a sort key.
        aggregate_timers.append(
            (first_start_time, (k, total_elapsed_ms, num_calls)))

    aggregate_timers.sort()
    return zip(*aggregate_timers)[1]


def print_registry(logger=None):
    def printfn(m):
        print m

    log = logger.debug if logger else printfn
    for desc, total, num_calls in aggregate_registry_timers():
        log('"{}": {} ms ({})'.format(desc, total, num_calls))


def serialize_registry():
    return [
        {
            'description': desc,
            'total_elapsed_ms': total,
            'num_calls': num_calls,
        }
        for desc, total, num_calls in aggregate_registry_timers()
    ]


class RegisteredTimer(Timer):

    # The stack index of the caller. Using this we can record where the Timer
    # object was istantiated. A subclass may want to override this index if
    # they're adding additional levels of calls, e.g. via a decorator.
    _CALLER_STACK_INDEX = 1

    def __init__(self, desc, verbose=False, registry=None):
        import datetime
        from harrison.util.inspectlib import stack_frame_info

        # Get information about the caller so we can avoid Timer collisions and
        # provide more informative output. Entry 0 is the current frame.
        self._where = stack_frame_info(self._CALLER_STACK_INDEX)

        self._creation_time = datetime.datetime.now()

        self._id = '{}:{}:{}'.format(
            self._where.filename,
            self._where.line_number,
            self._creation_time)

        _registry = registry if registry is not None else shared_registry
        _registry[self._id] = self

        super(RegisteredTimer, self).__init__(desc=desc, verbose=verbose)

    def __repr__(self):
        return '{} {}.{} "{}": {} ms'.format(
            self._id,
            self._where.module_name,
            self._where.function_name,
            self.desc,
            self.elapsed_time_ms)
