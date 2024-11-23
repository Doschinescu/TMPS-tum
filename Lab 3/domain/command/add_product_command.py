from .command_interface import Command

class AddProductCommand(Command):
    def __init__(self, cart, product_name, price):
        self.cart = cart
        self.product_name = product_name
        self.price = price

    def execute(self):
        product = {"name": self.product_name, "price": self.price}  
        self.cart.add_product(product)
        print(f"Added {self.product_name} (${self.price}) to the cart.")
