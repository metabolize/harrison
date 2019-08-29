import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='harrison',
    version=__import__('harrison').__version__,
    author='Body Labs, Metabolize',
    author_email='github@paulmelnikow.com',
    description='Time a block of code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/metabolize/harrison',
    license='MIT',
    packages=[
        'harrison',
        'harrison/util',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
