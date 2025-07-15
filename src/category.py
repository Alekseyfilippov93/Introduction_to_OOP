from src.product import Product


class Category:
    """Определяем для каждого свой тип данных"""

    name: str
    description: str
    __products: list  # Приватный доступ к атрибуту
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products  # Список товаров с приватным доступом
        Category.category_count += 1
        Category.product_count = len(self.products)

    @property
    def products(self) -> str:
        "Геттер для списка товаров"
        products_list = []
        for product in self.__products:
            products_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return "\n".join(products_list)

    def add_product(self, product: Product):
        "Метод добавления товаров"
        self.__products.append(product)
        Category.product_count += 1
