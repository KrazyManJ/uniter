from uniter.Uniter import Quantitor,Unit,Unitor


@Quantitor("p")
class Pressure(Unit): pass

@Unitor("Pa",1)
class PA(Pressure): pass