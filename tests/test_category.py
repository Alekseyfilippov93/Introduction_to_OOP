import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category():
    products = ['Samsung Galaxy S23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']
    return Category("Электроника", "Техника для дома", products)


@pytest.fixture
def sample_product():
    return Product("Ноутбук", "Игровой", 100000, 5)


def test_category_initialization(sample_category):
    """Проверка корректности инициализации категории."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert sample_category.products == ['Samsung Galaxy S23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']


def test_product_count_calculation(sample_category):
    """Проверка корректного подсчета количества продуктов в категории."""
    assert Category.product_count == len(sample_category.products)
