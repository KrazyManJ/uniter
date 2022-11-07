from .Uniter import Unit, Unitor

class Mass(Unit):
    pass

@Unitor(10 ** 3)
class KG(Mass): pass
@Unitor(1)
class G(Mass): pass
@Unitor(10 ** -3)
class MG(Mass): pass