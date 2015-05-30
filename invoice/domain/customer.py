from invoice.utils.pretty_dict import PrettyDict
from typing import *

class Customer(PrettyDict):
    def __init__(self, json: Dict[str, str]) -> None:
        self.name = json['name']
        self.adress = json['adress']
