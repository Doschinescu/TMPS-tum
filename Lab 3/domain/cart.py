class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product}' added to the cart.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product '{product}' removed from the cart.")
        else:
            print(f"Product '{product}' not found in the cart.")

    def show_cart(self):
        if self.products:
            print("Current products in the cart:", ", ".join(self.products))
        else:
            print("The cart is empty.")
