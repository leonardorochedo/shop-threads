import threading
from product import Product
from stock import Stock

class Consummer():
    def __init__(self, name: str):
        self.name = name
        self.listOfProducts = []
        self.semaphore = threading.Semaphore(1)
    
    def catchProduct(self, product: Product, stock: Stock):
        self.semaphore.acquire()
        if (stock.existProductInStock(product)):
            self.listOfProducts.append(product)
            stock.removeProduct(product)
            print(f'{product.getName()} foi adicionado ao carrinho do {self.name}')
        else:
            print(f"{product.getName()} não está disponível no estoque!")
        self.semaphore.release()
    
    def getListOfProducts():
        return self.listOfProducts
    
    def debitProducts():
        if (len(self.listOfProducts()) > 0):
            self.listOfProducts.clear()