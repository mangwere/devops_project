import random
import unittest

def add(x, y):
  return x + y
  
       # This function subtracts two numbers
def subtract(x, y):
  return x - y

  # This function multiplies two numbers

def multiply(x, y):
  return x * y

   # This function divides two numbers
def divide(x, y):
  return x / y

class Test(unittest.TestCase):
  def test_add(self):
    res = add(2,3)
    self.assertEqual(res, 5)
  def test_sub(self) :
    res = subtract(1,1)
    self.assertEqual(res, 0)
  def test_mult(self):
    res = multiply(2,2)
    self.assertEqual(res, 4)
  def test_div(self) :
    res = divide(4,2)
    self.assertEqual(res-1, 2)


if __name__ == '__main__':
  unittest.main()
