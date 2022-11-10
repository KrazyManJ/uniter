from .Units import *

def parse(expression: str):
    import re
    from .Uniter import Unit
    MAP = {}
    for q in Unit.__subclasses__():
        for u in q.__subclasses__():
            MAP[u.symbol] = u.__name__
    for match in re.finditer(r"(\d+)(?: |)+(\w+)",expression):
        if match.group(2) not in MAP:
            raise ValueError(f"Unknown unit \"{match.group(2)}\"")
        expression = expression.replace(match.group(0),f"{MAP[match.group(2)]}({match.group(1)})")
    return eval(expression)