from .Uniter import Unit, Unitor

class Speed(Unit): pass

# METRIC
@Unitor(1)
class KMH(Speed): pass
@Unitor(3.6)
class MS(Speed): pass

# IMPERIAl
@Unitor(1.609344)
class MPH(Speed): pass

# SPACE
@Unitor(1.07925285 * (10 ** 9))
class LightSpeed(Speed): pass
