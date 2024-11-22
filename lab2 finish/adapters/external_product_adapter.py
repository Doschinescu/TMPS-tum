from domain.product import Product, OffProduct

class ExternalProductAdapter:
    def __init__(self, product, **adapted_methods):
        self.product = product
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.product, attr)

    def original_dict(self):
        return self.product.__dict__
    