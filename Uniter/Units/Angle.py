from Uniter.Uniter import Unit, Unitor


class Angle(Unit):
    def __conv__(self, unit):
        from sympy import symbols, Eq, solve
        from math import pi
        deg, rad = symbols("deg rad")
        return solve(Eq(deg * pi / 180, rad).subs({DEG: deg, RAD: rad}[self.__class__], float(self)))[0]


@Unitor("°", 1)
class DEG(Angle): pass


@Unitor("rad", 0)
class RAD(Angle): pass
