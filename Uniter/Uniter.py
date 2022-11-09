from enum import Enum
from typing import Type
from abc import ABC


class Unit(ABC):

    def __init__(self, value):
        if type(self) is Unit or type(self).__base__ is Unit:
            raise Exception(f"Cannot instatiate {type(self).__name__} class")
        self.__value = value

    @property
    def multiplier(self) -> float:
        return 0

    @property
    def symbol(self):
        return None

    @property
    def unit_type(self):
        return None

    @property
    def sign(self):
        return None

    def convert_to(self, unit):
        if type(unit) is not type or not isinstance(self, unit.__base__):
            sbs = self.__class__.__base__.__subclasses__()
            raise TypeError(
                f"Illegal conversion from {self.__class__.__base__.__name__} to {unit.__base__.__name__} available units to convert this object to: {', '.join([c.__name__ for c in sbs])}")

        return unit(self.__conv__(unit))

    @staticmethod
    def __clr_pd__(num: float):
        from re import sub
        return float(sub(r"(?<=\.)(0)(\1+)", "", str(num)))

    def __conv__(self, unit) -> float:
        return self.__value * self.multiplier / unit(0).multiplier

    def __calc__(self, other, oper_name, oper_symbol):
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        if self.__class__.__base__ is not other.__class__.__base__:
            raise TypeError(
                f"{oper_name} of non-equal units ({self.__class__.__base__.__name__} {oper_symbol} {other.__class__.__base__.__name__})")
        return other.__class__(op[oper_symbol](self.__conv__(other.__class__), other.__value))

    def __add__(self, other: "Unit"):
        return self.__calc__(other, "Addition", "+")

    def __sub__(self, other: "Unit"):
        return self.__calc__(other, "Subtraction", "-")

    def __getitem__(self, unit: Type["Unit"]):
        return self.convert_to(unit)

    def __mul__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Multiplication of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value *= other
        return self

    def __rmul__(self, other: int | float):
        return self.__mul__(other)

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise TypeError(f"Power of Unit with {power.__class__.__name__}, use int/float instead!")
        self.__value = pow(self.__value, power, modulo)
        return self

    def __truediv__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Division of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value /= other
        return self

    def __floordiv__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Division of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value //= other
        return self

    def __str__(self):
        return f"{float(self) if round(self.__value) != self.__value else int(self.__value)}{self.symbol}"

    def __repr__(self):
        return f"<{self.__class__.__base__.__name__}.{self.__class__.__name__} value={self.__value}>"

    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return self.__clr_pd__(float(self.__value))

    @classmethod
    def default_unit(cls):
        clss = (cls if cls.__base__ is Unit else cls.__base__).__subclasses__()
        return [c for c in clss if c.multiplier == 1][0]

    @classmethod
    def units_by_category(cls, unit):
        clss = (cls if cls.__base__ is Unit else cls.__base__).__subclasses__()
        return [c for c in clss if c.unit_type is unit]


class Unitor:

    def __init__(self, symbol="", mp=0, unit_type=None) -> None:
        self.__mp = mp
        self.__sy = symbol
        self.__ut = unit_type

    def __call__(self, cls):
        cls.multiplier = self.__mp
        cls.symbol = self.__sy
        cls.unit_type = self.__ut
        return cls


class Quantitor:

    def __init__(self, sign=None):
        self.__s = sign

    def __call__(self, cls):
        cls.sign = self.__s
        return cls


class UnitType(Enum):
    METRIC = "Metric"
    IMPERIAL = "Imperial"
    ASTRONOMICAL = "Astronomical"
