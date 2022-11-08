from Uniter.Uniter import Unit, Unitor, Quantitor


@Quantitor("R")
class Resistance(Unit): pass


@Unitor("Ω", 1)
class OHM(Resistance): pass


@Unitor("kΩ", 10 ** 3)
class KOHM(Resistance): pass


@Unitor("MΩ", 10 ** 6)
class MOHM(Resistance): pass
