from domain.product import Product

class ProductFactory:
    @staticmethod
    def create_product(name, price, description=''):
        return Product(name, price, description)
