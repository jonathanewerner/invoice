from typing import *

from invoice.utils.pretty_dict import PrettyDict

class Bank(PrettyDict):
    def __init__(self, json) -> None:
        self.name = json['name']
        self.blz = json['blz']
        self.owner = json['owner']
        self.iban = json['iban']

class User(PrettyDict):
    def __init__(self, json: Dict[str, str]) -> None:
        self.email = json['email']
        self.telephone = json['telephone']
        self.steuernummer = json['steuernummer']
        self.ustIdNr = json['ustIdNr']
        self.adress = json['adress']
        self.bank = Bank(json['bank'])
