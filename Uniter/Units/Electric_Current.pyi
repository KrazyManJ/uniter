from Uniter.Uniter import Unit, __Q

class Electric_Current(Unit[__Q]): pass

class A(Electric_Current[Electric_Current]): pass
class MA(Electric_Current[Electric_Current]): pass
