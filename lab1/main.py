from domain.cart import Cart
from factory.product_factory import ProductFactory
from factory.order_builder import OrderBuilder
from models.product_type import ProductType

def main():
    smartphone = ProductFactory.create_product(ProductType.ELECTRONICS, "Smartphone", 5000, warranty_years=2)
    shirt = ProductFactory.create_product(ProductType.CLOTHING, "Shirt", 500, size='L')

    cart = Cart.get_instance()
    cart.add_to_cart(smartphone)
    cart.add_to_cart(shirt)

    print("Cart items:")
    for item in cart.list_cart_items():
        print(item)
    print(f"Total: {cart.get_cart_total()} MDL\n")

    order_builder = OrderBuilder()
    order = order_builder.add_product(smartphone).add_product(shirt).build()

    print("Order items:")
    for item in order.list_order_items():
        print(item)
    print(f"Order Total: {order.get_total()} MDL")

if __name__ == "__main__":
    main()
