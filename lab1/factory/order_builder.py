from domain.order import Order
from domain.product import Product

class OrderBuilder:
    def __init__(self):
        self.order = Order()  

    def add_product(self, product: Product):
        self.order.add_product(product)
        return self  

    def build(self):
        return self.order
