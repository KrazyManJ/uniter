from uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("S")
class Area(Unit): pass

@Unitor("km^2", 10**6)
class KM_2(Area): pass

@Unitor("ha", 10**4)
class HA(Area): pass

@Unitor("are", 10**2)
class ARE(Area): pass

@Unitor("m^2", 1)
class M_2(Area): pass

@Unitor("m^2", 10**-2)
class DM_2(Area): pass

@Unitor("m^2", 10**-4)
class CM_2(Area): pass

@Unitor("m^2", 10**-6)
class MM_2(Area): pass