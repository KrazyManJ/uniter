<h1 align="center">Uniter</h1>

<p align="center">
Is python package, that can handle unit conversion with easy syntax.
Comes with ability to perform mathematical operations, and parsing 
from human-readable string.
</p>


<h2 align="center">Features</h2>

- [X] Unit conversion between metric and imperial units
- [X] Mathematical operations between them (more described in [Syntax](https://github.com/KrazyManJ/Uniter#syntax))
  - [X] Addition / Subtraction
  - [X] Multiplication / Division / Floor division
  - [X] Power
- [X] Parsing from humar-readable string
- [ ] Adding formulas to create relation between units of different physics quantity (e.g. ohm's law)

<h2 align="center">Syntax</h2>

### Conversion
```py
from Uniter.Units import *

print( DM(80).convert_to(M) )       # prints out 8,
print( DM(80)[M] )                  # same thing but shorter syntax
print( DM(80)[KG] )                 # raises TypeError: Illegal conversion from Length to object 
```

### Addition / Subtraction

- Converts to last used unit in calculation

```py
from Uniter.Units import *

print( KM(50)+M(30) )               # prints out 5030m in Unit object
print( KM(50)-M(30) )               # prints out 4070m in Unit object
print( KM(50)-KG(30) )              # raise TypeError: Subtraction of non-equal units (Length - Mass)
```

### Multiplication / Division

- One of mul/div values needs to be int/float, not Unit type

```py
from Uniter.Units import *

print ( KM(30) * 80 )               # prints out 2400km in Unit object
print ( KM(30) / 6 )                # prints out 5km in Unit object
print ( KM(8) // 6 )                # prints out 1km in Unit object
print ( KM(8) * KG(6) )             # TypeError: Multiplication of Unit with KG, use int/float instead!
```

### Power
```py
from Uniter.Units import *

print ( KM(2) ** 16 )               # prints out 65536km in Unit object
print ( KM(2) ** KM(3) )            # Power of Unit with KM, use int/float instead!
```

### Parsing string to Uniter units
```py
import Uniter

print( Uniter.parse("2m + 5km") )   # returns 5.002km in Unit object
```

## Custom quantity/units

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
from Uniter.Uniter import Unit,Unitor,Quantitor,UnitType

# In this example i am using keywords arguments to make it clearer for you

# Creates physics quantity of your name and sign
@Quantitor(sign="EQ")
class ExampleQuantity(Unit): pass

# Creating unit of out ExampleQuantity quantity:
#
# - Multiplier is difference between this unit and default one
#
# - IF MULTUPLIER IS 1 THEN THIS UNIT IS DEFAULT
#
# - I've also defined unit type, this is not required, 
#   it is used to filter out specific type of units
@Unitor(symbol="fU",mp=1,unit_type=UnitType.METRIC)
class FirstU(ExampleQuantity): pass
```

If you have any ideas of other units, and you want to include them in this package, contact me 😉 !