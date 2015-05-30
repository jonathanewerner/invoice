from typing import *

from invoice.utils.pretty_dict import PrettyDict

class User(PrettyDict):
    def __init__(self, json: Dict[str, str]) -> None:
        self.email = json['email']
        self.telephone = json['telephone']
        self.steuernummer = json['steuernummer']
        self.ustIdNr = json['ustIdNr']
        self.adress = json['adress']
        self.bank = json['bank']
