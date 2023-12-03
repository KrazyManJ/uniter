from uniter.Uniter import Unit, Unitor, Quantitor


@Quantitor()
class Computer_Memory(Unit): pass


@Unitor("b", 1)
class Bit(Computer_Memory): pass

@Unitor("B", 8)
class Byte(Computer_Memory): pass


@Unitor("Kib", 2 ** 10)
class Kib(Computer_Memory): pass
@Unitor("KiB", 8 * 2 ** 10)
class KiB(Computer_Memory): pass
@Unitor("Kb", 10 ** 3)
class Kb(Computer_Memory): pass
@Unitor("KB", 8 * 10 ** 3)
class KB(Computer_Memory): pass


@Unitor("Mib", 2 ** 20)
class Mib(Computer_Memory): pass
@Unitor("MiB", 8 * 2 ** 20)
class MiB(Computer_Memory): pass
@Unitor("Mb", 10 ** 6)
class Mb(Computer_Memory): pass
@Unitor("MB", 8 * 10 ** 6)
class MB(Computer_Memory): pass


@Unitor("Gib", 2 ** 30)
class Gib(Computer_Memory): pass
@Unitor("GiB", 8 * 2 ** 30)
class GiB(Computer_Memory): pass
@Unitor("Gb", 10 ** 9)
class Gb(Computer_Memory): pass
@Unitor("GB", 8 * 10 ** 9)
class GB(Computer_Memory): pass


@Unitor("Tib", 2 ** 40)
class Tib(Computer_Memory): pass
@Unitor("TiB", 8 * 2 ** 40)
class TiB(Computer_Memory): pass
@Unitor("Tb", 10 ** 12)
class Tb(Computer_Memory): pass
@Unitor("TB", 8 * 10 ** 12)
class TB(Computer_Memory): pass


@Unitor("Pib", 2 ** 50)
class Pib(Computer_Memory): pass
@Unitor("PiB", 8 * 2 ** 50)
class PiB(Computer_Memory): pass
@Unitor("Pb", 10 ** 15)
class Pb(Computer_Memory): pass
@Unitor("PB", 8 * 10 ** 15)
class PB(Computer_Memory): pass


@Unitor("Eib", 2 ** 60)
class Eib(Computer_Memory): pass
@Unitor("EiB", 8 * 2 ** 60)
class EiB(Computer_Memory): pass
@Unitor("Eb", 10 ** 18)
class Eb(Computer_Memory): pass
@Unitor("EB", 8 * 10 ** 18)
class EB(Computer_Memory): pass


@Unitor("Zib", 2 ** 70)
class Zib(Computer_Memory): pass
@Unitor("ZiB", 8 * 2 ** 70)
class ZiB(Computer_Memory): pass
@Unitor("Zb", 10 ** 21)
class Zb(Computer_Memory): pass
@Unitor("ZB", 8 * 10 ** 21)
class ZB(Computer_Memory): pass


@Unitor("Yib", 2 ** 80)
class Yib(Computer_Memory): pass
@Unitor("YiB", 8 * 2 ** 80)
class YiB(Computer_Memory): pass
@Unitor("Yb", 10 ** 24)
class Yb(Computer_Memory): pass
@Unitor("YB", 8 * 10 ** 24)
class YB(Computer_Memory): pass