from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Temperature(Unit[__Q]): pass

class DEG_C(Temperature[Temperature]): pass
class DEG_F(Temperature[Temperature]): pass
class DEG_K(Temperature[Temperature]): pass
