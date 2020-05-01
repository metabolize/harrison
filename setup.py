from setuptools import setup

version_info = {}
exec(open("harrison/package_version.py").read(), version_info)

setup(
    name="harrison",
    version=version_info["__version__"],
    author="Body Labs, Metabolize",
    author_email="github@paulmelnikow.com",
    description="Time a block of code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/metabolize/harrison",
    license="MIT",
    packages=["harrison", "harrison/util"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
