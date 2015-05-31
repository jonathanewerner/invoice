from typing import *

from pprint import pprint
import json
from textwrap import dedent # type: ignore
from string import Template

from invoice.domain.invoice import Invoice

LINE = '-'*20

def add_newlines(s: str) -> str:
    return '\n\n'.join(s.split('\n'))


def run(invoice: Invoice) -> None:
    # pprint(invoice)

    s = Template(dedent("""
    # Rechnung
    </br>

    <table class='header'>
    <tr>
    <td>

    **An:**

    $customer_adress

    </td>
    <td align='right'>


    **Von:**

    $adress

    </br>
    <table class='right-align-second-column'>

    <tr> <td>*Email*: </td><td>$email</td> </tr>
    <tr> <td>*Telefon*: </td><td>$telephone</td> </tr>
    <tr> <td>*USt.Id-Nr*: </td><td>$ustIdNr</td> </tr>
    <tr> <td>*Steuernummer*: </td><td>$steuernummer</td> </tr>
    <tr> <td></br></td></tr>
    <tr> <td>Rechnungsnr: </td><td>$rnr</td> </tr>
    <tr> <td>Rechnungsdatum: </td><td>$rdate</td> </tr>

    </table>


    </td>
    </tr>
    </table>

    </br>
    </br>
    <table class='products'>
    <tr><th>Beschreibung</th><th>Preis</th></tr>
    <tr class='white'><td>&nbsp;</td><td>&nbsp;</td></tr>
    $products
    <tr class='white'><td>&nbsp;</td><td>&nbsp;</td></tr>
    <tr><td class='gesamt'>Gesamt:</td><td class='sum'>$sum €</td></tr>
    </table>

    </br>

    $notes

    </br>

    <p class='space'>Bitte überweisen Sie den Betrag auf folgendes Konto:</p>

    <table class='bank-info'>
    <tr><td>*Bank:*</td> <td>$bank_name</td></tr>
    <tr><td>*BLZ:*</td> <td>$bank_blz</td></tr>
    <tr><td>*Name:*</td> <td>$bank_owner</td></tr>
    <tr><td>*IBAN:*</td> <td>$bank_iban</td></tr>
    </table>

    """))




    products_string = ''
    for product in invoice.products:
        products_string += '<tr><td>{}</td><td>{} €</td></tr>'.format(product.description, product.price)

    sum_ = sum(product.price for product in invoice.products)

    d = dict( # type: ignore
            rnr=invoice.nr,
            rdate=invoice.date,

            adress=add_newlines(invoice.user.adress),
            email=invoice.user.email,
            telephone=invoice.user.telephone,
            ustIdNr=invoice.user.ustIdNr,
            steuernummer=invoice.user.steuernummer,

            customer_adress=add_newlines(invoice.customer.adress),

            products=products_string,
            sum=sum_,
            notes=invoice.notes,

            bank_name=invoice.user.bank.name,
            bank_blz=invoice.user.bank.blz,
            bank_owner=invoice.user.bank.owner,
            bank_iban=invoice.user.bank.iban

            )
    s_ = s.substitute(d) # type: ignore

    print(s_)
