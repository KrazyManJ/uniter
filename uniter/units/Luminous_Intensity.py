from uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("I")
class Luminous_Intensity(Unit): pass

@Unitor("cd",1)
class MOL(Luminous_Intensity): pass