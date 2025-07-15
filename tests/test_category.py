import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category():
    products = ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
    return Category("Электроника", "Техника для дома", products)


@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5),
        Product("iPhone 15", "512GB", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "128GB", 31000.0, 14),
    ]


@pytest.fixture
def sample_product():
    return Product("Ноутбук", "Игровой", 100000, 5)


def test_category_initialization(sample_category):
    """Проверка корректности инициализации категории."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert sample_category.products == [
        "Samsung Galaxy S23 Ultra",
        "Iphone 15",
        "Xiaomi Redmi Note 11",
    ]


def test_product_count_calculation(sample_category):
    """Проверка корректного подсчета количества продуктов в категории."""
    assert Category.product_count == len(sample_category.products)


def test_add_product(sample_category, sample_product):
    """Проверка добавления продукта в категорию"""
    initial_count = len(sample_category.products)
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == initial_count + 1
    assert Category.product_count == initial_count + 1
