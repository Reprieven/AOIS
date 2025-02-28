import Conversion 
import unittest
class TestDecimalToBinDirect(unittest.TestCase):
    def test_convert_int_positive(self):
        decimal = 18
        bin = [0,0,0,1,0,0,1,0]
        self.assertEqual(Conversion.decimal_to_bin_direct(decimal),bin)

    def test_convert_int_negative(self):
        decimal = -37
        bin = [1,0,1,0,0,1,0,1]
        self.assertEqual(Conversion.decimal_to_bin_direct(decimal),bin)

    def test_convert_fractional(self):
        decimal = 33.75
        bin = [0,0,1,0,0,0,0,1,1,1,0,0,0]
        self.assertEqual(Conversion.decimal_to_bin_direct(decimal),bin)

class TestDecimalToBinInverse(unittest.TestCase):
    def test_convert_int_positive(self):
        decimal = 18
        bin = [0,0,0,1,0,0,1,0]
        self.assertEqual(Conversion.decimal_to_bin_inverse(decimal),bin)

    def test_convert_int_negative(self):
        decimal = -118
        bin = [1,0,0,0,1,0,0,1]
        self.assertEqual(Conversion.decimal_to_bin_inverse(decimal),bin)
    
class TestDecimalToBinComplement(unittest.TestCase):
    def test_convert_int_positive(self):
        decimal = 18
        bin = [0,0,0,1,0,0,1,0]
        self.assertEqual(Conversion.decimal_to_bin_complement(decimal),bin)
    
    def test_convert_int_negative(self):
        decimal = -118
        bin = [1,0,0,0,1,0,1,0]
        self.assertEqual(Conversion.decimal_to_bin_complement(decimal),bin)

class TestComplementToDirect(unittest.TestCase):
    def conversion_test(self):
        bin_complement = [1,0,0,0,1,0,1,0]
        bin_direct = [1,1,1,1,0,1,1,0]
        self.assertEqual(bin_direct,Conversion.complement_to_direct(bin_complement))

class TestBinToDecimal(unittest.TestCase):
    def test_convert_int_positive(self):
        bin_direct = [0,1,1,1,0,1,1,0]
        self.assertEqual(Conversion.bin_to_decimal(bin_direct), 118)
    def test_convert_int_negative(self):
        bin_direct = [1,0,0,0,0,0,1,0]
        self.assertEqual(Conversion.bin_to_decimal(bin_direct),-2)
class TestBinToDecimalFractional(unittest.TestCase):
    def test_convert(self):
        bin_fractional = [1,1,1,0,0]
        self.assertEqual(Conversion.bin_to_decimal_fractional(bin_fractional), 0.875)

class TestDecimalToBinIEEE754(unittest.TestCase):
    def test_convert(self):
        decimal = 1.23459
        bin_IEEE754 = [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1]
        self.assertEqual(Conversion.decimal_to_bin_ieee754(decimal),bin_IEEE754)

class TestBinIEEE754ToDecimal(unittest.TestCase):
    def test_convert(self):
        decimal = 6 
        bin = [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(Conversion.bin_to_decimal_ieee754(bin),decimal)
