from Uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("V")
class Volume(Unit): pass

@Unitor("m^3", 10**3)
class M_3(Volume): pass

@Unitor("hL", 10**2)
class HL(Volume): pass

@Unitor("L", 1)
class L(Volume): pass

@Unitor("dm^3", 1)
class DM_3(Volume): pass

@Unitor("dL", 10**-1)
class DL(Volume): pass

@Unitor("cL", 10**-2)
class CL(Volume): pass

@Unitor("mL", 10**-3)
class ML(Volume): pass

@Unitor("cm^3", 10**-3)
class CM_3(Volume): pass