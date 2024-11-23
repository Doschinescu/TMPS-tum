from .command_interface import Command

class ClearCartCommand(Command):
    def __init__(self, cart):
        self.cart = cart

    def execute(self):
        self.cart.clear_cart()
        print("The cart has been cleared.")
