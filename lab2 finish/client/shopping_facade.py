from models.cart import ShoppingCart
from factories.product_factory import ProductFactory
from decorators.discount_decorator import DiscountedProductDecorator

class ShoppingFacade:
    def __init__(self):
        self.cart = ShoppingCart()

    def add_product(self, name, price, description=''):
        product = ProductFactory.create_product(name, price, description)
        self.cart.add_product(product)

    def add_discounted_product(self, name, price, discount, description=''):
        product = ProductFactory.create_product(name, price, description)
        discounted_product = DiscountedProductDecorator(product, discount)
        self.cart.add_product(discounted_product)

    def view_cart(self):
        self.cart.display_products()
