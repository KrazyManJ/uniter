from uniter.Uniter import Unit, __Q

class Time(Unit[__Q]): pass

class DAY(Time[Time]): pass

class HR(Time[Time]): pass

class MIN(Time[Time]): pass

class SEC(Time[Time]): pass

class YR(Time[Time]): pass

