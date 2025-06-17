class Product:
    """Класс для продуктов"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой и понижением если пользователь захочет понизить"""
        if new_price <= 0:
            print(f"Цена {new_price} - не должна быть нулевая или отрицательная")
            return self.__price

        if new_price < self.__price:
            answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите понижение (y/n) \n")
            if answer.lower() != 'y':
                print("Понижение цены отменено")
                return
            self.__price = new_price
        else:
            print(f"Цена повышается с {self.__price} до {new_price}")
            self.__price = new_price

    @classmethod
    def new_product(cls, new_product, existing_products=None):
        """ Создание нового продукта"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)


class Category:
    """Класс для категорий"""
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, products):
        """ Метод в который передается объект класса Product и
        уже его записывает в приватный атрибут списка товаров."""
        self.__products.append(products)
        Category.category_count += 1

    @property
    def product(self):
        """ Возможность просмотра товаров через геттер"""
        products_str = []
        for product in self.__products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            products_str.append(product_info)
        return products_str
