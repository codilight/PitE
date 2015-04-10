#!/usr/bin/python

from bramka2_mod import CoinBox
from bramka2_mod import InvalidCoinError
import unittest

class TestCoinBox(unittest.TestCase):
    def setUp(self):
        self.box = CoinBox()
        
    def test_adding_coins_method_with_negative_input(self):
        self.box.empty()
        self.assertRaises(InvalidCoinError, self.box.addCoin, (-3,))
        
    def test_box_suspense_after_invalid_input(self):
        self.box.empty()
        try:
            self.box.addCoin("2")
        except InvalidCoinError:
            pass
        
        self.assertEqual(0, self.box.value())
        self.box.addCoin(2)
        self.assertEqual(0, self.box.value())
        self.box.empty()
        self.box.addCoin(2)
        self.box.addCoin(3)
        self.assertEqual(5, self.box.value())
        
    def test_adding_coins_method_with_string_input(self):
        self.box.empty()
        self.assertRaises(InvalidCoinError, self.box.addCoin, ("2",))
        self.assertEqual(0, self.box.value())
        
    def test_valid_adding_coins(self):
        self.box.empty()
        self.box.addCoin(2)
        self.assertEqual(2, self.box.value())

if __name__ == "__main__":
    unittest.main()