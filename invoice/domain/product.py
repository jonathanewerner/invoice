from typing import *

from invoice.utils.pretty_dict import PrettyDict

class Product(PrettyDict):

    def __init__(self, description: str, price: int) -> None:
        self.description = description
        self.price = price

