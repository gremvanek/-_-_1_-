class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_products += 1


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
