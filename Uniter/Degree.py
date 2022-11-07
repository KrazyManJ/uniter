
from .Uniter import Unit


class Degree(Unit):
    def __conv__(self, unit: type["Unit"]):
        from math import degrees, radians
        if self.__class__ is unit:
            return self.__int__()
        MAP = { DEG: degrees, RAD: radians }
        return MAP[unit](self.__int__())

    pass


class DEG(Degree): pass


class RAD(Degree): pass
