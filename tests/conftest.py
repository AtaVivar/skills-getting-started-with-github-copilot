from copy import deepcopy

from fastapi.testclient import TestClient
import pytest

from src import app as app_module
from src.app import app


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_activities))


@pytest.fixture
def client():
    return TestClient(app)
