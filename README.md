harrison
========

Time a block of code.

Use as the context expression of a `with` statement:

```pyconsole
>>> from harrison import Timer
>>> with Timer() as t:
>>>     ...
>>> print t.elapsed_time_ms
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
print timer.elapsed_time_s

another_expensive_function(...)
timer.stop()
print timer.elapsed_time_s
```

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
pip install -r requirements_dev.txt
rake lint
```


Contribute
----------

- Issue Tracker: https://github.com/bodylabs/harrison/issues
- Source Code: https://github.com/bodylabs/harrison

Pull requests welcome!


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the two-clause BSD license.
