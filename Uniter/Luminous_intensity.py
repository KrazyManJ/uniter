from .Uniter import Unit, Unitor, Quantitor

@Quantitor("I")
class LuminousIntensity(Unit): pass

@Unitor("cd",1)
class MOL(LuminousIntensity): pass