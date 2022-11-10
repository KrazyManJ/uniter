from enum import Enum

from .Exceptions import UnitInstatiateError, UnitConversionError, UnitInheritanceError, UnitQuantitorError, \
    UnitUnitorError, UnitArithmeticError, UnitBaseClassError
from .Util import classproperty

class Unit:

    def __init__(self, value):
        if type(self) is Unit:
            raise UnitInstatiateError("Cannot instantiate Unit base class")
        if type(self).__base__ is Unit:
            raise UnitInstatiateError(f"Cannot instatiate {type(self).__name__} quantity class")
        if type(self).__base__.__base__ is not Unit:
            raise UnitInstatiateError(f"Cannot instatiate {type(self).__name__} class that is not child of quantity class")
        if self.__class__.__dict__.__len__() == 2:
            self.__class__.__multiplier = 0
            self.__class__.__symbol = ""
            self.__class__.__unit_type = None
            self.__class__.__sign = ""
            self.__class__.__quantity_type = QuantityType.MULTIPLIER
        self.__value = value


    @classproperty
    def multiplier(self) -> float: return self.__multiplier

    @classproperty
    def symbol(self): return self.__symbol

    @classproperty
    def unit_type(self): return self.__unit_type

    @classproperty
    def sign(self): return self.__sign

    @classproperty
    def quantity_type(self): return self.__quantity_type

    def convert_to(self, unit):
        if type(self) is unit:
            return self
        if type(unit) is not type or not isinstance(self, unit.__base__):
            sbs = self.__class__.__base__.__subclasses__()
            cvt = unit.__base__.__name__ if type(unit) is type else type(unit).__name__
            raise UnitConversionError(
                f"Illegal conversion from {self.__class__.__base__.__name__} to {cvt} available units to convert this object to: {', '.join([c.__name__ for c in sbs])}")

        return unit(self.__conv__(unit))  # type: ignore

    def in_bigger_unit(self, keep_unit_type=True):
        return self[self.__class__.bigger_unit(keep_unit_type)]

    def in_smaller_unit(self, keep_unit_type=True):
        return self[self.__class__.smaller_unit(keep_unit_type)]

    @classmethod
    def bigger_unit(cls, keep_unit_type=True):
        if cls.quantity_type is QuantityType.CUSTOM_CALCULATION: return cls
        units, index = cls.__unit_size_map__(keep_unit_type, "bigger unit")  # type: ignore
        return units[min(index + 1, units.__len__() - 1)]

    @classmethod
    def smaller_unit(cls, keep_unit_type=True):
        if cls.quantity_type is QuantityType.CUSTOM_CALCULATION: return cls
        units, index = cls.__unit_size_map__(keep_unit_type, "smaller unit")  # type: ignore
        return units[max(index - 1, 0)]

    @classmethod
    def is_biggest(cls, in_unit_type=True):
        if cls.quantity_type is QuantityType.CUSTOM_CALCULATION: return False
        units, index = cls.__unit_size_map__(in_unit_type, "if unit is the biggest")  # type: ignore
        return index == units.__len__() - 1

    @classmethod
    def is_smallest(cls, in_unit_type=True):
        if cls.quantity_type is QuantityType.CUSTOM_CALCULATION: return False
        units, index = cls.__unit_size_map__(in_unit_type, "if unit is the smallest")  # type: ignore
        return index == 0

    @classmethod
    def __unit_size_map__(cls, keep_unit_type, operation_name):
        if cls is Unit or cls.__base__ is Unit:
            raise UnitBaseClassError(f"Cannot get {operation_name} from {'Unit base class' if cls is Unit else f'{cls.__name__} quantity class'}")
        if cls.__base__.__base__ is not Unit:
            raise UnitInheritanceError(f"Cannot get {operation_name} from {cls.__name__} class because it is not in correct inheritance order (Unit -> QuantityName -> {cls.__name__})")
        units = sorted(cls.units_by_category(cls.unit_type) if keep_unit_type else cls.__base__.__subclasses__(), # type: ignore
                       key=lambda o: o.multiplier)
        index = units.index(cls)
        return units, index

    @staticmethod
    def __clr_pd__(num):
        from re import sub
        return float(sub(r"(\.\d+?)(0)(\2+)$", "\1", str(num)))

    def __conv__(self, unit):
        return self.__value * self.__multiplier / unit(0).multiplier

    def __calc__(self, other, oper_name, oper_symbol):
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        if self.__class__.__base__ is not other.__class__.__base__:
            raise UnitArithmeticError(
                f"{oper_name} of non-equal units ({self.__class__.__base__.__name__} {oper_symbol} {other.__class__.__base__.__name__})")
        return other.__class__(op[oper_symbol](self.__conv__(other.__class__), other.__value))

    def __add__(self, other):
        return self.__calc__(other, "Addition", "+")  # type: ignore

    def __sub__(self, other):
        return self.__calc__(other, "Subtraction", "-")  # type: ignore

    def __getitem__(self, unit):
        return self.convert_to(unit)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise UnitArithmeticError(f"Multiplication of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise UnitArithmeticError(f"Power of Unit with {power.__class__.__name__}, use int/float instead!")
        self.__value = pow(self.__value, power, modulo)
        return self

    def __truediv__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise UnitArithmeticError(f"Division of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value /= other
        return self

    def __floordiv__(self, other: int | float):
        if not isinstance(other, (int, float)):
            raise UnitArithmeticError(f"Division of Unit with {other.__class__.__name__}, use int/float instead!")
        self.__value //= other
        return self

    def __str__(self):
        return f"{float(self) if round(self.__value) != self.__value else int(self.__value)}{self.symbol}"

    def __repr__(self):
        return f"<{self.__class__.__base__.__name__}.{self.__class__.__name__} value={self.__value}>"

    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return self.__clr_pd__(float(self.__value))  # type: ignore

    @classmethod
    def default_unit(cls):
        clss = (cls if cls.__base__ is Unit else cls.__base__).__subclasses__()
        return [c for c in clss if c.multiplier == 1][0]  # type: ignore

    @classmethod
    def units_by_category(cls, unit):
        clss = (cls if cls.__base__ is Unit else cls.__base__).__subclasses__()
        return [c for c in clss if c.unit_type is unit]


class UnitType(Enum):
    METRIC = 0
    IMPERIAL = 1
    ASTRONOMICAL = 2


class Unitor:

    def __init__(self, symbol="", mp=0, unit_type=None) -> None:
        self.__mp = mp
        self.__sy = symbol
        self.__ut = unit_type

    def __call__(self, cls: type):
        if type(cls) is not type:
            raise UnitUnitorError("Unitor cannot be applied on function")
        if cls.__base__.__base__ is not Unit:
            raise UnitUnitorError("Unitor class is not extending Quantity class")
        cls._Unit__multiplier = self.__mp
        cls._Unit__symbol = self.__sy
        cls._Unit__unit_type = self.__ut
        return cls


class QuantityType(Enum):
    MULTIPLIER = 0
    CUSTOM_CALCULATION = 1


class Quantitor:

    def __init__(self, sign=None, quantity_type=QuantityType.MULTIPLIER):
        self.__s = sign
        self.__qt = quantity_type

    def __call__(self, cls):
        if type(cls) is not type:
            raise UnitQuantitorError("Quantitior cannot be applied on function")
        if cls.__base__ is not Unit:
            raise UnitQuantitorError("Quantitor class is not extending Unit class")
        cls._Unit__sign = self.__s
        cls._Unit__quantity_type = self.__qt
        return cls
