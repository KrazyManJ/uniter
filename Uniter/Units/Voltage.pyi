from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Voltage(Unit[__Q]): pass

class Volt(Voltage[Voltage]): pass
