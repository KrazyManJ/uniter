from typing import TypeVar, Generic, Type

__Q = TypeVar("__Q", bound=Unit)


class Unit(Generic[__Q]):
    __value: float
    __multiplier: float
    __symbol: str
    __unit_type: UnitType
    __sign: str

    @property
    def multiplier(self) -> float: ...

    @property
    def symbol(self) -> str: ...

    @property
    def unit_type(self) -> UnitType: ...

    @property
    def sign(self) -> UnitType: ...

    def convert_to(self, unit: type[__Q]) -> __Q: ...

    def in_bigger_unit(self, keep_unit_type: bool = ...) -> __Q: ...

    def in_smaller_unit(self, keep_unit_type: bool = ...) -> __Q: ...

    def in_default_unit(self) -> __Q: ...

    def is_convertable_to(self, unit: type[__Q]) -> bool: ...

    @classmethod
    def default_unit(cls) -> type[__Q]: ...

    @classmethod
    def units_by_category(cls, unit_type: UnitType) -> list[__Q]: ...

    @classmethod
    def bigger_unit(cls, keep_unit_type: bool = ...) -> Type[__Q]: ...

    @classmethod
    def smaller_unit(cls, keep_unit_type: bool = ...) -> Type[__Q]: ...

    @classmethod
    def is_biggest(cls, in_unit_type: bool = ...) -> bool: ...

    @classmethod
    def is_smallest(cls, in_unit_type: bool = ...) -> bool: ...

    def __init__(self, value: int | float) -> __Q: ...

    def __add__(self, other: __Q) -> __Q: ...

    def __sub__(self, other: __Q) -> __Q: ...

    def __getitem__(self, item: type[__Q]) -> __Q: ...

    def __mul__(self, other: int | float) -> __Q: ...

    def __rmul__(self, other: int | float) -> __Q: ...

    def __pow__(self, power: int | float, modulo=...) -> __Q: ...

    def __truediv__(self, other: int | float) -> __Q: ...

    def __floordiv__(self, other: int | float) -> __Q: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

    def __eq__(self, other: __Q) -> bool: ...

    def __ne__(self, other: __Q) -> bool: ...

    def __lt__(self, other: __Q) -> bool: ...

    def __le__(self, other: __Q) -> bool: ...

    def __gt__(self, other: __Q) -> bool: ...

    def __ge__(self, other: __Q) -> bool: ...


class Unitor:
    __mp: float
    __sy: str
    __ut: UnitType

    def __init__(self, symbol: str = ..., mp: int | float = ..., unit_type: UnitType = ...): ...

    def __call__(self): ...


class Quantitor:
    __s: str

    def __init__(self, sign: str): ...

    def __call__(self): ...


class UnitType:
    METRIC = ...
    IMPERIAL = ...
    ASTRONOMICAL = ...