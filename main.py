import threading
import random

from product import Product
from repository import Repository
from consummer import Consummer
from cashier import Cashier
from stock import Stock


# Instanciando as classes
repositories = []
consummers = []
cashiers = []
products = []

stock = Stock("Estoque")

for i in range(3):  # Defina no range a quantidade a ser criada
    # Instanciando a classe e já adicionando a lista
    repositories.append(Repository("Repositor " + str(i+1)))

for i in range(4):
    consummers.append(Consummer("Consumidor " + str(i+1)))

for i in range(2):
    cashiers.append(Cashier("Caixa " + str(i+1)))

for i in range(20):
    products.append(Product("Produto " + str(i+1)))


# Inicia as threads
count = 0

while count < 100:  # Definindo um contador apenas para o terminal não ficar em loop
    for f in repositories:
        threading.Thread(target=f.run, args=(
            random.choice(products), stock)).start()

    for f in consummers:
        threading.Thread(target=f.run, args=(
            random.choice(products), stock)).start()

    for f in cashiers:
        threading.Thread(target=f.run, args=(
            random.choice(consummers),)).start()

    count += 1
