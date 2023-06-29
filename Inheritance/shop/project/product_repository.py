from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        return [p for p in self.products if p.name == product_name][0]

    def remove(self, product_name):
        product = self.find(product_name)
        self.products.remove(product)

    def __repr__(self) -> str:
        return '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])