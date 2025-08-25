import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category(sample_products):
    return Category("Электроника", "Техника для дома", sample_products)


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


def test_product_count_calculation(sample_category):
    """Проверка корректного подсчета количества продуктов в категории."""
    assert Category.product_count == len(sample_category.products)


def test_category_initialization(sample_category, sample_products):
    """Проверка корректности инициализации категории."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert len(sample_category.products) == 3
    assert sample_category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_add_product(sample_category, sample_product):
    """Проверка добавления продукта в категорию"""
    initial_count = len(sample_category.products)
    initial_total_count = Category.product_count
    sample_category.add_product(sample_product)
    assert (
            len(sample_category.products) == initial_count + 1
    )  # Проверка количество продуктов увеличилось на 1
    assert Category.product_count == initial_total_count + 1


def test_len_method(sample_category):
    """Проверка подсчёта общего количества товаров в категории"""
    assert len(sample_category) == 27  # 5 (Samsung) + 8 (iPhone) + 14 (Xiaomi)


def test_midle_price_with_products():
    """Тест на корректность вычисления средней цены"""
    products = [
        Product("Телефон_а", "Cерый", 100.0, 2),
        Product("Телефон_б", "Синий", 200.0, 1),
        Product("Телефон_в", "Зеленый", 300.0, 3),
    ]
    category = Category("Проверка теста", "Категория", products)
    assert category.middle_price() == 200.0


def test_midle_price_with_one_products():
    """Тест на корректность вычисления средней цены с одним товаром"""
    products = [
        Product("Телефон_а", "Cерый", 100.0, 2),
    ]
    category = Category("Проверка теста", "Категория", products)
    assert category.middle_price() == 100.0
