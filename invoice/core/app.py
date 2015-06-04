#!/usr/bin/env mypy-wrap
from typing import *

import argparse
import json
import sys
import time
from string import Template

from invoice.utils.pretty_dict import PrettyDict
from invoice.utils.ui import err
from invoice.config import Config
from invoice.domain.customer import Customer
from invoice.domain.user import User
from invoice.domain.product_template import ProductTemplate
from invoice.domain.product import Product
from invoice.domain.invoice import Invoice
from invoice.exporters.export import export

class InvoiceApp:

    def __init__(self, config: Config) -> None:
        customers_json = json.load(open(config.customers_path))

        product_templates = json.load(open(config.product_templates_path)) # type: Dict[str, dict]
        self.product_templates = \
            {shortname: ProductTemplate(product_template) for
             shortname, product_template in product_templates.items()}

        self.customers = \
            {shortname: Customer(customer) for
            shortname, customer in customers_json.items()}

        self.exporters = config.exporters
        self.notes = config.notes

        self.user = User(config.user)


    def create_invoice(self, nr: int, products: List[Product], customer_shortname: str):
        invoice = Invoice(
                nr=nr,
                customer=self.customers[customer_shortname],
                products=products,
                user=self.user,
                notes=self.notes,
                date=time.strftime("%d.%m.%Y"))

        self.export(invoice, self.exporters[0])


    def make_product(
            self,
            product_shortname: str,
            replacements: Dict[str, str],
            price: int
            ) -> Product:
        """
        create a product instance from a template with the necessary parameters
        """
        product_template = self.product_templates[product_shortname] # type: ProductTemplate
        product_item = product_template.create_product(replacements, price) # type: Product

        return product_item


    def export(self, invoice: Invoice, exporter_name: str) -> None:
        export(invoice, exporter_name)

def parse_product(s: str):
    shortname, args = s.split('[')
    args_str = args[:-1]
    args = dict(tuple(s.split('=')) for s in args_str.split(','))
    args['price'] = int(args['price'])
    return shortname, args, args['price']

def run(args: List[str]) -> str:
    config_path = '/home/jwerner/dev/invoice/config/config.json'

    config = Config(config_path)
    invoice_app = InvoiceApp(config)

    parser = argparse.ArgumentParser(prog='invoice')
    subparsers = parser.add_subparsers(help='available subcommands')
    parser_new = subparsers.add_parser('new', help='new invoice')
    parser_new.add_argument('nr', type=int, help='invoice nr')
    parser_new.add_argument('customer', type=str, help='customer shortname')
    parser_new.add_argument('products', nargs='+', type=str, help='product shortname/s plus args')

    make_product = lambda product_string: \
            invoice_app.make_product(*parse_product(product_string))

    f = lambda args: invoice_app.create_invoice(
            nr=args.nr,
            customer_shortname=args.customer,
            products=list(map(make_product, args.products)))
    parser_new.set_defaults(func=f)

    args = parser.parse_args(args)
    args.func(args)
    # print(args)
    # f(args)



