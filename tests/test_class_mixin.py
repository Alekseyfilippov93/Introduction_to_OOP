from src.product import Product
from src.smartphone import Smartphone


def test_repr_output(capsys):
    """Тестирует вывод repr через PrintMixin"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    captured = capsys.readouterr()
    assert captured.out.strip() == repr(product)
    assert "name=QLED 4K" in repr(product)


def test_smartphone_repr(capsys):
    """Проверка вывода для наследника"""
    phone = Smartphone("iPhone", "Pro", 100000, 2, 95.0, "15", 256, "Black")
    captured = capsys.readouterr()
    assert "Smartphone" in captured.out
    assert "model=15" in repr(phone)


def test_print_mixin_integration(capsys):
    """Тестирует интеграцию PrintMixin с Product"""
    # Проверяем, что __init__ вызывает print(repr(self))
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    captured = capsys.readouterr()
    assert captured.out.strip() == repr(test_product)
