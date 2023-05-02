from MyCalc import MyCalc

def test_addition():
    calc = MyCalc()
    assert calc.calc(2, 3, "+") == 5

def test_calc_with_ans():
    calc = MyCalc()
    calc.calc(2, 3, "+")
    assert calc.calc("ans", 4, "+") == 9

def test_subtraction():
    calc = MyCalc()
    assert calc.calc(5, 3, "-") == 2

def test_calc_with_sub():
    calc = MyCalc()
    calc.calc(5, 3, "-")
    assert calc.calc("ans", 1, "-") == 1

def test_multiplication():
    calc = MyCalc()
    assert calc.calc(2, 3, "*") == 6

def test_calc_with_mul():
    calc = MyCalc()
    calc.calc(2, 3, "*")
    assert calc.calc("ans", 4, "*") == 24

def test_division():
    calc = MyCalc()
    assert calc.calc(6, 3, "/") == 2.0

def test_calc_with_div():
    calc = MyCalc()
    calc.calc(20, 2, "/")
    assert calc.calc("ans", 5, "/") == 2

