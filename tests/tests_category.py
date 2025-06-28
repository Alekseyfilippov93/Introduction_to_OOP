import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category():
    return Category("Электроника", "Техника для дома")


@pytest.fixture
def sample_product():
    return Product("Ноутбук", "Игровой", 100000, 5)


def test_category_initialization(sample_category):
    """Проверка корректности инициализации категории."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert sample_category.products == []


def test_add_product(sample_category, sample_product):
    """Проверка добавления товара в категорию."""
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Ноутбук"
