from domain.product import Product

class ProductBuilder:
    def __init__(self, name, price):
        self.product = Product(name, price)

    def set_description(self, description):
        self.product.description = description
        return self  

    def build(self):
        return self.product  
