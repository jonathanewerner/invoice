from typing import *
import json
PathsDict = Dict[str, str]

class Config:
    def __init__(self, paths: PathsDict) -> None:
        self.customers_path = paths['customers_path']
        config = json.load(open(paths['config_path']))
        self.exporters = config['exporters']
        self.user = config['user']




