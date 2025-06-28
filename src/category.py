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
    count_category = 0
    count_product = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.count_category += 1
        Category.count_product = len(self.products)
