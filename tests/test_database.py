from unittest.mock import patch
from database import Database
from bun import Bun
from ingredient import Ingredient


class TestDatabase:

    def test_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6
        assert isinstance(db.buns[0], Bun)
        assert isinstance(db.ingredients[0], Ingredient)

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    @patch('database.Database.__init__', return_value=None)
    def test_empty_database(self, _):
        db = Database()
        db.buns = []
        db.ingredients = []
        assert db.available_buns() == []
        assert db.available_ingredients() == []
