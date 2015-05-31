from typing import *

import json
import os

from invoice.utils.dot_dict import DotDict

PathsDict = Dict[str, str]

class Config:
    def __init__(self, config_path: str) -> None:
        config = json.load(open(config_path))

        database_path = config['database_path']
        self.customers_path = os.path.join(database_path, 'customers.json')
        self.product_templates_path = os.path.join(database_path, 'products.json')

        self.exporters = config['exporters']
        self.user = config['user']
        self.startNr = config['startNr']
        self.notes = config['notes']




