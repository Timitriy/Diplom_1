from bun import Bun
import pytest

@pytest.mark.parametrize('name, price', [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_bun_init(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

def test_bun_properties():
    bun = Bun("test bun", 150)
    assert bun.name == "test bun"
    assert bun.price == 150