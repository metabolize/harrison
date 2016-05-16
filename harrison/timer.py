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
