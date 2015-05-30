from pprint import pformat

class PrettyDict:
    def __str__(self):
        return pformat(self.__dict__)
