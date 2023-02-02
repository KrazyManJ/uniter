import importlib
import inspect
from typing import Any
from uniter.Uniter import Unit
import os

UNIT_PATH = r"uniter/units"

def units_stubs():

    for f in [p for p in os.listdir(UNIT_PATH) if p.endswith(".py") and p != "__init__.py"]:
        quantity = f[:-3]
        BASE = f"from uniter.Uniter import Unit, __Q\n\nclass {quantity}(Unit[__Q]): pass\n\n".lstrip()
        def pr(clazz):
            return inspect.isclass(clazz) and clazz.__name__ not in [quantity, "Quantitor", "Unit", "Unitor",
                                                                     "UnitType"]
        for name, cls in inspect.getmembers(importlib.import_module(f"uniter.units.{quantity}"), pr):
            BASE += f"class {name}({quantity}[{quantity}]): pass\n\n"
        open(UNIT_PATH + rf"\{quantity}.pyi", "w").write(BASE)

def unit_init():
    init = ""
    for q in Unit.__subclasses__():
        init += f"from .{q.__name__} import {q.__name__}, {', '.join([u.__name__ for u in q.__subclasses__()])}\n"
    open(UNIT_PATH + rf"\__init__.py", "w").write(init)

def formulas_stub():
    stub = "from typing import overload\nfrom uniter.Uniter import Unit\nfrom uniter.units import *\n\n"
    mod = importlib.import_module(f"uniter.Formulas")
    for inspectData in inspect.getmembers(mod, lambda x: inspect.isfunction(x) and mod.__name__ is x.__module__ and x.__name__ not in ["__form__"]):
        name,fct = inspectData
        args = {}
        dt = inspect.getfullargspec(fct)
        for arg in dt.args:
            args[arg] = dt.annotations.get(arg, Any).__name__
        for i in range(len(args)):
            tA = args.copy()
            tA[list(tA.keys())[i]] = None
            stub += f"@overload\ndef {name}({', '.join(f'{k}: {v} = ...' for k, v in tA.items())}) -> {args[list(args.keys())[i]]}: ...\n\n"
        stub += f"def {name}({', '.join(f'{k}: {v} | None = ...' for k, v in args.items())}) -> Unit: ...\n\n"
    open("uniter/Formulas.pyi", "w").write(stub.rstrip())

if __name__ == '__main__':
    units_stubs()
    unit_init()
    formulas_stub()

