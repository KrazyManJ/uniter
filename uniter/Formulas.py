from uniter.Uniter import Unit
from uniter.units import *
from uniter.Exceptions import UnitFormulaParameterError
from sympy import Eq, solve
from sympy.core.symbol import Symbol


def __form__(eq, unit_map, **values):
    decl_Size = {k: v for k, v in values.items() if v is not None}.__len__()
    if decl_Size < values.__len__() - 1:
        raise UnitFormulaParameterError("You did not provide enough parameters to calculation!")
    if decl_Size == values.__len__():
        raise UnitFormulaParameterError("You provide all arguments, and there is nothing to calculate!")
    for s in eq.free_symbols:
        val, un = values[str(s)], unit_map[str(s)]
        if val is not None:
            if not isinstance(val, Unit):
                raise UnitFormulaParameterError(
                    f"Expected unit of {un.__base__.__name__}, got {type(val).__name__} instead")
            if not val.is_convertable_to(un):
                raise UnitFormulaParameterError(
                    f"Expected unit of {un.__base__.__name__}, got unit of {type(val).__base__.__name__} instead")
            eq = eq.subs(s, float(val[un]))
    runit, res = list(solve(eq, dict=True)[0].items())[0]
    return unit_map[str(runit)](res)


def ohms_law(electric_current = None, voltage = None, resistance = None):
    return __form__(Eq(Symbol("i"), Symbol("u") / Symbol("r")), {"r": OHM, "u": Volt, "i": A}, i=electric_current,
                    u=voltage, r=resistance)


def average_speed(distance = None, speed = None, time = None):
    return __form__(Eq(Symbol("s"), Symbol("v") * Symbol("t")), {"s": M, "v": MS, "t": SEC}, s=distance, v=speed,
                    t=time)


def cylinder_volume(radius = None, height = None, volume = None):
    from math import pi
    return __form__(Eq(pi * Symbol("r") ** 2 * Symbol("v"), Symbol("V")), {"r": M, "v": M, "V": M_3}, r=radius,
                    v=height, V=volume)


def cylinder_surface(radius = None, height = None, surface = None):
    from math import pi
    return __form__(Eq(2 * pi * Symbol("r") * (Symbol("r") + Symbol("v")), Symbol("S")), {"r": M, "v": M, "S": M_2},
                    r=radius, v=height, S=surface)


def sphere_volume(radius = None, volume = None):
    from math import pi
    return __form__(Eq(4 / 3 * pi * Symbol("r") ** 3, Symbol("V")), {"r": M, "V": M_3}, r=radius, V=volume)


def sphere_surface(radius = None, surface = None):
    from math import pi
    return __form__(Eq(4 * pi * Symbol("r") ** 2), {"r": M, "S": M_2}, r=radius, S=surface)


def density_formula(mass = None, volume = None, density = None):
    return __form__(Eq(Symbol("R"), Symbol("m") / Symbol("V")), {"R": KGM_3, "m": KG, "V": M_3}, m=mass, V=volume,
                    R=density)
