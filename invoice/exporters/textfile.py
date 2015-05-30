from typing import *

from pprint import pprint
import json

from invoice.domain.invoice import Invoice

LINE = '-'*20

def run(invoice: Invoice) -> None:
    pprint(invoice)
    s = ''
    s += 'Rechnung {}\n{}\n\n'.format(invoice.nr, LINE)
    s += 'Von:\n{}\n\n'.format(invoice.user.adress)
    s += 'Email: {}\n'.format(invoice.user.email)
    s += 'Telefon: {}\n'.format(invoice.user.telephone)
    s += 'USt.Id-Nr: {}\n'.format(invoice.user.ustIdNr)
    s += 'Steuernummer: {}\n\n'.format(invoice.user.steuernummer)
    s += 'An:\n{}\n'.format(invoice.customer.adress)
    print(s)
