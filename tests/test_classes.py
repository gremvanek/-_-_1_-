

from src.classes import Category, Smartphone, LawnGrass


def test_add_product_to_category():
    category = Category("Электроника", "Технические устройства")
    smartphone = Smartphone("iPhone", 1000, 10, "High", "X", 128, "Silver")
    category.add_product(smartphone)
    assert len(category.get_products()) == 1
    assert Category.total_products == 1


def test_calculate_average_price_with_zero_products():
    category = Category("Электроника", "Технические устройства")
    assert category.calculate_average_price() == 0


def test_calculate_average_price_with_products():
    category = Category("Электроника", "Технические устройства")

    smartphone = Smartphone("iPhone", 1000, 10, "High", "X",
                            128, "Silver")
    lawn_grass = LawnGrass("Газонная трава", 5, 100, "Green", 10)

    category.add_product(smartphone)
    category.add_product(lawn_grass)

    assert category.calculate_average_price() == 9.136363636363637


def test_create_product_with_smartphone():
    category = Category("Электроника", "Технические устройства")
    new_product = Smartphone.create_product("Новый смартфон", 500, 10, category)
    assert len(category.get_products()) == 1
    assert new_product.get_stock() == 10
    assert Category.total_products == 4
