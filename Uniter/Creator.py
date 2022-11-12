import os.path


class QuantityFileCreator:

    def __init__(self,quantity_name,quantity_sign) -> None:
        self.__name = quantity_name
        self.__sign = quantity_sign
        self.__units = []
        self.__typeunits = []

    def add_unit(self,unit_name,unit_symbol,multiplier):
        self.__units.append(f'@Unitor("{unit_symbol}", {multiplier})\nclass {unit_name}({self.__name}): pass')
        self.__typeunits.append(f"class {unit_name}({self.__name}[{self.__name}]): pass")
        return self

    def create_file(self, output_dir=""):
        units = "\n\n".join(self.__units)
        typeunits = "\n\n".join(self.__typeunits)
        open(os.path.join(output_dir,f"{self.__name}.py"),"w")\
            .write(f'from Uniter.Uniter import Unit, Unitor, Quantitor\n\n@Quantitor("{self.__sign}")\nclass {self.__name}(Unit): pass\n\n{units}')
        open(os.path.join(output_dir,f"{self.__name}.pyi"),"w")\
            .write(f"from Uniter.Uniter import Unit, __Q\n\nclass {self.__name}(Unit[__Q]): pass\n\n{typeunits}")