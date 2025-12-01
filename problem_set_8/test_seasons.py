from seasons import get_date
from datetime import date

def test_valid_date():
    assert get_date("2000-01-01") == date(2000, 1, 1)

def test_invalid_format():
    assert get_date("01-01-2000") is None

def test_invalid_date():
    assert get_date("2023-02-30") is None
