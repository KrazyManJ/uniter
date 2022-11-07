from .Uniter import Unit, Unitor, Quantitor

@Quantitor("A")
class Electric_Current(Unit): pass

@Unitor("A",1)
class A(Electric_Current): pass
@Unitor("mA",10 ** -3)
class MA(Electric_Current): pass