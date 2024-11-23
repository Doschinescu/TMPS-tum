# client/main.py
from domain.cart import ShoppingCart
from domain.command.add_product_command import AddProductCommand
from domain.command.remove_product_command import RemoveProductCommand
from domain.command.clear_cart_command import ClearCartCommand

class CartInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

if __name__ == "__main__":
    cart = ShoppingCart()
    invoker = CartInvoker()

    add_laptop_command = AddProductCommand(cart, "Laptop", 1200)
    add_phone_command = AddProductCommand(cart, "Smartphone", 800)
    remove_laptop_command = RemoveProductCommand(cart, "Laptop", 1200)
    clear_cart_command = ClearCartCommand(cart)

    invoker.execute_command(add_laptop_command)
    invoker.execute_command(add_phone_command)
    invoker.execute_command(remove_laptop_command)
    invoker.execute_command(clear_cart_command)

    cart.show_cart()
