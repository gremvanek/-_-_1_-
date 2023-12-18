import pytest
from src.Classes import Category, Product


@pytest.fixture
def test_category_1():
    return Category("Электроника", "Технические устройства")


@pytest.fixture
def test_category_2():
    return Category("Одежда", "Одежда и аксессуары")


@pytest.fixture
def test_product_1():
    return Product("Смартфон", "Современный смартфон", 499.99, 50)


@pytest.fixture
def test_product_2():
    return Product("Футболка", "Мужская футболка", 19.99, 100)


def test_category_initialization(test_category_1):
    assert test_category_1.name == "Электроника"
    assert test_category_1.description == "Технические устройства"
    assert test_category_1.products == []


def test_product_initialization(test_product_1):
    assert test_product_1.name == "Смартфон"
    assert test_product_1.description == "Современный смартфон"
    assert test_product_1.price == 499.99
    assert test_product_1.quantity_in_stock == 50


def test_add_product_to_category_and_count(test_category_1, test_category_2, test_product_1, test_product_2):
    test_category_1.add_product(test_product_1)
    assert len(test_category_1.products) == 1
    assert Category.total_products == 1

    test_category_2.add_product(test_product_2)
    assert len(test_category_2.products) == 1
    assert Category.total_products == 2
