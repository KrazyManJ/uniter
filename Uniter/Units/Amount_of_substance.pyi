from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Amount_of_substance(Unit[__Q]): pass

class MOL(Amount_of_substance[Amount_of_substance]): pass
