from uniter.Uniter import Unit, Quantitor, Unitor

@Quantitor("W")
class Energy(Unit): pass

@Unitor("J", 1)
class J(Energy): pass

@Unitor("kJ", 10 ** 3)
class KJ(Energy): pass

@Unitor("MJ", 10 ** 6)
class MJ(Energy): pass

@Unitor("GJ", 10 ** 9)
class GJ(Energy): pass