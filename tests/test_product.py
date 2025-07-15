import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000, 10)


def test_price_setter(sample_product):
    """Проверка изменения цены."""
    sample_product.price = 45000
    assert sample_product.price == 45000
