import threading

from product import Product
from repository import Repository
from consummer import Consummer
from cashier import Cashier
from stock import Stock

repositories = []
consummers = []
cashiers = []

stock = Stock("Estoque")

for i in range(3):
    repositories.append(Repository("Repositor " + str(i+1)))

for i in range(4):
    consummers.append(Consummer("Consumidor " + str(i+1)))

for i in range(2):
    cashiers.append(Cashier("Caixa " + str(i+1)))
