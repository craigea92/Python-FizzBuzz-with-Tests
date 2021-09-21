import unittest
import sys

sys.path.append('/Users/mehulchauhan/After-Makers/FizzBuzz-Python/lib')

from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
  def test_fizz(self):
    for i in [3, 6, 9, 18]:
      print('testing', i)
      assert fizzbuzz(i) == 'Fizz'
  
  def test_buzz(self):
    for i in [5, 10, 50, 100]:
      print('testing', i)
      assert fizzbuzz(i) == 'Buzz'
