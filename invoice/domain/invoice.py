from typing import *

from invoice.domain.customer import Customer
from invoice.domain.user import User
from invoice.domain.product import Product
from invoice.utils.pretty_dict import PrettyDict

class Invoice(PrettyDict):

    def __init__(
            self,
            customer: Customer,
            user: User,
            products: List[Product],
            notes: str,
            date: str) -> None:

        self.nr = 0
        self.customer = customer
        self.user = user
        self.products = products
        self.notes = notes
        self.date = date

