import pytest

from src.product import Category, Product


@pytest.fixture
def product_iphone():
    product_1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product_1


def test_product(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_product_attribute_modification():
    product = Product("Samsung Galaxy S22 Ultra (2024)", "256GB, Серый цвет, 200MP камера", 150000.0, 5)
    product.name = "Samsung Galaxy S23 Ultra (2025)"
    product.price = 190000.0
    product.quantity = 10

    assert product.name == "Samsung Galaxy S23 Ultra (2025)"
    assert product.price == 190000.0
    assert product.quantity == 10


def test_product_min_price():
    product = Product("Samsung Galaxy S23 Ultra (2025)", "Description", 0.0, 5)
    assert product.price == 0.0


def test_product_min_quantity():
    product = Product("Samsung Galaxy S23 Ultra (2025)", "Description", 100.0, 0)
    assert product.quantity == 0


@pytest.fixture
def category_creation():
    product_1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_2 = Product("Samsung Galaxy S23 Ultra", "256GB, " "Серый цвет, 200MP камера", 180000.0, 5)
    category = Category("Смартфоны", "Описание категории", [product_1, product_2])
    return product_1, product_2, category


def test_category(category_creation):
    product_1, product_2, category = category_creation
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_category_count():
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category_1 = Category("Смартфоны", "Описание категории", [product_1, product_2])
    category_2 = Category("Телевизоры", "Описание категории", [product_3])

    assert Category.category_count == 2
    assert Category.product_count == 1
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание категории"
    assert len(category_1.products) == 2
    assert category_2.name == "Телевизоры"
    assert category_2.description == "Описание категории"
    assert len(category_2.products) == 1


def test_count_category():
    Category("Смартфоны", "Описание", [])
    Category("Телевизоры", "Описание", [])
    assert Category.category_count == 2


def test_category_empty_products():
    category = Category("Пустая категория", "Описание пустой категории", [])
    assert len(category.products) == 0
    assert Category.product_count == 0
    assert Category.category_count == 1
    assert category.name == "Пустая категория"
    assert category.description == "Описание пустой категории"
