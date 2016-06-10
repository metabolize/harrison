import datetime

class Timer(object):
    """Time a block of code.
    """
    def __init__(self, desc='', verbose=True):
        self.desc = desc
        self.start_time = None
        self.stop_time = None
        self._verbose = verbose

    @property
    def description(self):
        return self.desc

    def start(self):
        self.start_time = datetime.datetime.now()
        self.stop_time = None
        return self.start_time

    def stop(self):
        self.stop_time = datetime.datetime.now()
        return self.stop_time

    @property
    def elapsed_time_s(self):
        if self.start_time is None:
            raise AttributeError(
                'The Timer "{}" has not been started'.format(self.desc))
        if self.stop_time is not None:
            return (self.stop_time - self.start_time).total_seconds()
        else:
            return (datetime.datetime.now() - self.start_time).total_seconds()

    @property
    def elapsed_time_ms(self):
        return 1000. * self.elapsed_time_s

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()
        if self._verbose:
            desc = '{}: '.format(self.description) if self.description else ''
            print '{}{:.2f} ms'.format(desc, self.elapsed_time_ms)

class TimeoutError(Exception):
    pass

class TimeoutTimer(Timer):
    '''
    Same as Timer but takes a timeout argument. It will raise a
    TimeoutError if not exitted within that number of seconds.
    Timer class arguments must be passed using keyword arguments.

    If another TimeoutTimer is already set (or something else that uses alarm signals)
    when the timer is started, a NotImplementedError will be raised.
    '''
    def __init__(self, timeout, **kwargs):
        self.timeout = timeout
        super(TimeoutTimer, self).__init__(**kwargs)

    def raise_timeout(self, signal=None, stack_frame=None, msg=None):
        _ = (signal, stack_frame) # for pylint
        if msg is None:
            msg = self.description + ' - Timed out after {} seconds.'.format(
                self.timeout
            )
        raise TimeoutError(msg)

    def start(self):
        import signal
        if self.timeout:
            old_timeout = signal.alarm(self.timeout)
            if old_timeout:
                raise NotImplementedError('Nested TimeoutTimers are not supported.')
            signal.signal(signal.SIGALRM, self.raise_timeout)
        return super(TimeoutTimer, self).start()

    def stop(self):
        import signal
        if self.timeout:
            signal.alarm(0)
        return super(TimeoutTimer, self).stop()
