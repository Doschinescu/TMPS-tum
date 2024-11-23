from command_interface import Command

class AddProductCommand(Command):
    def __init__(self, cart, product):
        self.cart = cart
        self.product = product

    def execute(self):
        self.cart.add_product(self.product)
        print(f"Added {self.product} to the cart.")