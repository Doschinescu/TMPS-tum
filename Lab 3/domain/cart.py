
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product['name']} added to the cart.")

    def remove_product(self, product):
        self.products = [p for p in self.products if p["name"] != product]
        print(f"{product} removed from the cart.")

    def clear_cart(self): 
        self.products = []
        print("Cart cleared.")

    def show_cart(self):
        if not self.products:
            print("Cart is empty.")
        else:
            print("Products in cart:")
            for p in self.products:
                print(f"{p['name']} - ${p['price']}")
