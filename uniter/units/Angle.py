from uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("°")
class Angle(Unit):
    def __conv__(self, unit):
        from math import degrees, radians
        DEGS = [DEG, MOA, SOA]
        if self.__class__ in DEGS and unit in DEGS:
            return super().__conv__(unit) # type: ignore
        elif self.__class__ in DEGS and unit is RAD:
            return radians(float(self[DEG]))
        elif self.__class__ is RAD and unit in DEGS:
            return float(DEG(degrees(float(self)))[unit])


@Unitor("°", 1)
class DEG(Angle): pass

@Unitor("′", 1/60)
class MOA(Angle): pass

@Unitor("″", 1/3600)
class SOA(Angle): pass

@Unitor("rad")
class RAD(Angle): pass
