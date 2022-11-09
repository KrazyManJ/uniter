from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Length(Unit[__Q]): pass

class AstronomicalUnit(Length[Length]): pass
class CM(Length[Length]): pass
class DM(Length[Length]): pass
class Foot(Length[Length]): pass
class Inch(Length[Length]): pass
class KM(Length[Length]): pass
class LightYear(Length[Length]): pass
class M(Length[Length]): pass
class MM(Length[Length]): pass
class McM(Length[Length]): pass
class Mile(Length[Length]): pass
class NM(Length[Length]): pass
class PM(Length[Length]): pass
class UnitType(Length[Length]): pass
class Yard(Length[Length]): pass
