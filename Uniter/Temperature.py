from .Uniter import Unit


class Temperature(Unit):
    def __conv__(self, unit):
        if self.__class__ is unit:
            return self.__int__()
        MAP: dict = {
            (DEG_C, DEG_K): lambda C: C - 273.15,
            (DEG_C, DEG_F): lambda C: 9 / 5 * C + 32,
            (DEG_F, DEG_C): lambda F: 5 / 9 * (F - 32),
            (DEG_K, DEG_C): lambda K: K + 273.15,
            (DEG_F, DEG_K): lambda F: (5 / 9 * (F - 32)) - 273.15,
            (DEG_K, DEG_F): lambda K: 9 / 5 * K + 273.15 + 32
        }
        return MAP[self.__class__, unit](self.__int__())

class DEG_C(Temperature): pass
class DEG_F(Temperature): pass
class DEG_K(Temperature): pass
