harrison
========

Time a block of code.

[![version](https://img.shields.io/pypi/v/harrison?style=flat-square)][pypi]
[![python version](https://img.shields.io/pypi/pyversions/harrison?style=flat-square)][pypi]
[![license](https://img.shields.io/pypi/l/harrison?style=flat-square)][pypi]
[![build](https://img.shields.io/circleci/project/github/metabolize/harrison/master?style=flat-square)][build]
[![code style](https://img.shields.io/badge/code%20style-black-black?style=flat-square)][black]

[pypi]: https://pypi.org/project/harrison/
[build]: https://circleci.com/gh/metabolize/harrison/tree/master
[black]: https://black.readthedocs.io/en/stable/

Use as the context expression of a `with` statement:

```pyconsole
>>> from harrison import Timer
>>> with Timer() as t:
>>>     ...
>>> print(t.elapsed_time_ms)
12345
```

When a description string is passed on initialization, the elapsed time will
be printed on completion, keyed by this description.

```pyconsole
>>> with Timer('My expensive block of code'):
>>>     ...
My expensive block of code: 12345 ms
```

You can also start and stop a Timer explicitly:

```py
timer = Timer()
timer.start()

some_expensive_function(...)
print(timer.elapsed_time_s)

another_expensive_function(...)
timer.stop()
print(timer.elapsed_time_s)
```

You can also time each execution of a function using a decorator:

```py
from harrison import profile

@profile('Describes the function')
def some_function():
    pass

# Without args, the function name (e.g. 'some_function') will be used
# as the description.
@profile()
def another_function():
    pass
```

You can also use `RegisteredTimer`, which groups together a bunch of named
timers, provides utilities for serializing their times, and an optional global
timer registry.

Named after John Harrison, the English carpenter and clockmaker who
invented the [marine chronometer][].

[John Harrison]: https://en.wikipedia.org/wiki/John_Harrison
[marine chronometer]: https://en.wikipedia.org/wiki/Marine_chronometer


Similar libraries
-----------------

This is similar to the library [contexttimer][], but that library is licensed
under the GPLv3 which is more restrictive than two-clause BSD license used
here.

[contexttimer]: https://github.com/brouberol/contexttimer


Development
-----------

```sh
./dev.py init
./dev.py test
```


Contribute
----------

- Issue Tracker: https://github.com/metabolize/harrison/issues
- Source Code: https://github.com/metabolize/harrison

Pull requests welcome!


Support
-------

If you are having issues, please let us know.


Acknowledgements
----------------

This project was packaged by [Paul Melnikow][] while at [Body Labs][]. Thanks
to Body Labs for the repository transfer.


[paul melnikow]: https://github.com/paulmelnikow
[body labs]: https://github.com/bodylabs


License
-------

The project is licensed under the two-clause BSD license.
