import threading

from product import Product

class Stock():
    def __init__(self, name: str):
        self.name = name
        self.stock = []
        self.semaphore = threading.Semaphore(1)
    
    def stockProduct(self, product: Product):
        self.stock.append(product)
    
    def removeProduct(self, product: Product):
        self.stock.remove(product)
    
    def existProductInStock(self, product: Product):
        for i in self.stock:
            if (i.getName() == product.getName()):
                return True
        return False