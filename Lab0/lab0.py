
from abc import ABC, abstractmethod
import json
from os import name

class Product:
    def init(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Printer(ABC):
    @abstractmethod
    def print_product(self, product: Product):
        pass


class TextProductPrinter(Printer):
    def print_product(self, product: Product):
        print(f"Product: {product.get_name()}, Price: {product.get_price()} MDL")


class JSONProductPrinter(Printer):
    def print_product(self, product: Product):
        product_data = {
            'name': product.get_name(),
            'price': product.get_price()
        }
        print(json.dumps(product_data, indent=4))


if name == "main":
    product1 = Product("Smartphone", 5000)
    product2 = Product("Laptop", 15000)

    text_printer = TextProductPrinter()
    text_printer.print_product(product1)  
    text_printer.print_product(product2)  

    print("\n--- Now printing in JSON format ---\n")

    json_printer = JSONProductPrinter()
    json_printer.print_product(product1)
    json_printer.print_product(product2)  
