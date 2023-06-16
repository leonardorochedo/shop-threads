import threading
import time

from product import Product
from stock import Stock


class Consummer():
    def __init__(self, name: str):
        self.name = name
        self.listOfProducts = []
        self.semaphore = threading.Semaphore(1)

    def run(self, product: Product, stock: Stock):
        time.sleep(1)
        self.catchProduct(product, stock)

    def catchProduct(self, product: Product, stock: Stock):
        self.semaphore.acquire()
        if (stock.existProductInStock(product)):
            self.listOfProducts.append(product)
            stock.removeProduct(product)
            print(f'{product.getName()} foi adicionado ao carrinho do {self.name}')
        else:
            print(
                f"{self.name} tentou achar {product.getName()} porém não está disponível no estoque!")
        self.semaphore.release()

    def getListOfProducts(self):
        return self.listOfProducts

    def debitProducts(self):
        self.listOfProducts.clear()
