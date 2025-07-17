from src.product import Product


class Category:
    """Определяем для каждого свой тип данных"""

    name: str
    description: str
    __products: list  # Приватный доступ к атрибуту
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = []  # Список товаров с приватным доступом
        Category.category_count += 1
        Category.product_count = len(products)

        for product in products:
            self.add_product(product)

    @property
    def products(self) -> str:
        """Геттер для списка товаров"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def add_product(self, product: Product):
        """Метод добавления товаров"""
        if not isinstance(product, Product):
            raise TypeError("Добавляем только Product")
        self.__products.append(product)
        Category.product_count += 1

    def __leb__(self):
        """Считаем количество товаров"""
        return len(self.__products)

    def __str__(self):
        """Строчное представление категории"""
        return f"{self.name}, количество продуктов: {len(self)} шт."
