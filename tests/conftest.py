import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(20, 10)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(1, 100)
