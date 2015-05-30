#!/usr/bin/env mypy-wrap
import json
import inspect
from invoice.utils.pretty_dict import PrettyDict
from invoice.config import Config
from invoice.domain.customer import Customer
from invoice.domain.user import User
from invoice.domain.invoice import Invoice
from invoice.exporters.export import export
from typing import *

class InvoiceApp:
    def __init__(self, config: Config) -> None:
        customers_json = json.load(open(config.customers_path))
        self.customers = list(map(Customer, customers_json))
        self.exporters = config.exporters

        self.user = User(config.user)
        invoice = Invoice(
            customer=self.customers[0],
            user=self.user
        )
        self.export(invoice, self.exporters[0])


    def export(self, invoice: Invoice, exporter_name: str) -> None:
        # print(inspect.getmembers(exporters))
        export(invoice, exporter_name)


def run() -> None:
    config_dir = '/home/jwerner/dev/invoice/config'
    database_dir = '/home/jwerner/dev/invoice/database'

    config = Config({
        'customers_path': '{}/customers.json'.format(database_dir),
        'config_path': '{}/config.json'.format(config_dir)
    })
    invoice_app = InvoiceApp(config)

