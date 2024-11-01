from models.product_type import ProductType
from domain.product import Product, Electronics, Clothing

class ProductFactory:
    @staticmethod
    def create_product(product_type: ProductType, name: str, price: float, **kwargs) -> Product:

        if product_type == ProductType.ELECTRONICS:
            return Electronics(name, price, kwargs.get('warranty_years', 1))
        
        elif product_type == ProductType.CLOTHING:
            return Clothing(name, price, kwargs.get('size', 'M'))
        
        else:
            return Product(name, price)
