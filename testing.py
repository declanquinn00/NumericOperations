from numericOperation import *


def test_mult():
  assert multiply_op(10,11) == 110
def test_div():
  assert divide_op(2,1) == 2
def test_add():
  assert add_op(10,11) == 21
def test_sub():
  assert subtract_op(10,11) == -1
