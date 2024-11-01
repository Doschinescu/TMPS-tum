class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        return sum(product.price for product in self.products)

    def list_order_items(self):
        return [product.get_details() for product in self.products]
