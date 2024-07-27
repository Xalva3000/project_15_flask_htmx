from dataclasses import dataclass, field
from random import randint

from faker import Faker


fake = Faker()


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    @property
    def names(self):
        return set([product.name for product in self.products.values()])

    def add(self, name, price):
        product = Product(
            id=self.next_id,
            name=name,
            price=price
        )
        self.products[product.id] = product
        return product

    def get_list(self):
        return list(self.products.values())

    def name_exists(self, product_name):
        return product_name in self.names



products_storage = ProductsStorage()

[products_storage.add(name=fake.last_name(), price=randint(1_000, 10_000)) for _ in range(10)]
