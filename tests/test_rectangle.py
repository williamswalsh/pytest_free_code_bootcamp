####################
# Class based tests
####################
import pytest

from source import shapes

def test_area(my_rectangle):
    assert my_rectangle.area() == 20 * 10


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (2 * 10) + (2 * 20)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
