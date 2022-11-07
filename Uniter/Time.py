from .Uniter import Unit, Unitor, Quantitor

@Quantitor("t")
class Time(Unit): pass

@Unitor("sec",1)
class SEC(Time): pass
@Unitor("min",60)
class MIN(Time): pass
@Unitor("h",60 ** 2)
class HR(Time): pass
@Unitor("d",60 ** 2 * 24)
class DAY(Time): pass
@Unitor("yr",60 ** 2 * 24 * 365.242199)
class YR(Time): pass