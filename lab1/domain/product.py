class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name}: {self.price} MDL"

class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_details(self):
        return f"{self.name} (Electronics, {self.warranty_years} years warranty): {self.price} MDL"


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_details(self):
        return f"{self.name} (Clothing, Size {self.size}): {self.price} MDL"
