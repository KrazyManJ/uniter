from Uniter.Uniter import Unit
from Uniter.Units.Electric_Current import Electric_Current
from Uniter.Units.Length import Length
from Uniter.Units.Resistance import Resistance
from Uniter.Units.Speed import Speed
from Uniter.Units.Time import Time
from Uniter.Units.Voltage import Voltage
from Uniter.Units.Volume import Volume

from typing import overload


@overload
def ohms_law(electric_current: Electric_Current = ..., voltage: Voltage = ...,
             resistance: None = ...) -> Resistance: ...
@overload
def ohms_law(electric_current: Electric_Current = ..., voltage: None = ...,
             resistance: Resistance = ...) -> Voltage: ...
@overload
def ohms_law(electric_current: None = ..., voltage: Voltage = ...,
             resistance: Resistance = ...) -> Electric_Current: ...
def ohms_law(electric_current: Electric_Current | None = ..., voltage: Voltage | None = ...,
             resistance: Resistance | None = ...) -> Unit: ...


@overload
def average_speed(distance: Length = ..., speed: Speed = ..., time: None = ...) -> Time: ...

@overload
def average_speed(distance: Length = ..., speed: None = ..., time: Time = ...) -> Speed: ...

@overload
def average_speed(distance: None = ..., speed: Speed = ..., time: Time = ...) -> Length: ...

def average_speed(distance: Length = ..., speed: Speed = ..., time: Time = ...) -> Unit: ...


@overload
def cylinder_surface(radius: Length = ..., height: Length = ..., volume: None = ...) -> Volume: ...

@overload
def cylinder_surface(radius: Length = ..., height: None = ..., volume: Volume = ...) -> Length: ...

@overload
def cylinder_surface(radius: None = ..., height: Length = ..., volume: Volume = ...) -> Length: ...

def cylinder_surface(radius: Length = ..., height: Length = ..., volume: Volume = ...) -> Unit: ...



@overload
def cylinder_volume(radius: Length = ..., height: Length = ..., volume: None = ...) -> Volume: ...

@overload
def cylinder_volume(radius: Length = ..., height: None = ..., volume: Volume = ...) -> Length: ...

@overload
def cylinder_volume(radius: None = ..., height: Length = ..., volume: Volume = ...) -> Length: ...

def cylinder_volume(radius: Length = ..., height: Length = ..., volume: Volume = ...) -> Unit: ...
