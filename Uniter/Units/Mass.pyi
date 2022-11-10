from Uniter.Uniter import Unit, __Q

class Mass(Unit[__Q]): pass

class G(Mass[Mass]): pass
class KG(Mass[Mass]): pass
class MG(Mass[Mass]): pass
class Ounce(Mass[Mass]): pass
class Pound(Mass[Mass]): pass
class Stone(Mass[Mass]): pass
class T(Mass[Mass]): pass
