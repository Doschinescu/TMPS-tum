# client/main.py

from domain.cart import ShoppingCart
from domain.command.add_product_command import AddProductCommand
from domain.command.remove_product_command import RemoveProductCommand

def main():
    cart = ShoppingCart()

    product1 = "Laptop"
    product2 = "Smartphone"

    add_laptop = AddProductCommand(cart, product1)
    add_smartphone = AddProductCommand(cart, product2)
    remove_laptop = RemoveProductCommand(cart, product1)

    print("\nExecuting Commands:")
    add_laptop.execute()  
    add_smartphone.execute()  
    cart.show_cart()  

    print("\nUndoing Commands:")
    remove_laptop.execute()  
    cart.show_cart()  

if __name__ == "__main__":
    main()
