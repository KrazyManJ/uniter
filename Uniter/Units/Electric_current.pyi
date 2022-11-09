from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class Electric_current(Unit[__Q]): pass

class A(Electric_current[Electric_current]): pass
class Electric_Current(Electric_current[Electric_current]): pass
class MA(Electric_current[Electric_current]): pass
