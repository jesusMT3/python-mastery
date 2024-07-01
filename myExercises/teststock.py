import unittest
from stock import *

class TestStock(unittest.TestCase):
    
    # Unit tests
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_keyword_arguments(self):
        s = Stock(name = 'GOOG',shares = 100, price = 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
        
    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(40)
        self.assertEqual(s.shares, 60)
        
    def test_from_row(self):
        s = Stock.from_row(['GOOG', 100, 490.1])
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")
        
    def test_eq(self):
        a = Stock('GOOG', 100, 490.1)
        b = Stock('GOOG', 100, 490.1)
        self.assertTrue(a==b)
        
    # Unit tests with expected errors
    def test_shares_string(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'
            
    def test_negative_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50
            
    def test_price_string(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '100'
            
    def test_negative_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -100.1
            
    def test_non_existent_attribute(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 100
        
if __name__ == '__main__':
    unittest.main()