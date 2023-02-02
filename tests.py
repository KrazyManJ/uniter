import unittest

from uniter import Parser, Formulas
from uniter.units import *
from uniter.Exceptions import *
from uniter.Uniter import Unit
from uniter.units.Length import Length

class UniterTestCase(unittest.TestCase):

    def test_conversion(self):
        self.assertEqual(DM(80).convert_to(M), M(8))
        self.assertEqual(DM(80)[M], M(8))
        self.assertRaises(UnitConversionError, DM(80).convert_to, KG)

    def test_parser(self):
        self.assertEqual(Parser.parse("5km + 200m"), KM(5.2))
        self.assertEqual(Parser.parse("5kmph",{"kmph":KMH}), KMH(5))
        self.assertRaises(UnknownUnitError, Parser.parse, "5unit + 8m - 4dm")

    def test_logical_operators(self):
        self.assertTrue(KM(5) == M(5000))
        self.assertFalse(KM(5) == DM(5000))
        self.assertTrue(KM(5) != DM(500))
        self.assertFalse(KM(5) != DM(50000))
        self.assertTrue(KM(5) > KM(2))
        self.assertFalse(DM(1) > M(1))
        self.assertTrue(KM(2) < KM(3))
        self.assertFalse(DM(100) < M(1))
        self.assertTrue(KM(5) >= KM(2))
        self.assertTrue(KM(5) >= KM(5))
        self.assertFalse(DM(1) >= M(1))
        self.assertTrue(KM(2) <= KM(3))
        self.assertTrue(KM(3) <= KM(3))
        self.assertFalse(DM(100) <= M(1))

    def test_mathematical_operators(self):
        self.assertEqual(KM(5)+DM(2),DM(50002))
        self.assertEqual(M(8)-CM(30),M(7.7))
        self.assertRaises(UnitArithmeticError,lambda a,b: a-b,M(80),KG(7))
        self.assertEqual(M(8)*5,M(40))
        self.assertEqual(M(8)/5,M(8/5))
        self.assertRaises(UnitArithmeticError,lambda a,b: a*b,M(80),KG(7))
        self.assertEqual(M(8)//5,M(1))
        self.assertEqual(M(2)**8,M(256))
        self.assertRaises(UnitArithmeticError,lambda a,b: a**b,M(80),KG(7))

    def test_temperature_conversion(self):
        self.assertEqual(DEG_C(1),DEG_F(33.8))
        self.assertEqual(DEG_C(1),DEG_K(274.15))
        self.assertEqual(DEG_K(1),DEG_F(-457.87))

    def test_angle_conversion(self):
        from math import pi
        self.assertEqual(DEG(360),RAD(2*pi))
        self.assertEqual(RAD(2*pi),DEG(360))

    def test_instantiation_error(self):
        self.assertRaises(UnitInstatiateError, Unit, 5)
        self.assertRaises(UnitInstatiateError, M.__base__, 5)

    def test_formulas(self):

        self.assertRaises(UnitFormulaParameterError,Formulas.ohms_law,resistance=5, voltage=Volt(30))
        self.assertRaises(UnitFormulaParameterError,Formulas.ohms_law,resistance=KM(8), voltage=Volt(30))
        self.assertRaises(UnitFormulaParameterError,Formulas.ohms_law,resistance=OHM(50),voltage=Volt(30),electric_current=A(0.6))
        self.assertRaises(UnitFormulaParameterError,Formulas.ohms_law,resistance=OHM(50))
        self.assertRaises(UnitFormulaParameterError,Formulas.ohms_law,{})

        self.assertEqual(Formulas.ohms_law(resistance=OHM(50),voltage=Volt(30)),A(0.6))
        self.assertEqual(Formulas.average_speed(distance=M(45),time=SEC(30)),MS(1.5))


if __name__ == '__main__':
    unittest.main()
