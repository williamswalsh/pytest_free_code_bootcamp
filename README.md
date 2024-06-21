# PyTest course

### Running a test file
```shell

# Execute tests in test.py
pytest <FILE>
pytest test.py

# Enable console output (-s)
pytest -s test.py
pytest -s <FILE>

# This will execute tests marked with: @pytest.mark.slow
pytest -m <mark>
pytest -m slow

# Disable warnings
# Can create a python.ini with custom marker definition or:
pytest -m <mark> --disable-pytest-warnings
pytest -m webtest    --disable-pytest-warnings
```

### Marking tests for conditional execution special marks
```python
# skip - you skip a test intentionally 
@pytest.mark.skip(reason="Reason for skipping test.")
def test_something():
  pass
# When running test file that has a skipped test it will appear as follows:  
# tests/test_my_functions.py .....s.   s is the skipped test


# xfail
@pytest.mark.xfail(reason="I expect this test to fail for some reason")
def test_something():
  pass
```

### conftest.py
Config file used to store pytest fixtures.  
```python
import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(20, 10)
```


### Parameterised Test
Mark the test with the parameterize mark
```python
#                       ("params comma-separated",     [tuple,   tuple  ])
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area
```