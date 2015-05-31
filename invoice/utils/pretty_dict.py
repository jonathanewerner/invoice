from pprint import pformat
import json

class PrettyDict:
    def __repr__(self):
        # return
        return  '[{}] {}'.format(
                self.__class__.__name__,
                pformat(self.__dict__))
