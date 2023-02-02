<h1 align="center">Uniter</h1>

<p align="center">
Is python package, that can handle unit conversion with easy syntax.
Comes with ability to perform mathematical operations, and parsing 
from human-readable string.
</p>


<h2 align="center">Features</h2>

- [X] Unit [conversion](https://github.com/KrazyManJ/Uniter#conversion) between metric and imperial units
- [X] Mathematical operations between units:
  - [X] [Addition / Subtraction](https://github.com/KrazyManJ/Uniter#addition--subtraction)
  - [X] [Multiplication / Division / Floor division](https://github.com/KrazyManJ/Uniter#addition--subtraction)
  - [X] [Power](https://github.com/KrazyManJ/Uniter#addition--subtraction)
- [X] Logical (comparison) operations between units
- [X] [Parsing](https://github.com/KrazyManJ/Uniter#parsing-string-to-uniter-units) from humar-readable string
- [X] Ability to [add custom units](https://github.com/KrazyManJ/Uniter#custom-quantityunits)
- [ ] Adding formulas to create relation between units of different physics quantity (e.g. ohm's law)

<h2 align="center">Syntax</h2>

Here are some examples of features, including bad one to show you what you should
not do while using all of these aspects.

### Conversion

```py
from uniter.units import *

print(DM(80).convert_to(M))  # prints out 8m in Unit object
print(DM(80)[M])  # same thing but shorter syntax
print(DM(80)[KG])  # raises TypeError: Illegal conversion from Length to object 
```

### Addition / Subtraction

- Converts to last used unit in calculation

```py
from uniter.units import *

print(KM(50) + M(30))  # prints out 5030m in Unit object
print(KM(50) - M(30))  # prints out 4070m in Unit object
print(KM(50) - KG(30))  # raise TypeError: Subtraction of non-equal units (Length - Mass)
```

### Multiplication / Division / Floor division

- One of mul/div values needs to be int/float, not Unit type

```py
from uniter.units import *

print(KM(30) * 2)  # prints out 900km in Unit object
print(KM(30) * 80)  # prints out 2400km in Unit object
print(KM(30) / 6)  # prints out 5km in Unit object
print(KM(8) // 6)  # prints out 1km in Unit object
print(KM(8) * KG(6))  # TypeError: Multiplication of Unit with KG, use int/float instead!
```

### Power

```py
from uniter.units import *

print(KM(2) ** 16)  # prints out 65536km in Unit object
print(KM(2) ** KM(3))  # Power of Unit with KM, use int/float instead!
```

### Parsing string to Uniter units

```py
import uniter

print(uniter.parse("2m + 5km"))  # returns 5.002km in Unit object
```

### Custom quantity/units

Before creation of your custom units, you need to know that units are structurized
as inheritance of `Unit (Base Class)` -> `{Your name of unit here}` -> `{Name of unit}`.
This structure can basically handle that you cannot convert your unit to another incompatible
units.

#### Example of structuring Length and Mass quatities
```
Unit
├─── Length
│    ├─── KM
│    ├─── M
│    ├─── DM
│    ├─── CM
│    └─── ...
└─── Mass
     ├─── KG
     ├─── G
     ├─── MG
     └─── ...
```

Now for creation, for making basic units using prefixes like k (kilo), m (mili), M (mega) etc.
you can just use defined decorators in `Uniter.py` file like that:

```py
from uniter.Uniter import Unit, Unitor, Quantitor, UnitType


# In this example I am using keywords arguments to make it clearer for you

# Creates physics quantity of your name and sign
@Quantitor(sign="EQ")
class ExampleQuantity(Unit): pass


# Creating unit of out ExampleQuantity quantity:
#
# - Multiplier is difference between this unit and default one
#
# - IF MULTUPLIER IS 1 THEN THIS UNIT IS CONSIDERED AS DEFAULT
#
# - I've also defined unit type, this is not required, 
#   it is used to filter out specific type of units
@Unitor(symbol="fU", mp=1, unit_type=UnitType.METRIC)
class FirstU(ExampleQuantity): pass
```

#### Add custom calculation method

If you are trying to make quantity with different type of calculation,
than a regular units multiplication or division,
you can define it via `__conv__(self, unit)` method which returns `float`.

Here i will show you piece of my code from [Angle.py](uniter/units/Angle.py):

```python
from uniter.Uniter import Unit, Quantitor


@Quantitor("°")
class Angle(Unit):
  def __conv__(self, unit):
    from math import pi, degrees, radians
    DEGS = [DEG, MOA, SOA]
    if self.__class__ in DEGS and unit in DEGS:
      return super().__conv__(unit)  # type: ignore
    elif self.__class__ in DEGS and unit is RAD:
      return radians(float(self[DEG]))
    elif self.__class__ is RAD and unit in DEGS:
      return float(DEG(degrees(float(self)))[unit])


...  # other units
```