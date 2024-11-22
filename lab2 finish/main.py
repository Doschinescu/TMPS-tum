from client.shopping_facade import ShoppingFacade
from adapters.external_product_adapter import ExternalProductAdapter

def main():
    facade = ShoppingFacade()

    facade.add_product("Laptop", 1200, "Gaming Laptop")
    facade.add_product("Headphones", 150, "Noise-cancelling headphones")

    facade.add_discounted_product("Smartphone", 800, 0.2, "Latest model smartphone")

    external_data = {
        "title": "External Monitor",
        "cost": 300,
        "info": "27-inch 4K monitor"
    }
    adapter = ExternalProductAdapter(external_data)
    external_product = adapter.to_product()
    facade.cart.add_product(external_product)

    print("\nProducts in the cart:")
    facade.view_cart()

if __name__ == "__main__":
    main()
