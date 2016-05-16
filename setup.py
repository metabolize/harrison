# https://coderwall.com/p/qawuyq
# Thanks James.

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''
    print 'warning: pandoc or pypandoc does not seem to be installed; using empty long_description'

from setuptools import setup

setup(
    name='harrison',
    version=__import__('harrison').__version__,
    author='Body Labs',
    author_email='david.smith@bodylabs.com, paul.melnikow@bodylabs.com',
    description='Time a block of code',
    long_description=long_description,
    url='https://github.com/bodylabs/harrison',
    license='MIT',
    packages=[
        'harrison',
        'harrison/util',
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
