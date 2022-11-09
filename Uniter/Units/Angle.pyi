from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Angle(Unit[__Q]): pass

class DEG(Angle[Angle]): pass
class RAD(Angle[Angle]): pass
