from typing import *

from string import Template

from invoice.utils.pretty_dict import PrettyDict
from invoice.utils.ui import err
from invoice.domain.product import Product


class ProductTemplate(PrettyDict):

    def __init__(self, json: Dict[str, str]) -> None:
        self.description = json['description']

    def create_product(
            self,
            replacements: Dict[str, str],
            price=None) -> Product:

        try:
            description = Template(self.description).substitute(replacements)
        except KeyError:
            raise KeyError('The replacements for the product template are not valid. "{}", repls: {}'.format(self.description, replacements))

        return Product(description, price or self.price)








