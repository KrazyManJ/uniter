from .Uniter import Unit, Unitor, UnitType, Quantitor

@Quantitor("l")
class Length(Unit): pass

# METRIC
@Unitor("km",10 ** 3, UnitType.METRIC)
class KM(Length): pass
@Unitor("m",1, UnitType.METRIC)
class M(Length): pass
@Unitor("dm",10 ** -1, UnitType.METRIC)
class DM(Length): pass
@Unitor("cm",10 ** -2, UnitType.METRIC)
class CM(Length): pass
@Unitor("mm",10 ** -3, UnitType.METRIC)
class MM(Length): pass
@Unitor("µm",10 ** -6, UnitType.METRIC)
class McM(Length): pass
@Unitor("nm",10 ** -9, UnitType.METRIC)
class NM(Length): pass
@Unitor("pm",10 ** -12, UnitType.METRIC)
class PM(Length): pass

# IMPERIAL
@Unitor("mi",10 ** 3 * 1.609344, UnitType.IMPERIAL)
class Mile(Length): pass
@Unitor("yd",0.9144, UnitType.IMPERIAL)
class Yard(Length): pass
@Unitor("ft",10 ** -2 * 30.48, UnitType.IMPERIAL)
class Foot(Length): pass
@Unitor("in",10 ** -2 * 2.54, UnitType.IMPERIAL)
class Inch(Length): pass

# SPACE
@Unitor("au",10 ** 3 * 149597871, UnitType.ASTRONOMICAL)
class AstronomicalUnit(Length): pass
@Unitor("ly",10 ** 15 * 9.4605284, UnitType.ASTRONOMICAL)
class LightYear(Length): pass