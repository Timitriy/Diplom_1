import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    return Mock(spec=Bun)


@pytest.fixture
def ingredient():
    return Mock(spec=Ingredient)


def test_burger_init(burger):
    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns(burger, bun):
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient(burger, ingredient):
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient


def test_remove_ingredient(burger, ingredient):
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(burger):
    ingredient1 = Mock()
    ingredient2 = Mock()
    ingredient3 = Mock()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)

    burger.move_ingredient(0, 2)
    assert burger.ingredients == [ingredient2, ingredient3, ingredient1]


def test_get_price(burger, bun):
    bun.get_price.return_value = 100
    ingredient1 = Mock()
    ingredient1.get_price.return_value = 50
    ingredient2 = Mock()
    ingredient2.get_price.return_value = 75

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    assert burger.get_price() == 100 * 2 + 50 + 75


def test_get_receipt(burger, bun):
    bun.get_name.return_value = "white bun"
    bun.get_price.return_value = 200

    ingredient1 = Mock()
    ingredient1.get_type.return_value = "SAUCE"
    ingredient1.get_name.return_value = "hot sauce"
    ingredient1.get_price.return_value = 100

    ingredient2 = Mock()
    ingredient2.get_type.return_value = "FILLING"
    ingredient2.get_name.return_value = "cutlet"
    ingredient2.get_price.return_value = 150

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    receipt = burger.get_receipt()
    assert "(==== white bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 650" in receipt