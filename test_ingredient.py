import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ing_type,name,price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 200)
])

def test_ingredient_init(ing_type, name, price):
    ing = Ingredient(ing_type, name, price)
    assert ing.get_type() == ing_type
    assert ing.get_name() == name
    assert ing.get_price() == price

def test_ingredient_properties():
    ing = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 150)
    assert ing.type == INGREDIENT_TYPE_SAUCE
    assert ing.name == "test sauce"
    assert ing.price == 150