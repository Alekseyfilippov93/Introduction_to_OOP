from src.base_product import BaseProduct
from src.class_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    def __init__(self, name, description, price, quantity):
        if price <= 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity == 0: # Проверяем исключения, если количество равна нулю
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name  # Название
        self.description = description  # Описание
        self.__price = float(price)  # Приватный атрибут цены.
        self.quantity = quantity  # Количество в наличии
        super().__init__()

    def __add__(self, other):
        """Магический метод сложения"""
        if not isinstance(other, self.__class__):
            raise TypeError("Складываем только объекты product")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        return self.__price

    @classmethod
    def new_product(cls, product_data: dict):
        """Классметод для создания продукта из словаря"""
        required_fields = [
            "name",
            "description",
            "price",
            "quantity",
            "efficiency",
            "model",
            "memory",
            "color",
        ]
        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Не хватает обязательного поля: {field}")
        return cls(**product_data)

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер цены на положительное значение"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
