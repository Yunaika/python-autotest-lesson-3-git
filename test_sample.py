import math

def test_sqrt():
   num = 4
   assert math.sqrt(num) == 2

def test_square():
   num = 3
   assert num*num == 9

def test_quality():
   assert 1 != 7

def test_subtraction():
   num_1 = 10
   num_2 = 5
   assert num_1 - num_2 == 5