import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


@pytest.fixture
def burger():
    """Пустой бургер."""
    return Burger()


@pytest.fixture
def bun_mock():
    """Mock для булочки."""
    return Mock(spec=Bun)


@pytest.fixture
def ingredient_mock():
    """Mock для ингредиента."""
    return Mock(spec=Ingredient)
