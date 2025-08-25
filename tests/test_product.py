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


def test_private_price(sample_product):  # Тесты на цену
    with pytest.raises(AttributeError):
        print(sample_product.__price)


def test_add(sample_product, sample_product_2):
    """Тест на проверку магического метода сложения"""
    assert sample_product + sample_product_2 == 1000000


def test_product_new_with_zero_quantity():
    """Тест на создание продукта 0 количеством, при котором будет вызывать ValueError"""
    with pytest.raises(ValueError) as exc_info:
        Product("Не соответствует товар", "Неверное количество", 1000.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)


def test_with_more_0_quantity():
    """Тест, на проверку, где количество шт больше 0"""
    product = Product("Телефон", "Смартфон", 50000.0, 2)
    assert product.quantity == 2
    assert product.name == "Телефон"
