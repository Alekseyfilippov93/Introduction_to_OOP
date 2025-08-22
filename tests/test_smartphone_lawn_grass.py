import pytest
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", "Pro", 100000, 3, 95.5, "15", 256, "Black")


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Трава", "Газонная", 500, 10, "Россия", "14 дней", "Зеленая")


def test_smartphone_creation(sample_smartphone):
    assert sample_smartphone.model == "15"
    assert sample_smartphone.memory == 256


def test_lawn_grass_creation(sample_lawn_grass):
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "14 дней"


def test_inherited_addition(sample_smartphone, sample_lawn_grass):
    # Проверяем сложение объектов одного класса
    another_phone = Smartphone("Samsung", "Ultra", 80000, 2, 90, "S23", 512, "Blue")
    total = sample_smartphone + another_phone
    assert total == 100000 * 3 + 80000 * 2

    # Проверяем ошибку при сложении разных классов
    with pytest.raises(TypeError):
        sample_smartphone + sample_lawn_grass
