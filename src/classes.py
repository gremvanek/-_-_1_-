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
        result = []
        for product in self.__products:
            result.append(f"{product.get_name()}, {product.get_price()} руб. Остаток: {product.get_stock()} шт.")
        return '\n'.join(result)

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
