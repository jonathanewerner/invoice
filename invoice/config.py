from typing import *
PathsDict = Dict[str, str]

class Config:
    def __init__(self, paths: PathsDict) -> None:
        self.customers_path = paths['customers']


