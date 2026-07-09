from myapp.py import add, subtract

def test_add():
    assert add(6,7) == 13

def test_subtract():
    assert subtract(6,7) == -1

    