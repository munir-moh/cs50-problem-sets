from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ABC123") == True

def test_too_short_or_too_long():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_non_alpha_start():
    assert is_valid("1ABC") == False
    assert is_valid("9CS50") == False

def test_numbers_not_at_end():
    assert is_valid("AB1C") == False
    assert is_valid("CS50X1") == False

def test_leading_zero_in_number():
    assert is_valid("AB01") == False
