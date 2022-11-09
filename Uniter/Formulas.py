def calc_average_speed(length=None, speed=None, time=None):
    from Uniter.Units import M, MS, SEC
    from sympy import symbols, Eq, solve
    s, v, t = symbols("s v t")
    formula, rtU, ct = Eq(s, v * t), None, 0
    for un, sym, ucls in [(length, s, M), (speed, v, MS), (time, t, SEC)]:
        if un is not None:
            formula = formula.subs(sym, float(un[un.default_unit()]))
            ct += 1
        else:
            rtU = ucls.default_unit()
    if ct < 2:
        raise ArithmeticError("Function must be passed at least with two arguments!")
    return rtU(solve(formula)[0].evalf())


def ohms_law(electric_current=None, voltage=None, resistance=None):
    from Uniter.Units import A, Volt, OHM
    from sympy import symbols, Eq, solve
    i, u, r = symbols("i u r")
    formula, rtU, ct = Eq(u / r, i), None, 0
    for un, sym, ucls in [(electric_current, i, A), (voltage, u, Volt), (resistance, r, OHM)]:
        if un is not None:
            formula = formula.subs(sym, float(un[un.default_unit()]))
            ct += 1
        else:
            rtU = ucls.default_unit()
    if ct < 2:
        raise ArithmeticError("Function must be passed at least with two arguments!")
    return rtU(solve(formula)[0].evalf())
