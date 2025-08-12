from src.product import Product


def test_repr_output(capsys):
    """Тестирует вывод repr через PrintMixin"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    captured = capsys.readouterr()
    assert captured.out.strip() == repr(product)


def test_print_mixin_integration(capsys):
    """Тестирует интеграцию PrintMixin с Product"""
    # Проверяем, что __init__ вызывает print(repr(self))
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    captured = capsys.readouterr()
    assert captured.out.strip() == repr(test_product)
