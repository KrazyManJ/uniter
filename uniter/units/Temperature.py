from uniter.Uniter import Unit, Unitor, Quantitor


@Quantitor("T")
class Temperature(Unit):
    def __conv__(self, unit):
        from sympy import symbols, Eq, solve
        C, K, F = symbols("C K F")
        SYM = {DEG_C: C, DEG_K: K, DEG_F: F}
        EQ = {(DEG_C, DEG_K): Eq(C + 273.15, K), (DEG_C, DEG_F): Eq(9 / 5 * C + 32, F),
              (DEG_K, DEG_F): Eq(9 / 5 * K - 459.67, F)}

        return \
        solve(EQ[[k for k in EQ.keys() if set(k) == {self.__class__, unit}][0]].subs(SYM[self.__class__], float(self)))[  # type: ignore
            0]


@Unitor("°C", 1)
class DEG_C(Temperature): pass


@Unitor("°F")
class DEG_F(Temperature): pass


@Unitor("°K")
class DEG_K(Temperature): pass
