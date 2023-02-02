from uniter.Uniter import Unit, Quantitor, Unitor

@Quantitor("W")
class Work(Unit): pass

@Unitor("J", 1)
class J(Work): pass

@Unitor("kJ", 10 ** 3)
class KJ(Work): pass

@Unitor("MJ", 10 ** 6)
class MJ(Work): pass

@Unitor("GJ", 10 ** 9)
class GJ(Work): pass