from uniter.Uniter import Unit,Unitor,Quantitor

@Quantitor()
class Computer_Memory(Unit): pass

@Unitor("b",1)
class Bit(Computer_Memory): pass

@Unitor("B",8)
class Byte(Computer_Memory): pass

@Unitor("Kb",2 ** 10)
class Kb(Computer_Memory): pass
@Unitor("KB",8 * 2 ** 10)
class KB(Computer_Memory): pass

@Unitor("Mb",2 ** 20)
class Mb(Computer_Memory): pass
@Unitor("MB",8 * 2 ** 20)
class MB(Computer_Memory): pass

@Unitor("Gb",2 ** 30)
class Gb(Computer_Memory): pass
@Unitor("GB",8 * 2 ** 30)
class GB(Computer_Memory): pass

@Unitor("Tb",2 ** 40)
class Tb(Computer_Memory): pass
@Unitor("TB",8 * 2 ** 40)
class TB(Computer_Memory): pass

@Unitor("Pb",2 ** 50)
class Pb(Computer_Memory): pass
@Unitor("PB",8 * 2 ** 50)
class PB(Computer_Memory): pass

@Unitor("Eb",2 ** 60)
class Eb(Computer_Memory): pass
@Unitor("EB",8 * 2 ** 60)
class EB(Computer_Memory): pass

@Unitor("Zb",2 ** 70)
class Zb(Computer_Memory): pass
@Unitor("ZB",8 * 2 ** 70)
class ZB(Computer_Memory): pass

@Unitor("Yb",2 ** 80)
class Yb(Computer_Memory): pass
@Unitor("YB",8 * 2 ** 80)
class YB(Computer_Memory): pass