class default_exception_module:
    def __call__(self, cls):
        cls.__module__ = Exception.__module__
        return cls


@default_exception_module()
class UnitInstatiateError(Exception): pass

@default_exception_module()
class UnitConversionError(Exception): pass

@default_exception_module()
class UnitArithmeticError(Exception): pass

@default_exception_module()
class UnitInheritanceError(Exception): pass

@default_exception_module()
class UnitBaseClassError(Exception): pass

@default_exception_module()
class UnitQuantitorError(Exception): pass

@default_exception_module()
class UnitUnitorError(Exception): pass

@default_exception_module()
class UnknownUnitError(Exception): pass

@default_exception_module()
class UnitFormulaParameterError(Exception): pass


