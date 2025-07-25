import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000, 10)


@pytest.fixture
def sample_product_2():
    return Product("Ноутбук", "Игровой", 100000, 5)


def test_price_setter(sample_product):
    """Проверка изменения цены."""
    sample_product.price = 45000
    assert sample_product.price == 45000


def test_create_product():  # Проверка на создание продукта
    p = Product("Ноутбук", "Игровой", 100000, 5)
    assert p.name == "Ноутбук"
    assert p.description == "Игровой"
    assert p.price == 100000  # Проверка геттера
    assert p.quantity == 5


def test_str_representation(sample_product):
    assert str(sample_product) == "Телефон, 50000 руб. Остаток: 10 шт."


def test_private_price(sample_product):  # Тесты на цену
    with pytest.raises(AttributeError):
        print(sample_product.__price)


def test_add(sample_product, sample_product_2):
    """Тест на проверку магического метода сложения"""
    assert sample_product + sample_product_2 == 1000000
