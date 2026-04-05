from daily_codes.calculator import add, subtract

def test_add():
    # This checks if the exact output of add(2, 3) is 5
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    # This checks if the exact output of subtract(5, 3) is 2
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
