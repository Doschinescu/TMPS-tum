from itertools import product
from client.shopping_facade import ShoppingFacade
from adapters.external_product_adapter import ExternalProductAdapter 
from domain.product import Product, OffProduct


def main():
    Objects = []
    
    product1 = Product("Monitor", 100)
    Objects.append(ExternalProductAdapter(product1, types=product1.Digital))

    product2 = OffProduct("Case", 50)
    Objects.append(ExternalProductAdapter(product2, types=product2.Offline))


    for obj in Objects:
        print("A {0} is a {1} device".format(obj.name, obj.types()))

if __name__ == "__main__":
    main()
