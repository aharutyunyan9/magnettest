import pytest


@pytest.fixture
def page(page):
    yield page
    page.wait_for_timeout(3000)  # 3 sec pause before browser closes
