import pytest
from working import convert

def test_regular_cases():
    assert convert("9 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"

def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "0:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "0:00 to 12:00"

def test_crossing_midnight():
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 0:01"
    assert convert("5 PM to 9 AM") == "17:00 to 9:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")      # hour out of range
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")    # invalid minute
    with pytest.raises(ValueError):
        convert("9AM to 5PM")         # missing spaces
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")        # wrong separator
