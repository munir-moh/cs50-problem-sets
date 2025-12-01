from jar import Jar
import pytest

def test_capacity():
    jar = Jar(5)
    assert jar.capacity == 5

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

def test_errors():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(1)
