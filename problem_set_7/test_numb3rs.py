from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")
    assert validate("0.0.0.0")

def test_invalid_range():
    assert not validate("256.0.0.1")
    assert not validate("275.3.6.28")
    assert not validate("1.2.3.999")

def test_invalid_format():
    assert not validate("1.2.3")
    assert not validate("1.2.3.4.5")
    assert not validate("hello")
    assert not validate("1..2.3")
