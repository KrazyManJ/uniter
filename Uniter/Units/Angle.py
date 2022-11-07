from Uniter.Uniter import Unit, Unitor


class Angle(Unit):
    def __conv__(self, unit):
        from math import degrees, radians
        if self.__class__ is unit:
            return self.__int__()
        MAP = { DEG: degrees, RAD: radians }
        return MAP[unit](self.__int__())
    pass

@Unitor("°",1)
class DEG(Angle): pass

@Unitor("rad",0)
class RAD(Angle): pass

