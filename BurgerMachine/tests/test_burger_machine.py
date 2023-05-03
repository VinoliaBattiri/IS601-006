import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

# add required test cases below

"""UCID : vb437 Date: 03/05/2023"""
def test_cost_of_burger(machine1):
    machine1.handle_bun("Wheat Burger Bun")
    machine1.handle_patty("turkey")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("ketchup")
    machine1.handle_toppings("mustard")
    machine1.handle_toppings("done")
    total1 = machine1.calculate_cost()
    assert total1 == 3.75
    assert "${:.2f}".format(total1) == "$3.75"
    machine1.handle_pay(total1,"${:.2f}".format(total1))

    machine1.handle_bun("white burger bun")
    machine1.handle_patty("turkey")
    machine1.handle_patty("next")
    machine1.handle_toppings("done")
    total2 = machine1.calculate_cost()
    assert total2 == 2.5
    assert "${:.2f}".format(total2) == "$2.50"
    machine1.handle_pay(total2,"${:.2f}".format(total2))

    machine1.handle_bun("lettuce wrap")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("tomato")
    machine1.handle_toppings("done")
    total3 = machine1.calculate_cost()
    assert total3 == 2.5
    assert "${:.2f}".format(total3) == "$2.50"
    machine1.handle_pay(total3,"${:.2f}".format(total3))

"""UCID : vb437 Date: 03/05/2023"""
def test_total_sales(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    total1 = machine.calculate_cost()
    machine.handle_pay(total1,"${:.2f}".format(total1))
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    total2 = machine.calculate_cost()
    machine.handle_pay(total2,"${:.2f}".format(total2))
    machine.handle_bun("white Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    total3 = machine.calculate_cost()
    machine.handle_pay(total3,"${:.2f}".format(total3))
    assert machine.total_sales == total1 + total2 + total3

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""

"""UCID : vb437 Date: 03/05/2023"""