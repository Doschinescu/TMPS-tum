class ShoppingCart:
    _instance = None  

    def __new__(cls): 
        if cls._instance is None:
            cls._instance = super(ShoppingCart, cls).__new__(cls)
            cls._instance.products = []  
        return cls._instance

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product)
