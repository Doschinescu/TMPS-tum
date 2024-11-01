from domain.order import Order
from domain.product import Product

class OrderBuilder:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)
        return self  

    def build(self):
        order = Order()
        for product in self._products:
            order.add_to_order(product)
        return order
