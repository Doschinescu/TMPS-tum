from domain.product import Product

class ExternalProductAdapter:
    def __init__(self, external_data):
        self.external_data = external_data

    def to_product(self):
        return Product(
            name=self.external_data['title'],
            price=self.external_data['cost'],
            description=self.external_data.get('info', 'No description')
        )
