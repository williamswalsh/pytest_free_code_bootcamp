########################
# Function Based Tests
########################
import time
import pytest
from source import my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add("I like ", "burgers")
    assert result == "I like burgers"


def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_too_slow():
    # Slow test
    time.sleep(5)
    result = my_functions.divide(10, 2)
    assert result == 5


@pytest.mark.skip(reason="This feature is broken. See JIRA WW-1369")
def test_to_be_skipped():
    time.sleep(5)
    result = my_functions.divide(10, 2)
    assert result == 5


@pytest.mark.william
def test_to_be_conditionally_executed():
    result = my_functions.divide(10, 2)
    assert result == 5


@pytest.mark.xfail(reason="Cannot divide by zero")
def test_to_be_conditionally_executed():
    a = 10 / 0