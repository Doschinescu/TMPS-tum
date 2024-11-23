from .command_interface import Command

class RemoveProductCommand(Command):
    def __init__(self, cart, product, price):
        self.cart = cart
        self.product = product
#       self.price = price

    def execute(self):
        self.cart.remove_product(self.product)
        print(f"Removed {self.product} from the cart.")
    
    # def execute(self):
    #     self.cart.remove_product(self.product)
    #     print(f"Remove {self.product}" from the cart")