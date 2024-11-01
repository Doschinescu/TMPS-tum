from domain.order import Order

class Cart:
    _instance = None

    def __init__(self):
        if Cart._instance is not None:
            raise Exception("This class is a singleton!")
        self.order = Order()
        Cart._instance = self

    @staticmethod
    def get_instance():
        if Cart._instance is None:
            Cart()
        return Cart._instance

    def add_to_cart(self, product):
        self.order.add_product(product)

    def get_cart_total(self):
        return self.order.get_total()

    def list_cart_items(self):
        return self.order.list_order_items()
