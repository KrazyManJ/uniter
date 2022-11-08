<h1 align="center">Uniter</h1>


<h2 align="center">Syntax</h2>

### Conversion
```py
from Uniter.Units import *

print( DM(80).convert_to(M) )       # prints out 8,
print( DM(80)[M] )                  # same thing but shorter syntax
print( DM(80)[KG] )                 # raise error due to non equal quantities
```

### Addition / Subtraction

- Converts to last used unit in calculation

```py
from Uniter.Units import *

print( KM(50)+M(30) )               # prints out 5030m in Unit object
print( KM(50)-M(30) )               # prints out 4070m in Unit object
print( KM(50)-KG(30) )              # raise error due to non equal quantities
```

### Multiplication / Division

- One of mul/div values needs to be int/float, not Unit type

```py
from Uniter.Units import *

print ( KM(30) * 80 )               # prints out 2400KM
print ( KM(30) / 6 )                # prints out 5KM
```

### Parsing string to Uniter units
```py
import Uniter

print( Uniter.parse("2m + 5km") )   # returns 5.002km in Unit object
```