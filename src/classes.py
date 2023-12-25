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
        self.__products.append(product)
        Category.total_products += 1

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_products(self):
        return '\n'.join(map(str, self.__products))

    def __str__(self):
        return f"{self.__name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return CategoryIterator(self.__products)

    @staticmethod
    def get_total_products():
        return Category.total_products


class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

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
        for product in category.__products:
            if product.get_name() == name:
                # Товар с таким именем уже существует, обновляем его
                if price > product.get_price():
                    product.price = price
                product.stock += stock
                return product

        # Товар с таким именем не найден, создаем новый
        new_product = Product(name, price, stock)
        category.add_product(new_product)
        return new_product
