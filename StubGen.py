import importlib
import inspect
import os

if __name__ == '__main__':
    UNIT_PATH = r"Uniter\Units"
    for f in [p for p in os.listdir(UNIT_PATH) if p.endswith(".py") and p != "__init__.py"]:
        quantity = f[:-3]

        BASE = f"""
from typing import TypeVar
from Uniter.Uniter import Unit

__Q = TypeVar("__Q")

class {quantity}(Unit[__Q]): pass

""".lstrip()

        def pr(cls):
            return inspect.isclass(cls) and cls.__name__ not in [quantity, "Quantitor", "Unit", "Unitor"]


        for name, cls in inspect.getmembers(importlib.import_module(f"Uniter.Units.{quantity}"),pr):
            BASE += f"class {name}({quantity}[{quantity}]): pass\n"
        print(BASE)
        open(UNIT_PATH+rf"\{quantity}.pyi","w").write(BASE)