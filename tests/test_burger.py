from burger import Burger


class TestBurger:

    def test_init(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        ing1, ing2, ing3 = object(), object(), object()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1]

    def test_get_price(self, burger, bun_mock, ingredient_mock):
        bun_mock.get_price.return_value = 100

        ing1 = ingredient_mock
        ing1.get_price.return_value = 50

        ing2 = object()
        
        from unittest.mock import Mock
        ing2 = Mock()
        ing2.get_price.return_value = 75

        burger.set_buns(bun_mock)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert burger.get_price() == 100 * 2 + 50 + 75

    def test_get_receipt(self, burger, bun_mock):
        bun_mock.get_name.return_value = "white bun"
        bun_mock.get_price.return_value = 200

        from unittest.mock import Mock
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100

        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 150

        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()
        assert "(==== white bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 650" in receipt
