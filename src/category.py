class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Category:
    """Определяем для каждого свой тип данных"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(self.products)
