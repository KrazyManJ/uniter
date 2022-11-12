from Uniter.Uniter import Unit, __Q

class Resistance(Unit[__Q]): pass

class KOHM(Resistance[Resistance]): pass

class MOHM(Resistance[Resistance]): pass

class OHM(Resistance[Resistance]): pass

