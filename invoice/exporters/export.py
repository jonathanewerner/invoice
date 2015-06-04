from typing import *
import sys

# it seems that i cant import the module, set it as value in the mappings
# dict and then call run on it. so i import the functions themselves
from invoice.exporters.pdf import run as run_pdf

from invoice.domain.invoice import Invoice

def export(invoice: Invoice, exporter_name: str) -> None:
    mappings = {
        'pdf': run_pdf
    }

    if not exporter_name in mappings:
        raise ValueError('exporter name not in dictionary.')
        sys.exit(1)

    export_func = mappings[exporter_name]
    export_func(invoice)
