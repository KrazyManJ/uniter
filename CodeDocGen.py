import importlib
import inspect
import os

if __name__ == '__main__':
    from Uniter.Uniter import Unit
    UNIT_PATH = r"Uniter\Units"
    for f in [p for p in os.listdir(UNIT_PATH) if p.endswith(".py") and p != "__init__.py"]:
        quantity = f[:-3]
        BASE = f"from Uniter.Uniter import Unit, __Q\n\nclass {quantity}(Unit[__Q]): pass\n\n".lstrip()
        def pr(clazz):
            return inspect.isclass(clazz) and clazz.__name__ not in [quantity, "Quantitor", "Unit", "Unitor", "UnitType", "QuantityType"]
        for name, cls in inspect.getmembers(importlib.import_module(f"Uniter.Units.{quantity}"),pr):
            BASE += f"class {name}({quantity}[{quantity}]): pass\n"
        print(BASE)
        open(UNIT_PATH+rf"\{quantity}.pyi","w").write(BASE)
    __INIT__ = ""
    for q in Unit.__subclasses__():
        __INIT__ += f"from .{q.__name__} import {', '.join([u.__name__ for u in q.__subclasses__()])}\n"
    open(UNIT_PATH+rf"\__init__.py", "w").write(__INIT__)