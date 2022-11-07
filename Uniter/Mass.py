from .Uniter import Unit, Unitor, UnitType, Quantitor

@Quantitor("m")
class Mass(Unit): pass

# METRIC
@Unitor("t",10 ** 6, UnitType.METRIC)
class T(Mass): pass
@Unitor("kg",10 ** 3, UnitType.METRIC)
class KG(Mass): pass
@Unitor("g",1, UnitType.METRIC)
class G(Mass): pass
@Unitor("mg",10 ** -3, UnitType.METRIC)
class MG(Mass): pass

# IMPERIAL
@Unitor("lb", 10 ** 3 * 0.45359237, UnitType.IMPERIAL)
class Pound(Mass): pass
@Unitor("lb", 28.349523125, UnitType.IMPERIAL)
class Ounce(Mass): pass
@Unitor("st", 10 ** 3 * 6.35029318, UnitType.IMPERIAL)
class Stone(Mass): pass