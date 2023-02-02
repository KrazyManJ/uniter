from uniter.Uniter import Unit, __Q

class Energy(Unit[__Q]): pass

class GJ(Energy[Energy]): pass

class J(Energy[Energy]): pass

class KJ(Energy[Energy]): pass

class MJ(Energy[Energy]): pass

