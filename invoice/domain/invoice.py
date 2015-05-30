from invoice.domain.customer import Customer
from invoice.domain.user import User
from invoice.utils.pretty_dict import PrettyDict

class Invoice(PrettyDict):
    def __init__(self, customer: Customer, user: User) -> None:
        self.nr = 0
        self.customer = customer
        self.user = user

