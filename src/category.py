from src.product import Product


class Category:
    """Определяем для каждого свой тип данных"""

    name: str
    description: str
    __products: list  # Приватный доступ к атрибуту
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = []  # Список товаров с приватным доступом
        Category.category_count += 1

        for product in products:
            self.add_product(product)

    @property
    def products(self) -> list[Product]:
        """Геттер для списка товаров"""
        return self.__products

    def add_product(self, product: Product):
        """Метод добавления товаров"""
        if not isinstance(product, Product):
            raise TypeError("Добавляем только Product")
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик продуктов

    def __len__(self) -> int:
        """Считаем количество товаров"""
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """Строчное представление категории"""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def middle_price(self) -> float:
        """Метод, который подсчитывает средний ценник всех товаров"""
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)  # Вычисляем среднюю цену
            return average_price
        except ZeroDivisionError:
            return 0.0
