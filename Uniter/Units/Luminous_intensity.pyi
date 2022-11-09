from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Luminous_intensity(Unit[__Q]): pass

class LuminousIntensity(Luminous_intensity[Luminous_intensity]): pass
class MOL(Luminous_intensity[Luminous_intensity]): pass