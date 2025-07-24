import pytest
from bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_init(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_properties(self):
        bun = Bun("test bun", 150)
        assert bun.name == "test bun"
        assert bun.price == 150
