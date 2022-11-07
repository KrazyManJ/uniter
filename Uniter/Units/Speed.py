from Uniter.Uniter import Unit, Unitor, Quantitor

@Quantitor("v")
class Speed(Unit): pass

# METRIC
@Unitor("km/h",1)
class KMH(Speed): pass
@Unitor("m/s",3.6)
class MS(Speed): pass

# IMPERIAl
@Unitor("mph",1.609344)
class MPH(Speed): pass
@Unitor("fps",1.09728)
class FPS(Speed): pass

# SPACE
@Unitor("c",1.07925285 * (10 ** 9))
class LightSpeed(Speed): pass
