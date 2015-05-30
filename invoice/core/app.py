#!/usr/bin/env mypy-wrap
import json
from invoice.utils.PrettyDict import PrettyDict
from invoice.config import Config
from typing import *

class Customer(PrettyDict):
    def __init__(self, json: Dict[str, str]) -> None:
        self.name = json['name']
        self.adress = json['adress']

# class Invoice:
#     def __init__(self, customer) -> None:


class InvoiceApp:
    def __init__(self, config: Config) -> None:
        """
        config: a Config object which supplies all paths we need
        """
        customers_json = json.load(open(config.customers_path))
        self.customers = list(map(Customer, customers_json))
        print(self.customers[0])


def run() -> None:
    config_dir = '/home/jwerner/dev/invoice/config'
    database_dir = '/home/jwerner/dev/invoice/database'

    config = Config({
        'customers': '{}/customers.json'.format(database_dir)
    })
    invoice_app = InvoiceApp(config)

