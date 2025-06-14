import json
import os
from typing import List

from config import JSON_DATA
from src.product import Category, Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_objects(data: dict) -> List[Category]:
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            products.append(Product(**product_data))

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)

    return categories


if __name__ == "__main__":
    data_json = read_json(JSON_DATA)
    categories = create_objects(data_json)
    print(categories[0].name)
    print(categories[1].products)
