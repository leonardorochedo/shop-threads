import threading

class Cashier():
    def __init__(self):
        self.semaphore = threading.Semaphore(1)