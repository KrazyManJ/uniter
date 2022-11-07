from .Uniter import Unit, Unitor, Quantitor

@Quantitor("n")
class AmountOfSubstance(Unit): pass

@Unitor("mol",1)
class MOL(AmountOfSubstance): pass