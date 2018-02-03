# Pytest fixtures etc

import os
import sys
from tempfile import mkdtemp
from shutil import rmtree

import pytest


@pytest.fixture
def tmpdir():
    tmpdir = mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmpdir)
        yield tmpdir
    finally:
        os.chdir(cwd)
        rmtree(tmpdir)


@pytest.fixture
def cwd_on_path():
    sys.path.append('.')
    yield
    sys.path.pop()


@pytest.fixture
def rollback_modules():
    modules = sys.modules.copy()
    yield
    for key, value in list(sys.modules.items()):
        if not key in modules:
            del sys.modules[key]


@pytest.fixture
def restore_python_path():
    path = sys.path[:]
    yield
    sys.path = path[:]


@pytest.fixture
def restore_system_path():
    path = os.environ["PATH"]
    yield
    os.environ["PATH"] = path
