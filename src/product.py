from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Сеттер для цены"""
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"{self.__class__.__name__}({signature})")


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом")

        super().__init__(name, description, price, quantity)
        self.__price = price


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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает результат сложения сумм всех товаров двух категорий"""
        if type(other) == type(self):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError

class Smartphone(Product):
    def __init__(self, name, description, __price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, __price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, __price, quantity, country, germination_period, color):
        super().__init__(name, description, __price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

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
        if not isinstance(products, Product):
            raise TypeError
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

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."
