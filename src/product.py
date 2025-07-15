class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name  # Название
        self.description = description  # Описание
        self.__price = price  # Приватный атрибут цены.
        self.quantity = quantity  # Количество в наличии

    @classmethod
    def new_product(cls, product_data: dict):
        """Классметод для создания продукта из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
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
