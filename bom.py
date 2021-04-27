from ms_sqlserver import DbAccessor


class GetBoms:
    def akira(self):
        print()


class Bom:

    def __init__(self, partsnumber, partsname):
        self.__partsnumber = partsnumber
        self.__partsname = partsname

    @property
    def partsnumber(self):
        return self.__partsnumber

    @property
    def partsname(self):
        return self.__partsname
