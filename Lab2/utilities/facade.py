class ShoppingFacade:
    def __init__(self):
        self.cart = ShoppingCart()

    def add_product(self, name, price, description=''):
        product = Product(name, price, description=description)
        self.cart.add_product(product)

    def view_cart(self):
        self.cart.display_products()

    def apply_discount(self, product_name, discount):
        self.cart.apply_discount_to_product(product_name, discount)
