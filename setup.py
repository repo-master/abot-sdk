
import os
from contextlib import suppress

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'abot-sdk'
PACKAGE_VERSION = '0.1.1'
DESCRIPTION = 'SDK for Abot fulfillments using FastAPI'
URL = 'https://github.com/repo-master/abot-api-sdk'
EMAIL = 'repomaster@phaidelta.com'
AUTHOR = 'phAIdelta'
REQUIRES_PYTHON = '>=3.9.0'
LICENSE = ''

REQUIRED = [
    'fastapi'
]


long_desc = DESCRIPTION
BASEPATH = os.path.abspath(os.path.dirname(__file__))
with suppress(FileNotFoundError):
    with open(os.path.join(BASEPATH, 'README.md'), encoding='utf-8') as f:
        long_desc = f.read()

setup(
    name=NAME,
    version=PACKAGE_VERSION,
    description=DESCRIPTION,
    long_description=long_desc,
    packages=find_packages(),
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED
)
