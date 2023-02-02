from Uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("ρ")
class Density(Unit): pass

@Unitor("kg/m^3",1)
class KGM3(Density): pass

@Unitor("g/cm^3",10 ** -3)
class GCM3(Density): pass