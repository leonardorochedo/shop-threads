import threading

from product import Product
from stock import Stock

class Repository():
    def __init__(self, name: str):
        self.name = name
        self.semaphore = threading.Semaphore(1)
    
    def stockProduct(self, product: Product, stock: Stock):
        self.semaphore.acquire()
        stock.stockProduct(product)
        print(f'{self.name} colocou o {product.getName()} no estoque!')
        self.semaphore.release()