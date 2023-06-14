from consummer import Consummer
import threading

class Cashier():
    def __init__(self, name: str):
        self.name = name
        self.semaphore = threading.Semaphore(1)
    
    def cashConsummer(consummer: Consummer):
        self.semaphore.acquire()
        if (len(consummer.getListOfProducts()) > 0):
            consummer.debitProducts()
            print(f'{self.name} liberou a compra do {consummer.name}')
        self.semaphore.release()