from .Exceptions import UnknownUnitError
from .units import *

def parse(expression, unit_mapping = None):
    import re
    from .Uniter import Unit
    MAP = {} if unit_mapping is None else {k:v.__name__ for k, v in unit_mapping.items()}
    for q in Unit.__subclasses__():
        for u in q.__subclasses__():
            MAP[u.symbol] = u.__name__
    for match in re.finditer(r"(\d+)(?: |)+(\w+)",expression):
        if match.group(2) not in MAP:
            raise UnknownUnitError(f"Unknown unit \"{match.group(2)}\"")
        expression = expression.replace(match.group(0),f"{MAP[match.group(2)]}({match.group(1)})")
    return eval(expression)