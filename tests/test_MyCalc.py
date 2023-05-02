from MyCalc import MyCalc


def test_add():
    calc = MyCalc()
    check = calc.add(2, 2)
    assert check == 4

def test_number_add_number():
    calc = MyCalc()
    calc.add(2)
    calc.add(3)
    assert calc.ans == 5

def test_ans_add_number():
    calc = MyCalc()
    calc.add(2)
    calc.add(3)
    calc.add("ans")
    assert calc.ans == 10

def test_number_subtract_number():
    calc = MyCalc()
    calc.subtract(5)
    calc.subtract(2)
    assert calc.ans == -3

def test_ans_subtract_number():
    calc = MyCalc()
    calc.add(5)
    calc.subtract(2)
    calc.subtract("ans")
    assert calc.ans == -2

def test_number_multiply_number():
    calc = MyCalc()
    calc.add(3)
    calc.multiply(4)
    assert calc.ans == 12

def test_ans_multiply_number():
    calc = MyCalc()
    calc.add(3)
    calc.multiply(4)
    calc.multiply("ans")
    assert calc.ans == 144

def test_number_divide_number():
    calc = MyCalc()
    calc.add(8)
    calc.divide(2)
    assert calc.ans == 4

def test_ans_divide_number():
    calc = MyCalc()
    calc.add(8)
    calc.divide(2)
    calc.divide("ans")
    assert calc.ans == 1

