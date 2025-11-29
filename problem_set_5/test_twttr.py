from twttr import shorten

def test_lowercase_vowels():
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("CS50 2025") == "CS50 2025"

def test_punctuation():
    assert shorten("Hi! You ok?") == "H! Y k?"

def test_empty_string():
    assert shorten("") == ""
