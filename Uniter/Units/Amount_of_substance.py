from Uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("n")
class Amount_of_substance(Unit): pass

@Unitor("mol",1)
class MOL(Amount_of_substance): pass