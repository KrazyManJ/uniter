from .Uniter import Unit, Unitor

class Length(Unit): pass

# METRIC
@Unitor(10 ** 3)
class KM(Length): pass
@Unitor(1)
class M(Length): pass
@Unitor(10 ** -1)
class DM(Length): pass
@Unitor(10 ** -2)
class CM(Length): pass
@Unitor(10 ** -3)
class MM(Length): pass
@Unitor(10 ** -6)
class McM(Length): pass
@Unitor(10 ** -9)
class NM(Length): pass
@Unitor(10 ** -12)
class PM(Length): pass

# IMPERIAL
@Unitor(10 ** 3 * 1.609344)
class Mile(Length): pass
@Unitor(0.9144)
class Yard(Length): pass
@Unitor(10 ** -2 * 30.48)
class Foot(Length): pass
@Unitor(10 ** -2 * 2.54)
class Inch(Length): pass

# SPACE
@Unitor(10 ** 3 * 149597871)
class AstronomicalUnit(Length): pass
@Unitor(10 ** 15 * 9.4605284)
class LightYear(Length): pass