from abc import ABC, abstractmethod


class CategoryIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            raise ValueError("Нельзя добавить в категорию объект, не являющийся продуктом")

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_products(self):
        return self.__products

    def __str__(self):
        return f"{self.__name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return iter(self.__products)

    @staticmethod
    def get_total_products():
        return Category.total_products


class Product(ABC):
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    @abstractmethod
    def get_description(self):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        user_confirmation = input(f"Вы уверены, что хотите изменить цену на {new_price} руб.? (y/n): ")
        if user_confirmation.lower() == 'y':
            self.__price = new_price
            print("Цена успешно изменена.")
        else:
            print("Изменение цены отменено.")

    def __str__(self):
        return f"{self.__name}, {self.__price} руб. Остаток: {self.__stock} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total_price = (self.__price * self.__stock) + (other.__price * other.__stock)
            total_stock = self.__stock + other.__stock
            return Product(f"{self.__name} + {other.__name}", total_price / total_stock, total_stock)
        else:
            raise TypeError("Unsupported operand type for +")

    @staticmethod
    def create_product(name, price, stock, category):
        for product in category.get_products():
            if product.get_name() == name:
                if price > product.get_price():
                    product.price = price
                product_stock = product.get_stock()
                product_stock += stock
                product.__stock = product_stock
                return product

        new_product = Product(name, price, stock)
        category.add_product(new_product)
        return new_product


class ReprMixin:
    def __repr__(self):
        attrs = [f"{attr}={getattr(self, attr)}" for attr in vars(self)]
        return f"{type(self).__name__}({', '.join(attrs)})"


class Smartphone(Product, ReprMixin):
    def __init__(self, name, price, stock, performance, model, memory_capacity, color):
        super().__init__(name, price, stock)
        self.__performance = performance
        self.__model = model
        self.__memory_capacity = memory_capacity
        self.__color = color

    def get_description(self):
        return f"Смартфон {self.__name}"

    def get_performance(self):
        return self.__performance

    def get_model(self):
        return self.__model

    def get_memory_capacity(self):
        return self.__memory_capacity

    def get_color(self):
        return self.__color


class LawnGrass(Product, ReprMixin):
    def __init__(self, name, price, stock, color, height):
        super().__init__(name, price, stock)
        self.__color = color
        self.__height = height

    def get_description(self):
        return f"Трава газонная {self.__name}"

    def get_color(self):
        return self.__color

    def get_height(self):
        return self.__height

    class Order(ABC):
        def __init__(self, product, quantity):
            self.__product = product
            self.__quantity = quantity
            self.__total_price = self.__product.price * self.__quantity

        @abstractmethod
        def get_total_price(self):
            pass

        @abstractmethod
        def get_product(self):
            pass

        @abstractmethod
        def get_quantity(self):
            pass
