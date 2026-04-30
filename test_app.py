from app import add, subtract, multiply, divide, square
from app import is_even, find_biggest, calculate_average, greet_user


def test_add():
    assert add(25, 4) == 29


def test_subtract():
    assert subtract(20, 5) == 15


def test_multiply():
    assert multiply(7, 5) == 35


def test_divide():
    assert divide(60, 2) == 30



def test_divide_by_zero():
    assert divide(10, 0) == "Cannot divide by zero"


def test_square():
    assert square(7) == 49


def test_is_even_true():
    assert is_even(10) == True


def test_is_even_false():
    assert is_even(9) == False


def test_find_biggest():
    assert find_biggest(50, 80) == 80


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_empty_average():
    assert calculate_average([]) == 0


def test_greet_user():
    assert greet_user("Sukand") == "Hello Sukand, welcome to Jenkins Testing Project!"