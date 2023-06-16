import threading
import time

from consummer import Consummer


class Cashier():
    def __init__(self, name: str):
        self.name = name
        self.semaphore = threading.Semaphore(1)

    def run(self, consummer: Consummer):
        time.sleep(1)
        self.cashConsummer(consummer)

    def cashConsummer(self, consummer: Consummer):
        self.semaphore.acquire()
        if (len(consummer.getListOfProducts()) > 0):
            consummer.debitProducts()
            print(f'{self.name} liberou a compra do {consummer.name}')
        else:
            print(
                f'{self.name} disse ao {consummer.name} que seu carrinho está vazio')
        self.semaphore.release()
