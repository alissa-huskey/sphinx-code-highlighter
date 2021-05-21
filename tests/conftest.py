from subprocess import run

import pytest
from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'

collect_ignore = ['roots']

@pytest.fixture(scope='session')
def rootdir():
    """Sphinx path object to the directory containing sample data files"""
    return path(__file__).parent.abspath() / "roots"


def pytest_addoption(parser):
    parser.addoption(
        "--noslow", action="store_true", default=False, help="skip slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--noslow"):
        return

    # --noslow given in cli: skip slow tests
    skip_slow = pytest.mark.skip(reason="--noslow")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
