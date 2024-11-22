class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.description = "digital"
        

    def Digital(self):
        return "digital"
    
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class OffProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.description = "Offline"
        
    def Offline(self):
        return "Offline"