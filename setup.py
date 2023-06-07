
import os

from setuptools import find_packages, setup

from abot_sdk.__version__ import __version__ as VERSION

# Package meta-data.
NAME = 'abot-sdk'
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
try:
    BASEPATH = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(BASEPATH, 'README.md'), encoding='utf-8') as f:
        long_desc = f.read()
except FileNotFoundError:
    pass

setup(
    name=NAME,
    version="0.1.0",
    description=DESCRIPTION,
    long_description=long_desc,
    packages=find_packages(),
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED
)
