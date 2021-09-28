from datetime import datetime
from uuid import *
import uuid
from random import *
from Transaction2 import Transaction
class Accaunt:
    transaction = []
    def __init__(self, number:int, name:str):
        self.id = uuid.uuid4
        self.number = number
        self.name = name

    def makeTransaction(self, id):
        self.transaction = Transaction(id, datetime.now())