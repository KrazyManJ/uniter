from uniter.Uniter import Unit,Unitor,Quantitor

@Quantitor("P")
class Power(Unit): pass

@Unitor("W",1)
class W(Power): pass