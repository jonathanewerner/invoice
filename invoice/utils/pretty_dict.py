from pprint import pformat
import json

class PrettyDict:
    def __repr__(self):
        return pformat(self.__dict__)
