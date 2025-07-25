class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name  # Название
        self.description = description  # Описание
        self.__price = price if price > 0 else 0.0  # Приватный атрибут цены.
        self.quantity = quantity  # Количество в наличии
        if price <= 0:
            raise ValueError("Цена не может быть отрицательной")


    def __add__(self, other):
        """Магический метод сложения"""
        if not isinstance(other, Product):
            raise TypeError("Складываем только объекты product")
        return (self.price * self.quantity) + (other.price * other.quantity)


    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, product_data: dict):
        """Классметод для создания продукта из словаря"""
        price = product_data["price"]
        if price <= 0:
            print("Цена не может быть меньше 0")
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=price,
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

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
