from uniter.Uniter import Unit, Unitor, Quantitor


@Quantitor("U")
class Voltage(Unit): pass


@Unitor("V", 1)
class Volt(Voltage): pass
