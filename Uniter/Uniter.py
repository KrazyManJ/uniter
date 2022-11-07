class Unit(object):

    def __init__(self, value): self.__value = value

    @property
    def multiplier(self) -> float: return 1

    def convert_to(self, unit: type["Unit"]):
        if type(unit) is not type or not isinstance(self, unit.__base__):
            sbs = self.__class__.__base__.__subclasses__()
            raise TypeError(f"Is not unit to convert to, use unit class instead (Full list of them: {', '.join([c.__name__ for c in sbs])})")

        return unit(self.__conv__(unit))

    def __conv__(self, unit: type["Unit"]): return self.__value * self.multiplier / unit(0).multiplier

    def __calc__(self, other, oper_name, oper_symbol):
        op = {'+': lambda x, y: x + y,'-': lambda x, y: x - y}
        if self.__class__.__base__ is not other.__class__.__base__:
            raise TypeError(f"{oper_name} of non equal units ({self.__class__.__base__.__name__} {oper_symbol} {other.__class__.__base__.__name__})")
        return other.__class__(op[oper_symbol](self.__conv__(other.__class__),other.__value))

    def __add__(self, other: "Unit"):
        return self.__calc__(other,"Addition","+")

    def __sub__(self, other: "Unit"):
        return self.__calc__(other,"Subtraction","-")

    def __getitem__(self, unit: type["Unit"]):
        return self.convert_to(unit)

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return self.__class__(self.__value*other)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.__value * other)

    def __div__(self, other):
        if isinstance(other,(int,float)):
            return self.__class__(self.__value/other)

    def __rdiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.__value/other)

    def __str__(self):
        return f"<{self.__class__.__base__.__name__}.{self.__class__.__name__} value={self.__value}>"

    def __int__(self):
        return self.__value

class Unitor:

    def __init__(self,mp) -> None:
        self.__mp = mp

    def __call__(self, cls):
        cls.multiplier = self.__mp
        return cls