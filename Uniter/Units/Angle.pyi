from Uniter.Uniter import Unit, __Q

class Angle(Unit[__Q]): pass

class DEG(Angle[Angle]): pass
class RAD(Angle[Angle]): pass
